#!/usr/bin/env python3
"""
Tests for Lyra's email client — attachment downloading feature.

Run: cd scripts && python3 -m pytest test_email_client.py -v
"""

import email
import json
import os
import tempfile
import unittest
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from unittest.mock import MagicMock, patch

from email_client import (
    _format_bytes,
    deduplicate_filename,
    download_attachments,
    extract_attachment_metadata,
    read_email,
    sanitize_filename,
    send_email,
)


# ---------------------------------------------------------------------------
# Helpers to build fake MIME messages
# ---------------------------------------------------------------------------

def _make_simple_text_email(body="Hello world"):
    """A plain text email with no attachments."""
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = "Simple"
    msg["From"] = "alice@example.com"
    msg["To"] = "lyra@example.com"
    return msg


def _make_email_with_attachments(text_body="See attached.", attachments=None):
    """
    Build a multipart/mixed email with a text body and optional attachments.
    Each attachment is a dict: {filename, content_bytes, content_type, maintype, subtype}.
    """
    msg = MIMEMultipart("mixed")
    msg["Subject"] = "Files for you"
    msg["From"] = "alice@example.com"
    msg["To"] = "lyra@example.com"

    msg.attach(MIMEText(text_body, "plain", "utf-8"))

    for att in (attachments or []):
        part = MIMEApplication(att["content_bytes"], Name=att["filename"])
        part.add_header("Content-Disposition", "attachment", filename=att["filename"])
        if "content_type" in att:
            part.replace_header("Content-Type", att["content_type"])
        msg.attach(part)

    return msg


def _make_email_with_inline_image(text_body="Look at this"):
    """Email with an inline image (Content-Disposition: inline)."""
    msg = MIMEMultipart("related")
    msg["Subject"] = "Inline pic"
    msg["From"] = "alice@example.com"
    msg["To"] = "lyra@example.com"

    msg.attach(MIMEText(text_body, "plain", "utf-8"))

    # 1x1 red PNG pixel
    png_data = (
        b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
        b"\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00"
        b"\x00\x00\x0cIDATx\x9cc\xf8\x0f\x00\x00\x01\x01\x00"
        b"\x05\x18\xd8N\x00\x00\x00\x00IEND\xaeB`\x82"
    )
    img_part = MIMEImage(png_data, "png")
    img_part.add_header("Content-Disposition", "inline", filename="logo.png")
    img_part.add_header("Content-ID", "<logo@example.com>")
    msg.attach(img_part)

    return msg


def _make_email_html_only():
    """An email where the body is HTML — no text/plain, no attachments."""
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "HTML email"
    msg["From"] = "alice@example.com"
    msg["To"] = "lyra@example.com"
    msg.attach(MIMEText("<h1>Hello</h1>", "html", "utf-8"))
    return msg


def _make_envelope(subject="Test", from_email="alice@example.com", message_id="<abc@example.com>"):
    """Build a mock ENVELOPE object like imapclient returns."""
    env = MagicMock()
    env.subject = subject.encode() if subject else None
    env.date = "2025-01-15 10:00:00"
    env.message_id = message_id.encode() if message_id else None

    from_part = MagicMock()
    user, host = from_email.split("@")
    from_part.mailbox = MagicMock()
    from_part.mailbox.decode = MagicMock(return_value=user)
    from_part.host = MagicMock()
    from_part.host.decode = MagicMock(return_value=host)
    env.from_ = [from_part]

    return env


# ===========================================================================
# Test Classes
# ===========================================================================

class TestSanitizeFilename(unittest.TestCase):
    """sanitize_filename should defend against path traversal and bad chars."""

    def test_strips_directory_components(self):
        self.assertEqual(sanitize_filename("../../etc/passwd"), "passwd")

    def test_strips_backslash_paths(self):
        self.assertEqual(sanitize_filename("C:\\Users\\evil\\payload.exe"), "payload.exe")

    def test_removes_null_bytes(self):
        self.assertEqual(sanitize_filename("file\x00name.txt"), "filename.txt")

    def test_removes_special_characters(self):
        result = sanitize_filename('file<>:"|?*name.txt')
        self.assertNotIn("<", result)
        self.assertNotIn(">", result)
        self.assertNotIn(":", result)
        self.assertNotIn('"', result)
        self.assertNotIn("|", result)
        self.assertNotIn("?", result)
        self.assertNotIn("*", result)
        self.assertTrue(result.endswith(".txt"))

    def test_empty_name_gets_default(self):
        result = sanitize_filename("")
        self.assertTrue(len(result) > 0)
        self.assertIn("attachment", result)

    def test_whitespace_only_gets_default(self):
        result = sanitize_filename("   ")
        self.assertTrue(len(result) > 0)
        self.assertIn("attachment", result)

    def test_long_name_truncated(self):
        long_name = "a" * 300 + ".pdf"
        result = sanitize_filename(long_name)
        self.assertLessEqual(len(result), 200)
        self.assertTrue(result.endswith(".pdf"))

    def test_normal_filename_unchanged(self):
        self.assertEqual(sanitize_filename("report.pdf"), "report.pdf")

    def test_none_gets_default(self):
        result = sanitize_filename(None)
        self.assertIn("attachment", result)


class TestDeduplicateFilename(unittest.TestCase):
    """deduplicate_filename should append _2, _3 etc. on conflicts."""

    def test_no_conflict(self):
        with tempfile.TemporaryDirectory() as d:
            result = deduplicate_filename(d, "report.pdf")
            self.assertEqual(result, "report.pdf")

    def test_single_conflict(self):
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, "report.pdf"), "w").close()
            result = deduplicate_filename(d, "report.pdf")
            self.assertEqual(result, "report_2.pdf")

    def test_multiple_conflicts(self):
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, "report.pdf"), "w").close()
            open(os.path.join(d, "report_2.pdf"), "w").close()
            result = deduplicate_filename(d, "report.pdf")
            self.assertEqual(result, "report_3.pdf")

    def test_no_extension(self):
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, "README"), "w").close()
            result = deduplicate_filename(d, "README")
            self.assertEqual(result, "README_2")


class TestFormatBytes(unittest.TestCase):
    """_format_bytes should produce human-readable sizes."""

    def test_bytes(self):
        self.assertEqual(_format_bytes(500), "500 B")

    def test_kilobytes(self):
        result = _format_bytes(1024)
        self.assertIn("KB", result)

    def test_megabytes(self):
        result = _format_bytes(1024 * 1024)
        self.assertIn("MB", result)

    def test_gigabytes(self):
        result = _format_bytes(1024 ** 3)
        self.assertIn("GB", result)

    def test_zero(self):
        self.assertEqual(_format_bytes(0), "0 B")


class TestExtractAttachmentMetadata(unittest.TestCase):
    """extract_attachment_metadata should find attachments in a MIME message."""

    def test_no_attachments(self):
        msg = _make_simple_text_email()
        result = extract_attachment_metadata(msg)
        self.assertEqual(result, [])

    def test_one_attachment(self):
        msg = _make_email_with_attachments(attachments=[
            {"filename": "report.pdf", "content_bytes": b"fake-pdf-content"},
        ])
        result = extract_attachment_metadata(msg)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["filename"], "report.pdf")
        self.assertIn("size", result[0])
        self.assertIn("size_human", result[0])

    def test_multiple_attachments(self):
        msg = _make_email_with_attachments(attachments=[
            {"filename": "a.pdf", "content_bytes": b"x" * 100},
            {"filename": "b.csv", "content_bytes": b"y" * 200},
        ])
        result = extract_attachment_metadata(msg)
        self.assertEqual(len(result), 2)
        filenames = {a["filename"] for a in result}
        self.assertEqual(filenames, {"a.pdf", "b.csv"})

    def test_inline_image_included(self):
        """Inline images (Content-Disposition: inline) with filenames should be included."""
        msg = _make_email_with_inline_image()
        result = extract_attachment_metadata(msg)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["filename"], "logo.png")

    def test_html_body_not_counted(self):
        """HTML body parts should not be counted as attachments."""
        msg = _make_email_html_only()
        result = extract_attachment_metadata(msg)
        self.assertEqual(result, [])

    def test_synthesized_filename(self):
        """If an attachment has no filename, one should be synthesized."""
        msg = MIMEMultipart("mixed")
        msg.attach(MIMEText("body", "plain"))
        part = MIMEApplication(b"data", "octet-stream")
        part.add_header("Content-Disposition", "attachment")
        # No filename parameter
        msg.attach(part)
        result = extract_attachment_metadata(msg)
        self.assertEqual(len(result), 1)
        self.assertIn("attachment", result[0]["filename"])


class TestDownloadAttachments(unittest.TestCase):
    """download_attachments should save files to disk."""

    @patch("email_client.MAIL_DIR")
    @patch("email_client.IMAPClient")
    def test_saves_file(self, MockIMAPClient, mock_mail_dir):
        with tempfile.TemporaryDirectory() as tmpdir:
            mock_mail_dir.__str__ = lambda s: tmpdir
            # Patch MAIL_DIR at module level
            with patch("email_client.MAIL_DIR", tmpdir):
                msg = _make_email_with_attachments(attachments=[
                    {"filename": "report.pdf", "content_bytes": b"PDF-content-here"},
                ])

                mock_client = MagicMock()
                MockIMAPClient.return_value.__enter__ = MagicMock(return_value=mock_client)
                MockIMAPClient.return_value.__exit__ = MagicMock(return_value=False)
                mock_client.fetch.return_value = {
                    42: {b"BODY[]": msg.as_bytes()}
                }

                result = download_attachments(42)

                self.assertEqual(result["status"], "ok")
                self.assertEqual(result["attachment_count"], 1)
                self.assertEqual(result["files"][0]["filename"], "report.pdf")
                # Verify file was actually written
                saved_path = result["files"][0]["path"]
                self.assertTrue(os.path.exists(saved_path))
                with open(saved_path, "rb") as f:
                    self.assertEqual(f.read(), b"PDF-content-here")

    @patch("email_client.IMAPClient")
    def test_no_attachments(self, MockIMAPClient):
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("email_client.MAIL_DIR", tmpdir):
                msg = _make_simple_text_email()

                mock_client = MagicMock()
                MockIMAPClient.return_value.__enter__ = MagicMock(return_value=mock_client)
                MockIMAPClient.return_value.__exit__ = MagicMock(return_value=False)
                mock_client.fetch.return_value = {
                    42: {b"BODY[]": msg.as_bytes()}
                }

                result = download_attachments(42)

                self.assertEqual(result["status"], "ok")
                self.assertEqual(result["attachment_count"], 0)
                self.assertEqual(result["files"], [])

    @patch("email_client.IMAPClient")
    def test_uid_not_found(self, MockIMAPClient):
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("email_client.MAIL_DIR", tmpdir):
                mock_client = MagicMock()
                MockIMAPClient.return_value.__enter__ = MagicMock(return_value=mock_client)
                MockIMAPClient.return_value.__exit__ = MagicMock(return_value=False)
                mock_client.fetch.return_value = {}

                result = download_attachments(999)

                self.assertIn("error", result)

    @patch("email_client.IMAPClient")
    def test_duplicate_filenames(self, MockIMAPClient):
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("email_client.MAIL_DIR", tmpdir):
                msg = _make_email_with_attachments(attachments=[
                    {"filename": "data.csv", "content_bytes": b"first"},
                    {"filename": "data.csv", "content_bytes": b"second"},
                ])

                mock_client = MagicMock()
                MockIMAPClient.return_value.__enter__ = MagicMock(return_value=mock_client)
                MockIMAPClient.return_value.__exit__ = MagicMock(return_value=False)
                mock_client.fetch.return_value = {
                    42: {b"BODY[]": msg.as_bytes()}
                }

                result = download_attachments(42)

                self.assertEqual(result["attachment_count"], 2)
                filenames = {f["filename"] for f in result["files"]}
                self.assertEqual(len(filenames), 2)  # Should be deduplicated

    @patch("email_client.IMAPClient")
    def test_binary_content(self, MockIMAPClient):
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("email_client.MAIL_DIR", tmpdir):
                binary_data = bytes(range(256))
                msg = _make_email_with_attachments(attachments=[
                    {"filename": "binary.bin", "content_bytes": binary_data},
                ])

                mock_client = MagicMock()
                MockIMAPClient.return_value.__enter__ = MagicMock(return_value=mock_client)
                MockIMAPClient.return_value.__exit__ = MagicMock(return_value=False)
                mock_client.fetch.return_value = {
                    42: {b"BODY[]": msg.as_bytes()}
                }

                result = download_attachments(42)

                saved_path = result["files"][0]["path"]
                with open(saved_path, "rb") as f:
                    content = f.read()
                self.assertEqual(content, binary_data)


class TestReadEmailWithAttachments(unittest.TestCase):
    """read_email should include attachment metadata in its return dict."""

    @patch("email_client.MAIL_DIR")
    @patch("email_client.IMAPClient")
    def test_metadata_included(self, MockIMAPClient, mock_mail_dir):
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("email_client.MAIL_DIR", tmpdir):
                msg = _make_email_with_attachments(
                    text_body="Please see attached.",
                    attachments=[
                        {"filename": "doc.pdf", "content_bytes": b"x" * 1000},
                        {"filename": "img.png", "content_bytes": b"y" * 2000},
                    ],
                )
                env = _make_envelope(subject="Files for you")

                mock_client = MagicMock()
                MockIMAPClient.return_value.__enter__ = MagicMock(return_value=mock_client)
                MockIMAPClient.return_value.__exit__ = MagicMock(return_value=False)
                mock_client.fetch.return_value = {
                    7: {
                        b"BODY[]": msg.as_bytes(),
                        b"ENVELOPE": env,
                    }
                }

                result = read_email(7)

                self.assertNotIn("error", result)
                self.assertEqual(result["attachment_count"], 2)
                self.assertEqual(len(result["attachments"]), 2)
                self.assertIn("total_attachment_size_human", result)

    @patch("email_client.MAIL_DIR")
    @patch("email_client.IMAPClient")
    def test_zero_attachments(self, MockIMAPClient, mock_mail_dir):
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("email_client.MAIL_DIR", tmpdir):
                msg = _make_simple_text_email("Just text, no files.")
                env = _make_envelope(subject="Simple")

                mock_client = MagicMock()
                MockIMAPClient.return_value.__enter__ = MagicMock(return_value=mock_client)
                MockIMAPClient.return_value.__exit__ = MagicMock(return_value=False)
                mock_client.fetch.return_value = {
                    8: {
                        b"BODY[]": msg.as_bytes(),
                        b"ENVELOPE": env,
                    }
                }

                result = read_email(8)

                self.assertNotIn("error", result)
                self.assertEqual(result["attachment_count"], 0)
                self.assertEqual(result["attachments"], [])


class TestSendEmailAttachments(unittest.TestCase):
    """send_email should support file attachments."""

    @patch("email_client.MAIL_DIR")
    @patch("email_client.smtplib")
    def test_send_with_one_attachment(self, mock_smtplib, mock_mail_dir):
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("email_client.MAIL_DIR", tmpdir):
                # Create a fake PDF file
                pdf_path = os.path.join(tmpdir, "paper.pdf")
                with open(pdf_path, "wb") as f:
                    f.write(b"%PDF-1.4 fake pdf content")

                mock_server = MagicMock()
                mock_smtplib.SMTP_SSL.return_value.__enter__ = MagicMock(return_value=mock_server)
                mock_smtplib.SMTP_SSL.return_value.__exit__ = MagicMock(return_value=False)

                result = send_email(
                    "cale@example.com", "Paper draft", "See attached.",
                    attachments=[pdf_path],
                )

                self.assertEqual(result["status"], "sent")
                self.assertEqual(len(result["attachments"]), 1)
                self.assertEqual(result["attachments"][0]["filename"], "paper.pdf")

                # Verify SMTP was called with a message containing the attachment
                mock_server.send_message.assert_called_once()
                sent_msg = mock_server.send_message.call_args[0][0]
                parts = list(sent_msg.walk())
                # Should have: multipart container, text body, attachment
                content_types = [p.get_content_type() for p in parts]
                self.assertIn("application/pdf", content_types)

    @patch("email_client.MAIL_DIR")
    @patch("email_client.smtplib")
    def test_send_with_multiple_attachments(self, mock_smtplib, mock_mail_dir):
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("email_client.MAIL_DIR", tmpdir):
                pdf_path = os.path.join(tmpdir, "paper.pdf")
                with open(pdf_path, "wb") as f:
                    f.write(b"%PDF-1.4 content")
                csv_path = os.path.join(tmpdir, "data.csv")
                with open(csv_path, "w") as f:
                    f.write("a,b,c\n1,2,3\n")

                mock_server = MagicMock()
                mock_smtplib.SMTP_SSL.return_value.__enter__ = MagicMock(return_value=mock_server)
                mock_smtplib.SMTP_SSL.return_value.__exit__ = MagicMock(return_value=False)

                result = send_email(
                    "bob@example.com", "Files", "Two files attached.",
                    attachments=[pdf_path, csv_path],
                )

                self.assertEqual(result["status"], "sent")
                self.assertEqual(len(result["attachments"]), 2)
                filenames = {a["filename"] for a in result["attachments"]}
                self.assertEqual(filenames, {"paper.pdf", "data.csv"})

    def test_send_with_missing_attachment(self):
        result = send_email(
            "bob@example.com", "Oops", "Missing file.",
            attachments=["/nonexistent/file.pdf"],
        )
        self.assertEqual(result["status"], "error")
        self.assertIn("not found", result["error"])

    def test_send_with_oversized_attachment(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            big_path = os.path.join(tmpdir, "huge.bin")
            # Create a file just over 25MB (using seek to avoid actually writing 25MB)
            with open(big_path, "wb") as f:
                f.seek(26 * 1024 * 1024)
                f.write(b"\0")

            result = send_email(
                "bob@example.com", "Too big", "This won't work.",
                attachments=[big_path],
            )
            self.assertEqual(result["status"], "error")
            self.assertIn("too large", result["error"].lower())

    @patch("email_client.MAIL_DIR")
    @patch("email_client.smtplib")
    def test_send_without_attachments_unchanged(self, mock_smtplib, mock_mail_dir):
        """Sending without attachments should work exactly as before."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("email_client.MAIL_DIR", tmpdir):
                mock_server = MagicMock()
                mock_smtplib.SMTP_SSL.return_value.__enter__ = MagicMock(return_value=mock_server)
                mock_smtplib.SMTP_SSL.return_value.__exit__ = MagicMock(return_value=False)

                result = send_email("alice@example.com", "Hi", "Hello!")

                self.assertEqual(result["status"], "sent")
                self.assertNotIn("attachments", result)

    @patch("email_client.MAIL_DIR")
    @patch("email_client.smtplib")
    def test_attachment_logged_in_sent_json(self, mock_smtplib, mock_mail_dir):
        """Sent email log should include attachment metadata."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("email_client.MAIL_DIR", tmpdir):
                pdf_path = os.path.join(tmpdir, "doc.pdf")
                with open(pdf_path, "wb") as f:
                    f.write(b"pdf-bytes")

                mock_server = MagicMock()
                mock_smtplib.SMTP_SSL.return_value.__enter__ = MagicMock(return_value=mock_server)
                mock_smtplib.SMTP_SSL.return_value.__exit__ = MagicMock(return_value=False)

                send_email("bob@example.com", "Doc", "Here.", attachments=[pdf_path])

                # Find the log file
                sent_dir = os.path.join(tmpdir, "sent")
                log_files = os.listdir(sent_dir)
                self.assertEqual(len(log_files), 1)
                with open(os.path.join(sent_dir, log_files[0])) as f:
                    log = json.load(f)
                self.assertIn("attachments", log)
                self.assertEqual(log["attachments"][0]["filename"], "doc.pdf")


if __name__ == "__main__":
    unittest.main()

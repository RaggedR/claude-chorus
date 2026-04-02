#!/usr/bin/env python3
"""
Tests for Gmail MCP server — verifies that MCP tools correctly delegate
to email_client functions and return structured results.

Run: cd scripts && python3 -m pytest test_email_mcp_server.py -v
"""

import unittest
from unittest.mock import patch

from email_mcp_server import check_inbox, read_email, send_email, download_attachments, mark_as_read


class TestCheckInbox(unittest.TestCase):
    """check_inbox tool should delegate to email_client.check_inbox."""

    @patch("email_mcp_server.email_client")
    def test_defaults(self, mock_ec):
        mock_ec.check_inbox.return_value = [
            {"uid": 10, "from": "alice@example.com", "subject": "Hello", "date": "2025-01-15", "unread": True, "message_id": "<abc@example.com>"},
        ]

        result = check_inbox()

        mock_ec.check_inbox.assert_called_once_with(unread_only=True, limit=10)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["uid"], 10)

    @patch("email_mcp_server.email_client")
    def test_custom_params(self, mock_ec):
        mock_ec.check_inbox.return_value = []

        result = check_inbox(unread_only=False, limit=5)

        mock_ec.check_inbox.assert_called_once_with(unread_only=False, limit=5)
        self.assertEqual(result, [])

    @patch("email_mcp_server.email_client")
    def test_error_propagated(self, mock_ec):
        mock_ec.check_inbox.return_value = [{"error": "Login failed"}]

        result = check_inbox()

        self.assertIn("error", result[0])


class TestReadEmail(unittest.TestCase):
    """read_email tool should delegate to email_client.read_email."""

    @patch("email_mcp_server.email_client")
    def test_reads_by_uid(self, mock_ec):
        mock_ec.read_email.return_value = {
            "uid": 42,
            "from": "bob@example.com",
            "subject": "Meeting notes",
            "body": "Here are the notes...",
            "date": "2025-01-15",
            "message_id": "<xyz@example.com>",
            "attachment_count": 0,
            "attachments": [],
            "total_attachment_size_human": "0 B",
        }

        result = read_email(uid=42)

        mock_ec.read_email.assert_called_once_with(42)
        self.assertEqual(result["uid"], 42)
        self.assertEqual(result["subject"], "Meeting notes")

    @patch("email_mcp_server.email_client")
    def test_not_found(self, mock_ec):
        mock_ec.read_email.return_value = {"error": "Message 999 not found"}

        result = read_email(uid=999)

        self.assertIn("error", result)


class TestSendEmail(unittest.TestCase):
    """send_email tool should delegate to email_client.send_email."""

    @patch("email_mcp_server.email_client")
    def test_send_basic(self, mock_ec):
        mock_ec.send_email.return_value = {"status": "sent", "to": "alice@example.com", "cc": None, "subject": "Hi"}

        result = send_email(to="alice@example.com", subject="Hi", body="Hello!")

        mock_ec.send_email.assert_called_once_with(
            "alice@example.com", "Hi", "Hello!",
            reply_to_id=None, cc=None,
        )
        self.assertEqual(result["status"], "sent")

    @patch("email_mcp_server.email_client")
    def test_send_with_cc_and_reply(self, mock_ec):
        mock_ec.send_email.return_value = {"status": "sent", "to": "alice@example.com", "cc": "robin@gmail.com", "subject": "Re: Hi"}

        result = send_email(
            to="alice@example.com",
            subject="Re: Hi",
            body="Thanks!",
            cc="robin@gmail.com",
            reply_to="<orig@example.com>",
        )

        mock_ec.send_email.assert_called_once_with(
            "alice@example.com", "Re: Hi", "Thanks!",
            reply_to_id="<orig@example.com>", cc="robin@gmail.com",
        )
        self.assertEqual(result["cc"], "robin@gmail.com")

    @patch("email_mcp_server.email_client")
    def test_send_error(self, mock_ec):
        mock_ec.send_email.return_value = {"status": "error", "error": "Authentication failed"}

        result = send_email(to="bad@example.com", subject="Test", body="Test")

        self.assertEqual(result["status"], "error")
        self.assertIn("error", result)


class TestDownloadAttachments(unittest.TestCase):
    """download_attachments tool should delegate to email_client.download_attachments."""

    @patch("email_mcp_server.email_client")
    def test_downloads(self, mock_ec):
        mock_ec.download_attachments.return_value = {
            "status": "ok",
            "uid": 42,
            "attachment_count": 2,
            "total_size_human": "3.0 KB",
            "saved_to": "/home/lyra/mail/attachments/42",
            "files": [
                {"filename": "a.pdf", "path": "/home/lyra/mail/attachments/42/a.pdf", "content_type": "application/pdf", "size": 1000, "size_human": "1000 B"},
                {"filename": "b.csv", "path": "/home/lyra/mail/attachments/42/b.csv", "content_type": "text/csv", "size": 2072, "size_human": "2.0 KB"},
            ],
        }

        result = download_attachments(uid=42)

        mock_ec.download_attachments.assert_called_once_with(42)
        self.assertEqual(result["attachment_count"], 2)
        self.assertEqual(result["files"][0]["filename"], "a.pdf")

    @patch("email_mcp_server.email_client")
    def test_not_found(self, mock_ec):
        mock_ec.download_attachments.return_value = {"error": "Message 999 not found"}

        result = download_attachments(uid=999)

        self.assertIn("error", result)


class TestMarkAsRead(unittest.TestCase):
    """mark_as_read tool should delegate to email_client.mark_as_read."""

    @patch("email_mcp_server.email_client")
    def test_marks_read(self, mock_ec):
        mock_ec.mark_as_read.return_value = {"status": "ok", "uid": 42}

        result = mark_as_read(uid=42)

        mock_ec.mark_as_read.assert_called_once_with(42)
        self.assertEqual(result["status"], "ok")

    @patch("email_mcp_server.email_client")
    def test_error(self, mock_ec):
        mock_ec.mark_as_read.return_value = {"error": "Connection refused"}

        result = mark_as_read(uid=42)

        self.assertIn("error", result)


if __name__ == "__main__":
    unittest.main()

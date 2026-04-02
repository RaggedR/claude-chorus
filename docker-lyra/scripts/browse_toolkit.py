#!/usr/bin/env python3
"""CodeAct browsing toolkit for Lyra's browse agents.

Provides a Browser context manager that wraps Playwright's sync API
with rate limiting, cookie loading, and convenience methods.

Usage:
    import sys; sys.path.insert(0, '/home/lyra/scripts')
    from browse_toolkit import Browser

    with Browser() as b:
        b.goto('https://medium.com/search?q=category+theory')
        links = b.get_links('article a')
        for link in links[:5]:
            b.goto(link['href'])
            print(b.get_text()[:500])
"""

import json
import os
import time
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright, Browser as PwBrowser, BrowserContext, Page

# Default paths
DEFAULT_STORAGE_STATE = "/home/lyra/.playwright-profile/storage-state.json"
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)


class Browser:
    """Context manager for Playwright browsing with rate limiting and cookie support.

    Each instance gets its own BrowserContext (isolated cookies, independent of
    other instances). Safe to run multiple Browser instances in parallel.

    Args:
        storage_state: Path to storage state JSON (cookies). Defaults to the
            export from Playwright MCP's profile. Pass None to skip cookie loading.
        rate_limit: Minimum seconds between navigations. Default 2.0.
        headless: Run headless (True) or headed on Xvfb (False). Default False.
        timeout: Default navigation timeout in milliseconds. Default 30000.
    """

    def __init__(
        self,
        storage_state: str | None = DEFAULT_STORAGE_STATE,
        rate_limit: float = 2.0,
        headless: bool = False,
        timeout: int = 30000,
    ):
        self._storage_state = storage_state
        self._rate_limit = rate_limit
        self._headless = headless
        self._timeout = timeout
        self._last_nav = 0.0
        self._playwright = None
        self._browser: PwBrowser | None = None

        # Public attributes — set in __enter__
        self.context: BrowserContext | None = None
        self.page: Page | None = None

    def __enter__(self):
        self._playwright = sync_playwright().start()

        # Launch args — same as Lyra's Playwright MCP config
        launch_args = [
            "--no-sandbox",
            "--disable-blink-features=AutomationControlled",
        ]

        self._browser = self._playwright.chromium.launch(
            headless=self._headless,
            args=launch_args,
        )

        # Resolve storage state — only load if file exists
        storage = None
        if self._storage_state and Path(self._storage_state).is_file():
            storage = self._storage_state

        self.context = self._browser.new_context(
            storage_state=storage,
            user_agent=DEFAULT_USER_AGENT,
            viewport={"width": 1280, "height": 720},
        )
        self.context.set_default_timeout(self._timeout)

        self.page = self.context.new_page()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.context:
            try:
                self.context.close()
            except Exception:
                pass
        if self._browser:
            try:
                self._browser.close()
            except Exception:
                pass
        if self._playwright:
            try:
                self._playwright.stop()
            except Exception:
                pass
        return False  # Don't suppress exceptions

    def _rate_limit_wait(self):
        """Enforce minimum delay between navigations."""
        elapsed = time.time() - self._last_nav
        if elapsed < self._rate_limit:
            time.sleep(self._rate_limit - elapsed)
        self._last_nav = time.time()

    def goto(self, url: str, wait_until: str = "domcontentloaded") -> None:
        """Navigate to URL with rate limiting.

        Args:
            url: The URL to navigate to.
            wait_until: When to consider navigation done.
                Options: 'load', 'domcontentloaded', 'networkidle', 'commit'.
        """
        self._rate_limit_wait()
        self.page.goto(url, wait_until=wait_until)

    def get_text(self) -> str:
        """Return visible text content of the current page."""
        return self.page.inner_text("body")

    def get_links(self, selector: str = "a") -> list[dict]:
        """Return list of {text, href} for links matching selector.

        Args:
            selector: CSS selector for link elements. Default 'a'.
        """
        links = self.page.eval_on_selector_all(
            selector,
            """elements => elements.map(el => ({
                text: (el.innerText || '').trim(),
                href: el.href || ''
            })).filter(l => l.href)""",
        )
        return links

    def wait_and_get_text(self, selector: str, timeout: int | None = None) -> str:
        """Wait for an element to appear, then return its text content.

        Args:
            selector: CSS selector to wait for.
            timeout: Override default timeout (ms).
        """
        kwargs = {}
        if timeout is not None:
            kwargs["timeout"] = timeout
        el = self.page.wait_for_selector(selector, **kwargs)
        return el.inner_text() if el else ""

    def screenshot(self, path: str = "/tmp/screenshot.png") -> str:
        """Save a screenshot of the current page.

        Args:
            path: File path to save the screenshot.

        Returns:
            The path where the screenshot was saved.
        """
        self.page.screenshot(path=path)
        return path

    def new_page(self) -> Page:
        """Open a new tab sharing the same cookies/context.

        Returns:
            The new Page object.
        """
        return self.context.new_page()

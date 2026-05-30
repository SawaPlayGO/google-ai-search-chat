from __future__ import annotations

from playwright.sync_api import BrowserContext, Browser, Playwright, sync_playwright

_playwright: Playwright | None = None
_browser: Browser | None = None
_context: BrowserContext | None = None
_persistent: bool = False  # флаг режима


def get_browser(
    headless: bool = True,
    user_data_dir: str | None = None,
) -> BrowserContext:
    global _playwright, _browser, _context, _persistent

    if _context is None:
        _playwright = sync_playwright().start()

        common_args = [
            "--disable-blink-features=AutomationControlled",
            "--disable-dev-shm-usage",
            "--no-sandbox",
            "--disable-gpu",
            "--window-size=1920,1080",
            "--start-maximized",
        ]
        common_context_kwargs = dict(
            viewport={"width": 1920, "height": 1080},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/136.0.0.0 Safari/537.36"
            ),
        )

        if user_data_dir:
            # Режим с сохранением профиля
            _persistent = True
            _context = _playwright.chromium.launch_persistent_context(
                user_data_dir=user_data_dir,
                headless=headless,
                channel="chrome",
                args=common_args,
                ignore_default_args=["--enable-automation"],
                **common_context_kwargs,
            )
        else:
            # Режим без сохранения
            _persistent = False
            _browser = _playwright.chromium.launch(
                headless=headless,
                channel="chrome",
                args=common_args,
                ignore_default_args=["--enable-automation"],
            )
            _context = _browser.new_context(**common_context_kwargs)

    return _context


def close_browser() -> None:
    global _playwright, _browser, _context, _persistent

    if _context:
        try:
            _context.close()
        except Exception:
            pass
        _context = None

    # В persistent-режиме браузер закрывается вместе с контекстом,
    # отдельного _browser нет
    if not _persistent and _browser:
        try:
            _browser.close()
        except Exception:
            pass
    _browser = None

    if _playwright:
        try:
            _playwright.stop()
        except Exception:
            pass
        _playwright = None

    _persistent = False
from playwright.sync_api import BrowserContext, Browser, Playwright, sync_playwright

_playwright: Playwright | None = None
_browser: Browser | None = None
_context: BrowserContext | None = None


def get_browser(headless: bool = True) -> BrowserContext:
    global _playwright, _browser, _context

    if _context is None:
        _playwright = sync_playwright().start()
        _browser = _playwright.chromium.launch(
            headless=headless,
            channel="chrome",
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-dev-shm-usage",
                "--no-sandbox",
                "--disable-gpu",
                "--window-size=1920,1080",
                "--start-maximized",
            ],
            ignore_default_args=["--enable-automation"],
        )
        _context = _browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/136.0.0.0 Safari/537.36"
            ),
        )

    return _context


def close_browser() -> None:
    global _playwright, _browser, _context

    if _context:
        try:
            _context.close()
        except Exception:
            pass
        _context = None

    if _browser:
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
from playwright.sync_api import Page

GOOGLE_AI_URL = (
    "https://www.google.com/search?"
    "sca_esv=59e8ea9c916b862d&udm=50&atvm=2"
)

_SKIP_SELECTORS = ".HvurC, .Fsg96, .UrecDd, .FYF80, .DBd2Wb, .CxFouc"
_EXTRACT_JS = f"""el => {{
    const clone = el.cloneNode(true);
    clone.querySelectorAll('{_SKIP_SELECTORS}').forEach(n => n.remove());
    return clone.innerText.trim();
}}"""


class ChatGoogleAI:
    def __init__(self, page: Page):
        self.page = page

    def create(self) -> "ChatGoogleAI":
        self.page.goto(GOOGLE_AI_URL)
        self.check_agree()
        self.page.click("textarea.ITIRGe")
        self.page.keyboard.type("Start chat")
        self.page.click("[data-xid='input-plate-send-button']")
        self.page.wait_for_timeout(2000)
        return self

    def check_agree(self) -> None:
        btn = self.page.locator("#L2AGLb")
        if btn.count() > 0:
            btn.first.click()

    def send_message(self, message: str, photo: bytes | None = None) -> str:
        self.page.bring_to_front()
        self.check_agree()
        self.page.locator("textarea.ITIRGe").last.click()
        self.page.locator("textarea.ITIRGe").last.fill(message)

        if photo is not None:
            self.page.locator("button.hhGtFb").last.click()
            self.page.locator("input[accept*='image/jpeg']").last.set_input_files(
                files=[{"name": "image.jpg", "mimeType": "image/jpeg", "buffer": photo}]
            )

        self.page.wait_for_timeout(1000)
        self.page.locator("[data-xid='input-plate-send-button']").last.click()

        prev = ""
        stable_count = 0
        for _ in range(80):
            self.page.wait_for_timeout(800)
            blocks = self.page.locator("[data-subtree='aimc']").all()
            if not blocks:
                continue

            block = blocks[-1]
            main_col = block.locator("[data-container-id='main-col']")
            target = main_col if main_col.count() > 0 else block
            current = target.evaluate(_EXTRACT_JS)

            if current and current == prev:
                stable_count += 1
                if stable_count >= 3:
                    return current
            else:
                stable_count = 0
                prev = current

        return prev

    def close(self) -> None:
        self.page.close()
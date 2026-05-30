from .browser import get_browser, close_browser
from .chat import ChatGoogleAI


class GoogleAISession:
    """
    Manages multiple independent chats, each in its own tab.

    Usage:
        chat = session.new_chat()
        reply = chat.send_message("Hello")
        chat.close()
        session.close()
    """

    def __init__(
        self,
        headless: bool = True,
        user_data_dir: str | None = None,
    ):
        self._browser = get_browser(headless=headless, user_data_dir=user_data_dir)
        self._chats: list[ChatGoogleAI] = []

    def new_chat(self) -> ChatGoogleAI:
        page = self._browser.new_page()
        chat = ChatGoogleAI(page=page)
        chat.create()
        self._chats.append(chat)
        return chat

    def close_all_chats(self) -> None:
        for chat in self._chats:
            try:
                chat.close()
            except Exception:
                pass
        self._chats.clear()

    def close(self) -> None:
        self.close_all_chats()
        close_browser()
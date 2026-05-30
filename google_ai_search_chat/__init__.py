from __future__ import annotations

"""
Google AI Search - Unofficial Python client for Google AI Search.

A Python library for interacting with Google AI Search using browser automation
via Playwright, supporting multiple independent chat sessions and image uploads.

Example:
    Basic usage:
    >>> from google_ai_search_chat import GoogleAISession
    >>> session = GoogleAISession(user_data_dir="C:/chrome-profile")
    >>> chat = session.new_chat()
    >>> response = chat.send_message("Hello!")
    >>> print(response)
    >>> session.close()

    Multiple chats:
    >>> chat1 = session.new_chat()
    >>> chat2 = session.new_chat()
    >>> resp1 = chat1.send_message("First chat")
    >>> resp2 = chat2.send_message("Second chat")

    With images:
    >>> with open("image.jpg", "rb") as f:
    ...     response = chat.send_message("What's in this?", f.read())
"""

__version__ = "0.1.8"
__author__ = "Google AI Search Contributors"
__license__ = "MIT"

from .session import GoogleAISession
from .chat import ChatGoogleAI
from .browser import get_browser, close_browser

__all__ = [
    "GoogleAISession",
    "ChatGoogleAI",
    "get_browser",
    "close_browser",
    "__version__",
]
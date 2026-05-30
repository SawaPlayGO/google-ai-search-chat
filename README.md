# Google AI Search - Python Client

[![PyPI version](https://img.shields.io/pypi/v/google-ai-search-chat)](https://pypi.org/project/google-ai-search-chat/)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

https://github.com/user-attachments/assets/48528c71-e68c-4291-96bc-4dd929efa872

Unofficial Python client for [Google AI Search](https://www.google.com/search?sca_esv=59e8ea9c916b862d&udm=50) with support for multiple independent chat sessions using browser automation.

## Features

✨ **Key Features:**
- 🤖 Interact with Google AI Search using Python
- 💬 Create multiple independent chat sessions
- 🖼️ Send images along with text messages
- 🌐 Browser-based automation with Playwright

## Installation

### From PyPI (Recommended)

```bash
pip install google-ai-search-chat
```

### From GitHub (Latest Development Version)

```bash
pip install git+https://github.com/yourusername/google-ai-search-chat.git
```

### From Source

```bash
git clone https://github.com/yourusername/google-ai-search-chat.git
cd google-ai-search-chat
pip install -e .
```

### Browser Driver Setup

The library uses Playwright for browser automation. Install required browsers:

```bash
playwright install chromium
```

## Quick Start

### Basic Usage

```python
from google_ai_search_chat import GoogleAISession

# Create a session
session = GoogleAISession(user_data_dir=r"C:\chrome-profile", headless=False)

# Create a new chat
chat = session.new_chat()

# Send a message and get response
response = chat.send_message("Hello, what's the weather like?")
print(response)

# Create another independent chat in a new tab
chat2 = session.new_chat()
response2 = chat2.send_message("What is Python?")
print(response2)

# Cleanup
session.close()
```

### Sending Images

```python
from google_ai_search_chat import GoogleAISession

session = GoogleAISession(user_data_dir=r"C:\chrome-profile")
chat = session.new_chat()

# Send image with message
with open("image.jpg", "rb") as f:
    response = chat.send_message("What's in this image?", f.read())
    print(response)

session.close()
```

### Headless Mode

```python
# Headless mode (no browser window shown)
session = GoogleAISession(user_data_dir=r"C:\chrome-profile", headless=True)
chat = session.new_chat()
response = chat.send_message("Test message")
session.close()
```

## API Reference

### GoogleAISession

Main class for managing browser sessions and multiple chats.

```python
GoogleAISession(user_data_dir: str = r"C:\chrome-profile", headless: bool = True)
```

**Parameters:**
- `user_data_dir` (str): Path to Chrome profile directory for cookie persistence
- `headless` (bool): Run browser in headless mode (default: True)

**Methods:**
- `new_chat() -> ChatGoogleAI`: Create a new independent chat session
- `close_all_chats() -> None`: Close all open chats
- `close() -> None`: Close all chats and the browser session

### ChatGoogleAI

Represents a single chat session.

**Methods:**
- `send_message(message: str, photo: bytes | None = None) -> str`: Send a message (with optional image)
- `close() -> None`: Close the chat

## Requirements

- Python 3.12+
- Chromium browser (installed via Playwright)
- At least 500MB disk space for browser installation

# 🤖 Automated Reply AI Chatbot

An AI auto-responder bot built with Python, PyAutoGUI, and the Cohere API. This bot reads chat messages from WhatsApp Web, generates smart replies using AI, and sends them automatically — all while giving you control through a GUI STOP button to terminate the program.

---

## 🚀 Features

- 🔄 Automatically reads chat messages through screen automation
- 🤖 Generates replies using Cohere AI
- 🧠 Responds only when the last message is from the target or opposite person
- 🖱️ Uses PyAutoGUI for selecting, copying, and pasting text messages
- 🛑 Includes a STOP button GUI to safely terminate the bot
- 🔒 Securely stores your API key in a `.env` file (never exposed)

---

# 🧠 How It Works

This explains how the **Automated Reply AI Chatbot** automates replies on WhatsApp using desktop automation and Cohere AI.

---

## 🔧 Step-by-Step Flow

### 1. Bot Initialization
- Loads environment variables (API key from `.env`)
- Launches the GUI "STOP BOT" button in a separate thread
- Enters an infinite while loop that checks for messages

---

### 2. WhatsApp Message Capture
- Moves the mouse to the bottom of the screen to reveal the hidden taskbar
- Clicks the Edge browser icon (or any browser) to open the WhatsApp Web
- Performs a drag operation across the chat area to select recent messages
- Copies selected text to clipboard

---

### 3. Message Analysis
- Reads clipboard content using `pyperclip`
- Checks if the **last message is from the target sender**
- Skips if the last message is from the user themselves

---

### 4. AI-Powered Reply
- If the message is from the target sender:
  - Sends the chat text to Cohere's API via `ClientV2().chat(...)`
  - Gets a conversational reply from the AI
  - Pastes it into the WhatsApp Web chatbox
  - Presses `Enter` to send

---

### 5. Stop Button GUI
- A red STOP button remains visible in a small window on the screen
- Clicking it triggers a `threading.Event()` signal
- The main bot loop constantly checks for this signal and **exits cleanly** when it's clicked

---

## 📝 Notes

- All cursor positions (like click or drag coordinates) may need adjustment for your screen resolution.
- This method simulates user actions on screen, so don’t use your mouse/keyboard while it runs.
- The AI behavior can be changed by modifying the system prompt in the code.

---

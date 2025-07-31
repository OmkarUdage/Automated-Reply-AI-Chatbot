# 🤖 Automated Reply AI Chatbot

An AI auto-responder bot built with Python, PyAutoGUI, and the Cohere API. This bot reads chat messages from WhatsApp Web, generates smart replies using AI, and sends them automatically — all while giving you control through a GUI STOP button to terminate the program.

---

## 🚀 Features

- 🔄 Automatically reads chat messages via screen automation
- 🤖 Generates intelligent replies using Cohere AI
- 🧠 Responds only when the last message is from the target person
- 🖱️ Uses PyAutoGUI for selecting, copying, and pasting messages
- 🛑 Includes a STOP button GUI to safely terminate the bot
- 🔒 Securely stores your API key in a `.env` file (never exposed)

---

## 📦 Requirements

Make sure you have Python 3.7+ and install the dependencies:

```bash
pip install -r requirements.txt

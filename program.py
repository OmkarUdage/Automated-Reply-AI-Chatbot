import pyautogui         # For GUI automation
import pyperclip         # For copy/paste clipboard
import time              # For bot actions
import cohere            # AI assistant
import keyboard          # For detecting keyboard input (for 'esc')
import tkinter as tk     # To build the Stop button
import threading         # To allow the GUI and bot to run in parallel
from dotenv import load_dotenv    # load secret data from .env
import os

load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2(COHERE_API_KEY)

# Threading event to signal when to stop the bot
stop_event = threading.Event()

# Function to display a STOP button in a GUI
def show_stop_button():
    root = tk.Tk()
    root.title("Stop Bot")
    root.geometry("200x100")
    # Create the button and link it to stop_event
    stop_button = tk.Button(root, text="STOP BOT", font=('Arial', 14), fg="white", bg="red", command=stop_event.set)
    stop_button.pack(expand=True)

    root.mainloop()


# Start the GUI in a separate thread so it doesn't block the bot
gui_thread = threading.Thread(target=show_stop_button)
gui_thread.start()


# Function to check if the last message is from the other person, which prevents the bot from replying to its own messages
def is_last_message_from_sender(chat_text, sender_name = "---"):
    # Get only the last message segment based on timestamp format (e.g. /2025])
    lines = chat_text.strip().split("/2025] ")[-1]
    if sender_name in lines:
        return True
    return False
    
# Default pause between pyautogui action
pyautogui.PAUSE = 0.5

# Move to bottom edge of screen to show appear taskbar
pyautogui.moveTo(900, 1078)
time.sleep(1)


# Main boot loop
while not stop_event.is_set():
    if keyboard.is_pressed('esc'):
        print("ESC pressed. Exiting loop.")
        break

    # Click on chrome/edge/any browser icon on taskbar
    pyautogui.click(876, 1044)
    print("Opened chat application")
    time.sleep(3)    

    # Select text by dragging
    pyautogui.moveTo(682, 252)
    pyautogui.mouseDown()
    pyautogui.moveTo(1872, 999, duration=0.5)
    pyautogui.mouseUp()
    print("Text selected.")

    # Copy to clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    # Deselect text 
    pyautogui.moveTo(1856, 936)
    pyautogui.click()
    time.sleep(1)

    # Get clipboard content
    copied_text = pyperclip.paste()
    print("Copied Text:\n", copied_text)

    if is_last_message_from_sender(copied_text):
        print("Last message is from the other person. Responding...")

        # Generating a chat reply using Cohere AI API
        response = co.chat(
            model="command-a-03-2025", 
            messages=[
                {"role": "system", "content": "You are Omkar, a skilled programmer from India who speaks fluent English,"
                        "and understands Hindi and Marathi. Reply casually and naturally, like a WhatsApp chat."
                        "Avoid formal or robotic tone. Your reply should be short and friendly."
                        "Do not include timestamps or sender name."},
                {"role": "user", "content": copied_text}
            ]
        )

        myResponse = response.message.content[0].text
        print(myResponse)

        # Click on chatbox location
        pyautogui.click(1320, 1008) 
        time.sleep(0.5)

        # Copy text from clipboard
        pyperclip.copy(myResponse)

        # Paste the response into chatbox
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)

        # Press Enter to send
        pyautogui.press('enter')

    else:
        print("Last message is NOT from the sender. Skipping reply.\n")

    # Waiting before checking again to avoid infinite while loop and overloading
    time.sleep(25)

print("Bot stopped by user.")
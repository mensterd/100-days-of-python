#!/usr/bin/env python3
"""
Telegram Message Sender
"""
import requests  # Import the requests library to send HTTP requests 3
# Import secrets.py that holds api key
import secrets

# How the Telegram bot works
# https://docs.radist.online/docs/our-products/radist-web/connections/telegram-bot/instructions-for-creating-and-configuring-a-bot-in-botfather

# Get API-token and Chat_ID from secrets file. Put your Token and Chat-ID here.
BOT_TOKEN = secrets.TELEGRAM_BOT_TOKEN
CHAT_ID = secrets.TELEGRAM_CHAT_ID


class TelegramSender:
    def __init__(self, bot_token=BOT_TOKEN, chat_id=CHAT_ID):
        self.chat_id = chat_id
        self.bot_token = bot_token
        self.base_url = url = f"https://api.telegram.org/bot{self.bot_token}/"


    def send_message(self, message):
        url = self.base_url + "sendMessage"

        # Prepare the payload with chat id and text
        payload = {
            "chat_id": self.chat_id,
            "text": message
        }
        # Make the POST request to Telegram's API to send the message
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
        except Exception as err:
            print(f"Oops! {err}")
            return False
        else:
            # Check the response status code to see if the message was sent successfully
            if response.status_code == 200:
                print(f"Telegram message send to {self.chat_id}!")
                return True
            else:
                print("Failed to send message. Response:", response.text)
                return False



if __name__ == "__main__":
    m = TelegramSender()
    m.send_message("Hello Spencer!")




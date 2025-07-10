
""" 
notifier.py
Handles sending notification to users via Telegram by interfacing with the Telegram Bot API.

Brendan Dileo - July 2025
"""

import requests
import smtplib
from client import config
from email.mime.text import MIMEText

# Sends a message to a telegram chat
def send_telegram_message(message: str):
    
    # Construct url and define payload containing target chat and message
    url = config.telegram_send_message_url
    payload = { "chat_id": config.telegram_chat_id, "text": message }
    
    # Sends the POST request to the Telegram API with the message payload
    response = requests.post(url, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Message sent successfully!")
        return True
    else:
        print(f"Failed to send message: {response.status_code} - {response.text}")
        return False
    
# Sends an email notification
def send_email_notification(subject: str, message: str):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = config.email_from
    msg['To'] = config.email_to

""" 
notifier.py
Handles sending notification to users via Telegram by interfacing with the Telegram Bot API.

Brendan Dileo - July 2025
"""

import requests
from client import config

# Sends a message to a telegram chat
def send_telegram_message(message: str):
    url = config.telegram_send_message_url
    
    response = requests.post(url)
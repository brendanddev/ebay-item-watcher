
# config.py
# Brendan Dileo - July 2025

import os
from dotenv import load_dotenv

# Loads the env variables into the current environment
load_dotenv()

# Item watcher configuration
ebay_environment = os.getenv("EBAY_ENV")
ebay_app_id = os.getenv("EBAY_APP_ID")
ebay_dev_id = os.getenv("EBAY_DEV_ID")
ebay_cert_id = os.getenv("EBAY_CERT_ID")

# Notifier configuration
telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

if __name__ == "__main__":
    print("TELEGRAM_BOT_TOKEN:", telegram_bot_token)
    print("TELEGRAM_CHAT_ID:", telegram_chat_id)
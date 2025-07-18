
"""
config.py
Loads environment variables and centralizes configuration settings for the app.

Brendan Dileo - July 2025
"""

import os
from dotenv import load_dotenv

# Loads the env variables into the current environment
load_dotenv()

# Basic configuration
postal_prefix = os.getenv("POSTAL")
region = os.getenv("REGION")
country = os.getenv("COUNTRY")

# Item watcher configuration
ebay_environment = os.getenv("EBAY_ENV")
ebay_app_id = os.getenv("EBAY_APP_ID")
ebay_dev_id = os.getenv("EBAY_DEV_ID")
ebay_cert_id = os.getenv("EBAY_CERT_ID")

# Item watcher production configuration
ebay_app_id_prod = os.getenv("EBAY_APP_ID_PROD")
ebay_dev_id_prod = os.getenv("EBAY_DEV_ID_PROD")
ebay_cert_id_prod = os.getenv("EBAY_CERT_ID_PROD")

# Notifier configuration
telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

telegram_base_url = f"https://api.telegram.org/bot{telegram_bot_token}/"
telegram_send_message_url = telegram_base_url + "sendMessage"

# Email configuration
email_smtp_server = os.getenv("EMAIL_SMTP_SERVER")
email_smtp_port = int(os.getenv("EMAIL_SMTP_PORT", 587))
email_username = os.getenv("EMAIL_USERNAME")
email_password = os.getenv("EMAIL_PASSWORD")
email_from = email_username
email_to = os.getenv("EMAIL_RECIPIENT", email_username)
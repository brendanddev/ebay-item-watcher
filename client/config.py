
# config.py
# Brendan Dileo - July 2025

import os
from dotenv import load_dotenv

# Loads the env variables into the current environment
load_dotenv()

ebay_environment = os.getenv("EBAY_ENV")
ebay_app_id = os.getenv("EBAY_APP_ID")
ebay_dev_id = os.getenv("EBAY_DEV_ID")
ebay_cert_id = os.getenv("EBAY_CERT_ID")

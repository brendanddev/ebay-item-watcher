
"""
auth.py
Authenticates the app and retrieves the necessary app access token using the client credentials OAuth2 
flow. This token is used to authroize app level access to ebays api's

Brendan Dileo - July 2025
"""

import base64
import requests
from client import config

# Retrieves the access token for the app
def get_app_access_token():
    
    # Select environment
    is_prod = config.ebay_environment == "production"
    
    # Use correct credentials based on environment
    client_id = config.ebay_app_id_prod if is_prod else config.ebay_app_id
    client_secret = config.ebay_cert_id_prod if is_prod else config.ebay_cert_id
        
    auth_string = f"{client_id}:{client_secret}"
    encoded_auth = base64.b64encode(auth_string.encode()).decode()
    
    # Request headers including auth
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_auth}"
    }
    
    # Set request body with form request data
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }

    # Choose token url based on environment
    token_url = "https://api.ebay.com/identity/v1/oauth2/token" if is_prod else \
                "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
                
    # Makes the POST request passing necessary headers and data
    response = requests.post(token_url, headers=headers, data=data)
    
    # Checks if the request was successful and returns the access token if it is
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("Failed to get token:", response.status_code, response.json())
        return None

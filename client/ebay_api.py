
""" 
ebay_api.py
Provides a simple wrapper around the ebay browse api to search for items based on a query

Brendan Dileo - July 2025
"""

import requests
from client import auth

# Searches for an item on ebay using the buy API
def search(query):
    
    # Get the access token and validate it
    token = auth.get_app_access_token()
    if not token:
        print("Failed to retrieve access token.")
        return
    
    # Define api endpoint, headers and params for search request
    url = "https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search"
    headers = { "Authorization": f"Bearer {token}" }
    params = { "q": query }
    
    # Make GET request and store response
    response = requests.get(url, headers=headers, params=params)
    
    # Check if the request was successful
    # If successful, return the JSON response, otherwise print error
    if response.status_code == 200:
        print("Search successful!")
        return response.json()
    else:
        print("Search failed:", response.status_code, response.text)
        return None


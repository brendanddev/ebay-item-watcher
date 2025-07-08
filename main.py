
""" 
main.py
Main entry point to the app

Brendan Dileo - July 2025
"""

from client.auth import get_app_access_token
from client.ebay_api import build_search_params, search
from client.notifier import send_telegram_message


if __name__ == "__main__":
    
    # Sends a message to the user via the Telegram bot
    send_telegram_message("ebay Item Watcher started successfully!")
    
    # Get and print the app access token
    token = get_app_access_token()
    print("Access Token:", token)
    
    # Build search params with filters
    params = build_search_params(
        keyword="iPhone",
        limit=10
    )
    
    # Perform the search
    results = search(params)
    if results:
        print("Search Results:", results)
    else:
        print("No results found or search failed.")

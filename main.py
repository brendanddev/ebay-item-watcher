
""" 
main.py
Main entry point to the app

Brendan Dileo - July 2025
"""

from client.auth import get_app_access_token
from client.ebay_api import build_search_params, search
from client.notifier import send_telegram_message
from client.formatter import format_search_results


if __name__ == "__main__":
    
    # Sends a message to the user via the Telegram bot
    send_telegram_message("ebay Item Watcher started successfully!")
    
    # Get and print the app access token
    token = get_app_access_token()
    print("Access Token:", token)
    
    # Build search params with filters
    params = build_search_params(
        keyword="Marvel Super Heroes Secret Wars",
        price_min=5,
        price_max=100,
        price_currency="CAD",
        pickup_postal_code="L6L5W2",
        pickup_radius=1,
        item_location_region="ON",
        item_location_country="CA",
        canada_only=True,
        limit=15
    )

    # Perform the search
    results = search(params)
    if results:
        # print("Search Results:", results)
        formatted_results = format_search_results(results)
        print("Formatted Results:\n", formatted_results)
        # send_telegram_message(formatted_results)
    else:
        print("No results found or search failed.")

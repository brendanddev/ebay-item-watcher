
""" 
commands.py
Handles the core command logic for the ebay item watcher cli app.

Brendan Dileo - July 2025
"""

from client.ebay_api import build_search_params, search
from client.formatter import format_search_results
from client.notifier import send_telegram_message, send_email_notification
from client.config import postal_prefix, region, country
from utils.logger import Logger

logger = Logger().get_logger()

# Performs the eBay search based on user input
def perform_search(notification_choice="1"):
    logger.info("Prompting user for search keyword...")
    keyword = input("Enter search keyword: ")
    logger.debug(f"User entered keyword: {keyword}")

    logger.info("Prompting user for minimum price...")
    min_price = input("Enter minimum price (or leave blank): ")
    logger.debug(f"User entered min price: {min_price or 'None'}")

    logger.info("Prompting user for maximum price...")
    max_price = input("Enter maximum price (or leave blank): ")
    logger.debug(f"User entered max price: {max_price or 'None'}")
    
    # Build search params with filters
    params = build_search_params(
        keyword=keyword,
        price_min=min_price,
        price_max=max_price,
        price_currency="CAD",
        pickup_postal_code=postal_prefix,
        pickup_radius=5,
        item_location_region=region,
        item_location_country=country,
        limit=15
    )
    
    # Perform the search
    results = search(params)
    if results:
        
        if notification_choice == "1":
            logger.info("Sending results via Telegram bot...")
            send_telegram_message("Search completed successfully!")
        elif notification_choice == "2":
            logger.info("Sending results via Email...")
            subject = "eBay Item Watcher Search Results"
            message = format_search_results(results)
            send_email_notification(subject, message)
        elif notification_choice == "3":
            logger.info("Sending results via both Telegram bot and Email...")
            send_telegram_message("Search completed successfully!")
            subject = "eBay Item Watcher Search Results"
            message = format_search_results(results)
            send_email_notification(subject, message)
        else:
            logger.info("Displaying results in console only...")

        # Format search results
        formatted_results = format_search_results(results)
        print("Formatted Results:\n", formatted_results)
    else:
        print("No results found or search failed.")
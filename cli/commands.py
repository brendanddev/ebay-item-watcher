
""" 
commands.py

Brendan Dileo - July 2025
"""

from client.ebay_api import build_search_params, search
from client.formatter import format_search_results
from client.notifier import send_telegram_message
from client.config import postal_prefix, region, country
from utils.logger import Logger

logger = Logger().get_logger()

# Performs the eBay search based on user input
def perform_search():
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
        
        # Format search results
        formatted_results = format_search_results(results)
        print("Formatted Results:\n", formatted_results)
        
        # Sends a message to the user via the Telegram bot
        send_telegram_message(formatted_results)
    else:
        print("No results found or search failed.")
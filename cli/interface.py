
""" 
interface.py

Brendan Dileo - July 2025
"""

from cli.commands import perform_search
from utils.logger import Logger

logger = Logger().get_logger()

def run_cli():
    print("Welcome to eBay Item Watcher!")
    print("Available commands:")
    print("1. Search")

    logger.info("Prompting user for menu choice")
    choice = input("Enter a command number: ").strip()
    logger.debug(f"User selected menu option: {choice}")

    if choice == "1":
        logger.info("Running 'search' via menu selection")
        perform_search()
    else:
        logger.warning("Invalid command entered.")
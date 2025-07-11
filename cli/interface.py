
""" 
interface.py

Brendan Dileo - July 2025
"""

import argparse
from cli.commands import perform_search
from cli.ui import show_main_menu, prompt_for_notification, loading_spinner
from utils.logger import Logger

logger = Logger().get_logger()


def run_cli():
    # Creates an instance of ArgumentParser object to handle cli args
    parser = argparse.ArgumentParser(description="eBay Item Watcher CLI")
    
    # Accepts a cli argument for the command to run
    parser.add_argument(
        "command",
        nargs="?",
        choices=["search"],
        help="Choose a command (or leave blank for menu)",
    )
    
    # Parse cli args into structured object
    logger.info("Parsing command line arguments...")
    args = parser.parse_args()
    logger.info("Parsed command line arguments...")
    
    # If a user has provided a command
    if args.command:
        logger.info(f"Running command: {args.command}")
        if args.command == "search":
            perform_search()
    else:
        logger.info("Prompting user for menu choice")
        
        # cli menu if no args provided
        choice = show_main_menu()

        if choice == "Search items":
            notification_choice = prompt_for_notification()
            logger.info("Running 'search' via menu selection")
            perform_search(notification_choice=notification_choice)
            loading_spinner("Searching eBay...")
        elif choice == "Exit":
            print("Goodbye!")
            exit()
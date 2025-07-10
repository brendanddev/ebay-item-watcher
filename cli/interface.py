
""" 
interface.py

Brendan Dileo - July 2025
"""

import argparse
from cli.commands import perform_search
from utils.logger import Logger

logger = Logger().get_logger()

def run_cli():
    parser = argparse.ArgumentParser(description="eBay Item Watcher CLI")
    parser.add_argument(
        "command",
        nargs="?",
        choices=["search"],
        help="Choose a command (or leave blank for menu)",
    )
    args = parser.parse_args()

    if args.command:
        logger.info(f"Running command: {args.command}")
        if args.command == "search":
            perform_search()
    else:
        
        # App based menu if no cli args
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
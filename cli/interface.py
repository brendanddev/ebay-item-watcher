
""" 
interface.py

Brendan Dileo - July 2025
"""

import argparse
from time import sleep
from cli.commands import perform_search
from utils.logger import Logger
from rich.console import Console
from rich.spinner import Spinner
from InquirerPy import inquirer

logger = Logger().get_logger()
console = Console()
    

# Prompts the user for notification method to use
def prompt_for_notification():
    print("Choose notification method(s):")
    print("1. Telegram Bot only")
    print("2. Email only")
    print("3. Both Telegram Bot and Email")
    print("4. None (just display results)")
    choice = input("Enter your choice (1-4): ").strip()
    return choice 

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
        
        # App based menu if no cli args
        print("Welcome to eBay Item Watcher!")
        print("Available commands:")
        print("1. Search")

        logger.info("Prompting user for menu choice")
        choice = input("Enter a command number: ").strip()
        logger.debug(f"User selected menu option: {choice}")

        if choice == "1":
            notification_choice = prompt_for_notification()
            logger.info("Running 'search' via menu selection")
            perform_search(notification_choice=notification_choice)
        else:
            logger.warning("Invalid command entered.")
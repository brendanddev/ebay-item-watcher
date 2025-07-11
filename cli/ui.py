
""" 
ui.py
Defines the interactive ui components for the cli based app,
using inquirerpy for the menu and rich for the spinner

Brendan Dileo - July 2025
"""
from time import sleep
from rich.console import Console
from InquirerPy import inquirer

# Creates instance of rich console
console = Console()

# Displays the main menu
def show_main_menu():
    console.print("[bold green]Welcome to eBay Item Watcher![/bold green]\n")
    choice = inquirer.select(
        message="Select an option:",
        choices=[
            "Search items",
            "View last search results",
            "Configure notifications",
            "Help/About",
            "Exit",
        ],
        default="Search items"
    ).execute()
    return choice

# Shows a spinner while processing
def loading_spinner(message="Processing..."):
    with console.status(f"[bold green]{message}[/bold green]", spinner="dots"):
        sleep(3)

# Prompts user for notification method to use
def prompt_for_notification():
    print("Choose notification method(s):")
    print("1. Telegram Bot only")
    print("2. Email only")
    print("3. Both Telegram Bot and Email")
    print("4. None (just display results)")
    choice = input("Enter your choice (1-4): ").strip()
    return choice
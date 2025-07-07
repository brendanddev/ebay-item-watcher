
""" 
main.py
Main entry point to the app

Brendan Dileo - July 2025
"""

from client.auth import get_app_access_token
from client.ebay_api import search


if __name__ == "__main__":
    # Get and print the app access token
    token = get_app_access_token()
    print("Access Token:", token)
    
    # Perform a test search
    query = "laptop"
    results = search(query)
    if results:
        print("Search Results:", results)
    else:
        print("No results found.")

""" 
ebay_api.py
Provides a simple wrapper around the ebay browse api to search for items based on a query

Brendan Dileo - July 2025
"""

import requests
from client import auth
from client import config


# Builds a dictionary of search parameters for the ebay browse api search endpoint
def build_search_params(
    keyword,
    price_min=None,
    price_max=None,
    price_currency=None,
    pickup_postal_code=None,
    pickup_radius=None,
    item_location_region=None,
    item_location_country=None,
    limit=25
):  
    
    # Initialize params dictionary with required keyword and limit
    params = {"q": keyword, "limit": str(limit)}
    filters = []
        
    # Add the price range filter if both min and max prices are provided
    if price_min is not None and price_max is not None:
        price_filter = f"price:{price_min}..{price_max}"
        filters.append(price_filter)
    
    # Add the price currency filter if provided
    if price_currency:
        filters.append(f"priceCurrency:{price_currency}")
    
    # Add the pickup postal code and radius filter if provided
    if pickup_postal_code and pickup_radius:
        params["pickupPostalCode"] = pickup_postal_code
        params["pickupRadius"] = str(pickup_radius)
        filters.append("localPickup:true")
    
    # Add the item location region filter if provided
    if item_location_region:
        params["itemLocationRegion"] = item_location_region
    
    # Add the item location country filter if provided
    if item_location_country:
        params["itemLocationCountry"] = item_location_country

    # Join filters with commans to add to params if any filters were added
    if filters:
        params["filter"] = ",".join(filters)

    # Return the full params dictionary ready for the api req
    return params


# Searches for an item on ebay using the buy API
def search(params):
    
    # Get the access token and validate it
    token = auth.get_app_access_token()
    if not token:
        print("Failed to retrieve access token.")
        return
    
    # Check environment
    is_prod = config.ebay_environment == "production"
    
    # Dynamically set the base url based on the environment
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search" if is_prod else \
          "https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search"
    
    # Define request headers
    headers = { 
        "Authorization": f"Bearer {token}",
        "X-EBAY-C-MARKETPLACE-ID": "EBAY_CA"
    }
    
    # Make GET request and store response
    response = requests.get(url, headers=headers, params=params)
    
    # Check if the request was successful
    # If successful, return the JSON response, otherwise print error
    if response.status_code == 200:
        print("Search successful!")
        return response.json()
    else:
        print("Search failed:", response.status_code, response.text)
        return None

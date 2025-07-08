
""" 
ebay_api.py
Provides a simple wrapper around the ebay browse api to search for items based on a query

Brendan Dileo - July 2025
"""

import requests
from client import auth


# For building the dictionary of search parameters
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
    # Params and fuilters dict
    params = {"q": keyword, "limit": str(limit)}
    filters = []
    
    # CHECKS
    if price_min is not None and price_max is not None:
        price_filter = f"price:{price_min}..{price_max}"
        filters.append(price_filter)
    
    if price_currency:
        filters.append(f"priceCurrency:{price_currency}")
    
    if pickup_postal_code:
        params["pickupPostalCode"] = pickup_postal_code
    
    if pickup_radius:
        params["pickupRadius"] = str(pickup_radius)
    
    if item_location_region:
        params["itemLocationRegion"] = item_location_region
    
    if item_location_country:
        params["itemLocationCountry"] = item_location_country

        
    if filters:
        params["filter"] = ",".join(filters)
    
    
        
    return params





# Searches for an item on ebay using the buy API
def search(params):
    
    # Get the access token and validate it
    token = auth.get_app_access_token()
    if not token:
        print("Failed to retrieve access token.")
        return
    
    # Define api endpoint, headers and params for search request
    url = "https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search"
    headers = { "Authorization": f"Bearer {token}" }
    
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

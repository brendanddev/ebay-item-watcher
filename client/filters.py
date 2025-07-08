""" 
filters.py
...

Brendan Dileo - July 2025
"""

def filter_local_items(items, local_postal_prefix, local_country):
    local_items = []
    for item in items:
        loc = item.get("itemLocation", {})
        postal = loc.get("postalCode", "")
        country = loc.get("country", "")
        if country == local_country and postal.startswith(local_postal_prefix):
            local_items.append(item)
    return local_items
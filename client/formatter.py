
""" 
formatter.py
Formats raw json responses from the ebay API into readable strings

Brendan Dileo - July 2025
"""

# Format a single item into a readable string
def format_item_summary(item):
    title = item.get("title", "No title")
    price = item.get("price", {}).get("value", "N/A")
    currency = item.get("price", {}).get("currency", "N/A")
    url = item.get("itemWebUrl", "No URL")
    return f"🏷️ {title} - 💸 {price} {currency}\n🔗Link: {url}\n"
    
    
# Formats the entire search results into a readable string
def format_search_results(results):

    # Extracts the list of item summaries from the api response
    # Returns an empty list if no results found
    items = results.get("itemSummaries", []) if results else []
    
    if not items:
        return "No items found for the given search criteria."
    
    # Formats each item summary and joins them with new lines
    return "\n\n".join([format_item_summary(item) for item in items])
    

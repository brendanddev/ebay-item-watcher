
""" 
formatter.py
Formats raw json responses from the ebay API into readable strings

Brendan Dileo - July 2025
"""

def get_location(item):
    loc = item.get("itemLocation", {})
    # Try to get these keys; fallback to empty string if not found
    city = loc.get("city", "") or ""
    province = loc.get("stateOrProvince") or loc.get("provinceOrState") or ""
    country = loc.get("country") or ""

    # Postal code fallback if available
    postal_code = loc.get("postalCode") or ""

    # Build parts list only with non-empty strings
    parts = [p for p in [city, province, postal_code, country] if p]

    return ", ".join(parts) if parts else "Unknown location"


def format_item_summary(item, index=None):
    title = item.get("title", "No title")
    price = item.get("price", {}).get("value", "N/A")
    currency = item.get("price", {}).get("currency", "N/A")
    location = get_location(item)
    url = item.get("itemWebUrl", "No URL")

    # Shorten the URL display (for Telegram, links can be markdown formatted)
    link = f"[View Item]({url})" if url != "No URL" else url

    return f"{index+1 if index is not None else ''}. 🏷️ {title}\n💸 {price} {currency} 📍 {location}\n🔗 {link}\n"

    
# Formats the entire search results into a readable string
def format_search_results(results, max_items=15, max_total_length=4000):
    
    # Extracts the list of item summaries from the api response
    # Returns an empty list if no results found
    items = results.get("itemSummaries", []) if results else []
    
    if not items:
        return "No items found for the given search criteria."

    output_lines = []
    total_length = 0
    for i, item in enumerate(items[:max_items]):
        summary = format_item_summary(item, i)
        if total_length + len(summary) + 2 > max_total_length:
            break
        output_lines.append(summary)
        total_length += len(summary) + 2

    return "\n\n".join(output_lines)
    

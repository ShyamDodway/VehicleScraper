import requests
from bs4 import BeautifulSoup
import json

# Use a website that permits automated access
url = "https://books.toscrape.com/"

response = requests.get(url, timeout=20)
response.raise_for_status()

# Convert HTML into a structure Python can search
soup = BeautifulSoup(response.text, "html.parser")

books = []

# Find each product card
for item in soup.select("article.product_pod"):
    title_tag = item.select_one("h3 a")
    price_tag = item.select_one(".price_color")

    if title_tag and price_tag:
        books.append({
            "title": title_tag.get("title", ""),
            "price": price_tag.get_text(strip=True)
        })

# Save locally as JSON
with open("practice_data.json", "w", encoding="utf-8") as file:
    json.dump(books, file, indent=4, ensure_ascii=False)

print(f"Saved {len(books)} items.")
import requests
import csv
import os
from datetime import datetime

API_KEY = "f8a344e8-350c-4f18-858b-cb741100d721"

URL = f"https://content.guardianapis.com/search?api-key={API_KEY}&show-fields=bodyText&page-size=10"

response = requests.get(URL)
data = response.json()

articles = data["response"]["results"]

today = datetime.utcnow().strftime("%Y-%m-%d")

with open("news.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    for article in articles:
        headline = article["webTitle"]
        date = article["webPublicationDate"]
        body = article["fields"].get("bodyText", "")

        writer.writerow([today, date, headline, body])

print("News collected.")

import requests
import os
from datetime import datetime
import csv

NYT_KEY = "ArW0ySTAZ760ACM3xLKaXbdiz2sSvARUUj2SpXqKlK0S83Gp"
url = f"https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={NYT_KEY}"

resp = requests.get(url)
data = resp.json()

today = datetime.utcnow().strftime("%Y-%m-%d")

with open("booksales.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    for book in data["results"]["books"]:
        writer.writerow([
            today,
            book["title"],
            book["author"],
            book["rank"],
            book.get("description", "")
        ])

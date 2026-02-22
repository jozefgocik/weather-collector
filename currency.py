import requests
from datetime import datetime
import csv

URL = "https://api.exchangerate.host/latest?base=USD"

response = requests.get(URL)
data = response.json()

date = data["date"]
rates = data["rates"]

today = datetime.utcnow().strftime("%Y-%m-%d")
time = datetime.utcnow().strftime("%H:%M")

# Write CSV
with open("currency.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # Header if file is new
    # Uncomment if writing new file
    # writer.writerow(["date", "time", "base", "target", "rate"])

    for target, rate in rates.items():
        writer.writerow([today, time, data["base"], target, rate])

print("Currency rates saved.")

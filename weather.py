import requests
import csv
from datetime import datetime

API_KEY = "db715d0af3dbc1308a640aa3fbe3f599"
CITY = "Bratislava"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

now = datetime.utcnow()

row = [
    now.strftime("%Y-%m-%d"),
    now.strftime("%H:%M"),
    data["main"]["temp"],
    data["main"]["humidity"],
    data["wind"]["speed"],
    data["weather"][0]["description"]
]

with open("weather.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(row)

print("Saved weather.")

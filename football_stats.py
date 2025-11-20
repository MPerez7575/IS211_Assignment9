# Source: https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions
# Description: Scrapes the Wikipedia table of Super Bowl Champions and prints
#              the results (Game, Winner, Loser, and Score) in a clean format.

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# URL
URL = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Step 1: Fetch the page
response = requests.get(URL, headers=HEADERS)
if response.status_code != 200:
    print(f"Failed to load page (status {response.status_code})")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table")
target_table = None
for t in tables:
    caption = t.find("caption")
    if caption and "Super Bowl" in caption.get_text():
        target_table = t
        break

if not target_table:
    print("Could not find the Super Bowl table.")
    exit()

data = []
for row in target_table.find_all("tr")[1:]:  # skip header
    cols = [c.get_text(strip=True) for c in row.find_all(["th", "td"])]
    if len(cols) >= 7:
        game = cols[0]
        winner = cols[2]
        score = cols[3]
        loser = cols[4]
        data.append([game, winner, loser, score])

if data:
    headers = ["Game", "Winner", "Loser", "Score"]
    print(tabulate(data, headers=headers, tablefmt="grid"))
else:
    print("No rows found in the Super Bowl table.")

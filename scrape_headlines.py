import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

headlines = []

page_title = soup.title.string.strip() if soup.title else ""
if page_title:
    headlines.append(page_title)

for h2 in soup.find_all('h2'):
    text = h2.get_text(strip=True)
    if text:
        headlines.append(text)

with open("headlines.txt", "w", encoding="utf-8") as file:
    for line in headlines:
        file.write(line + "\n")

print(f"{len(headlines)} headlines saved to headlines.txt")
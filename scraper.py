import requests
from bs4 import BeautifulSoup


url = input("Url of the website you want to scrape: ")

req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

res = soup.title    # For scraping the title of website

print(res.get_text())
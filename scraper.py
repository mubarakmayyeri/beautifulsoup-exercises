import requests
from bs4 import BeautifulSoup


url = input("Url of the website you want to scrape: ")

req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())
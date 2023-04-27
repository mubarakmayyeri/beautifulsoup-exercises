# Beautiful Soup Exercises
Learning web scraping with Beautiful Soup Python Library

## How to create a basic webscraper
1. Insatll necessary libraries

```shell
pip install beautifulsoup4 request
```

2. Create a python application for scraping
```python
import requests
from bs4 import BeautifulSoup


url = input("Url of the website you want to scrape: ")

req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())
```

3. Run the python file
```shell
python scraper.py
```
Now you will be able too see the Html content of the url provided as input in your terminal.

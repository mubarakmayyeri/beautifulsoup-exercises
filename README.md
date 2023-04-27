# Beautiful Soup Exercises
Learning web scraping with Beautiful Soup Python Library

## How to create a basic webscraper
1. Insatll necessary libraries

```shell
pip install beautifulsoup4 requests lxml
```

2. Create a python application for scraping
```python
import requests
from bs4 import BeautifulSoup


url = input("Url of the website you want to scrape: ")

req = requests.get(url)
soup = BeautifulSoup(req.content, "lxml")

res = soup.title    # For scraping the title of website

print(res.get_text())
```

3. Run the python file
```shell
python scraper.py
```
Now give the website url as input and you will be able too see the `title` of the webiste in your terminal.

## References
1. Beautiful Soup Docs - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
2. Geekforgeeks Tutorial - https://www.youtube.com/watch?v=O6nnVHPjcJU&ab_channel=GeeksforGeeks
3. FreedCamp Tutorial - https://www.youtube.com/watch?v=XVv6mJpFOb0&t=1280s&ab_channel=freeCodeCamp.org


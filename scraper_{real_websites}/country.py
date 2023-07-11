import requests
from bs4 import BeautifulSoup
try:
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",}
    req = requests.get("https://www.worldometers.info/gdp/gdp-by-country/", headers=headers)
    #for findimg out the link is valid or not
    req.raise_for_status()
    soup=BeautifulSoup(req.text,"html.parser")
    Ranking=soup.find_all('td', attrs={'style': "font-weight: bold; font-size:17px; text-align:left; padding-left:5px; padding-top:10px; padding-bottom:10px"})

    for rank in Ranking:
        print(rank.a.text)
     

except Exception as e:
    print(e)
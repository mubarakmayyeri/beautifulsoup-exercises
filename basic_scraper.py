from bs4 import BeautifulSoup

with open('website-example/home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    res = soup.title

    print(res.get_text())
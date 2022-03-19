import requests as rq
from bs4 import BeautifulSoup

page = rq.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

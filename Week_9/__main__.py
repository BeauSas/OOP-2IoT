import requests as rq
from bs4 import BeautifulSoup as bs

URL =  "https://www.velo-antwerpen.be/availability_map/getJsonObject"
page = rq.get(URL)

soup = bs(page.content, "html.parser")

print(soup.prettify())
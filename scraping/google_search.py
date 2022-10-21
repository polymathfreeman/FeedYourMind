import requests
from bs4 import BeautifulSoup

website = input("url = ")
r = requests.get(website).text
soup = BeautifulSoup(r, "html.parser")
print([x.get("title") for x in soup.findAll("input") if x.get("title")])
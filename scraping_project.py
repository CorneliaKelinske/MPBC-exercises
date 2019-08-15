import requests
from bs4 import BeautifulSoup

response = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("quote")
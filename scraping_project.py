import requests
from bs4 import BeautifulSoup


all_quotes = []
response = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all(class_="quote")

for quote in quotes:
    quote_text = quote.find(class_="text").get_text()
    print(quote_text)





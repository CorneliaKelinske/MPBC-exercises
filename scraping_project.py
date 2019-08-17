import requests
from bs4 import BeautifulSoup


all_quotes = []
response = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all(class_="quote")

for quote in quotes:
    a_tag = quote.find("a")
    all_quotes.append({"text": quote.find(class_="text").get_text(),
    "author" : quote.find(class_="author").get_text(), 
    "href": a_tag['href']})

print(all_quotes)




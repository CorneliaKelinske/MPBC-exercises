import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice


all_quotes = []
base_url = "http://quotes.toscrape.com"
url = "/page/1"

while url:
        response = requests.get(f"{base_url}{url}")
        #print(f"Now scrapping {base_url}{url}...")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
    
                all_quotes.append({
                        "text": quote.find(class_="text").get_text(), 
                        "author" : quote.find(class_="author").get_text(), 
                        "bio_link": quote.find("a")["href"]
                        })
        next_button = soup.find(class_="next")
        url = next_button.find("a")["href"] if next_button else None
        #sleep(2)
#print(random.choice(all_quotes)["text"])

chosen_quote = choice(all_quotes)
remaining_guesses = 4
print("Here is a quote:")
print(chosen_quote["text"])
print(chosen_quote["author"])
guess = " "

while guess.lower() != chosen_quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this? Guess! You have {remaining_guesses} more guesses. ")
        remaining_guesses -= 1
        if remaining_guesses == 3:
                res = requests.get(f"{base_url}{chosen_quote['bio_link']}")
                soup = BeautifulSoup(res.text, "html.parser")
                birth_date = soup.find(class_="author-born-date").get_text()
                birth_place = soup.find(class_="author-born-location").get_text()
               
                print(f"Here is a hint: the author was born on {birth_date} in {birth_place}.")
                
        else:
                print("try again")


               
  
                #I need to make another scraping call, go to biolink, and then scrape there for author birth date and place

       
print("after while loop")







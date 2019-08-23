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
play = "yes"
while play == "yes":

        chosen_quote = choice(all_quotes)
        remaining_guesses = 4
        print("Here is a quote:")
        print(chosen_quote["text"])
        #print(chosen_quote["author"])
        guess = " "

        while guess.lower() != chosen_quote["author"].lower() and remaining_guesses > 0:
                guess = input(f"Who said this? Guess! You have {remaining_guesses} more guesses. ")
                remaining_guesses -= 1
                if remaining_guesses == 3 and guess.lower() != chosen_quote["author"].lower():
                        res = requests.get(f"{base_url}{chosen_quote['bio_link']}")
                        soup = BeautifulSoup(res.text, "html.parser")
                        birth_date = soup.find(class_="author-born-date").get_text()
                        birth_place = soup.find(class_="author-born-location").get_text()
               
                        print(f"Here is a hint: the author was born on {birth_date} {birth_place}.")
                
                elif remaining_guesses == 2 and guess.lower() != chosen_quote["author"].lower():
                        first_name = chosen_quote["author"].split(" ")[0][0]
                        print(f"Here is another hint: the first letter of the author's first name is {first_name}")
                elif remaining_guesses == 1 and guess.lower() != chosen_quote["author"].lower():
                        last_name = chosen_quote["author"].split(" ")[-1][0]
                        print(f"Here is another hint: the first letter of the author's last name is {last_name}")
                elif remaining_guesses == 0 and guess.lower() != chosen_quote["author"].lower():
                        print(f"You have no more guesses. The correct answer would have been: {chosen_quote['author']}")
                else:
                        print("Good job! You win!")
                
        play = input("Would you like to play again? yes or no ").lower()








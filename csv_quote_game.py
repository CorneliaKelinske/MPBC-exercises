import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com"
url = "/page/1"

def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(quotes):

    chosen_quote = choice(quotes)
    remaining_guesses = 4
    print("Here is a quote:")
    print(chosen_quote["text"])
    #print(chosen_quote["author"])
    guess = " "

    while guess.lower() != chosen_quote["author"].lower() and remaining_guesses > 0:
        guess = input(
            f"Who said this? Guess! You have {remaining_guesses} more guesses.\n")
        if guess.lower() == chosen_quote["author"].lower():
            print("You got it right!")
            break
        remaining_guesses -= 1
        print_hint(chosen_quote, remaining_guesses)
        
    again = ' '
    while again.lower() not in ('yes', 'y', 'no', 'n'):
        again = input("Would you like to play again (y/n)? ")
    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print("OK, GOODBYE!")

def print_hint(chosen_quote, remaining_guesses):
    if remaining_guesses == 3:
        res = requests.get(f"{BASE_URL}{chosen_quote['bio_link']}")
        soup = BeautifulSoup(res.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()

        print(
            f"Here is a hint: the author was born on {birth_date} in {birth_place}.")
    elif remaining_guesses == 2:
        print(
                f"Here is a hint: the author's first name starts with {chosen_quote['author'][0]}.")
    elif remaining_guesses == 1:
            # this will not work if the author has a middle name
        last_initial = chosen_quote["author"].split(" ")[1][0]
        print(
            f"Here is a hint: the author's last name starts with {last_initial}.")
    else:
        print(
            f"Sorry, you ran out of guesses! The answer was {chosen_quote['author']}")
quotes = read_quotes("quotes.csv")
start_game(quotes)
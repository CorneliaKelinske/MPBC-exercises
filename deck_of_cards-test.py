import unittest
from deck_of_cards_OOP import Card, Deck

class CardTests (unittest.TestCase):
    def setUp(self):
        self.card = Card("A", "Hearts")

    def test_init(self):
        """cards should have a value and a suit"""
        self.assertEqual(self.card.value, "A")
        self.assertEqual(self.card.suit, "Hearts")
    
    def test_repr(self):
        """repr should return a string saying 'VALUE of SUIT'"""
        self.assertEqual(repr(self.card), "A of Hearts")


class DeckTest (unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
    
    def test_init(self):
        """Deck should have a cards attribute that is a list of 52 cards"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)
    
    def test_repr(self):
        """repr should return a string saying how many cards are in the deck"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")
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

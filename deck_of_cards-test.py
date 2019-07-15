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
    
    def test_count(self):
        """count should return the number of cards that are currently in the deck"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_sufficient_cards(self):
        """_deal should return the number of cards specified, and take that number of cards away from the deck"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)
    
    def test_deal_insufficient_cards(self):
        """in this case, _deal should return the remaining number of cards and the deck should be empty afterwards"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        """_deal should throw a value error if the deck is empty"""
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)
    
    def test_deal_card(self):
        """deal_card shoud deal a single card from the deck"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        """deal_hand should deal the number of cards passed in as the hand size"""
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        """shuffle should shuffle the deck if the deck is full"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)
    
    def test_shuffle_not_full_deck(self):
        """shuffle should throw a ValueError if the deck is not full"""
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()
    
if __name__ == "__main__":
    unittest.main()
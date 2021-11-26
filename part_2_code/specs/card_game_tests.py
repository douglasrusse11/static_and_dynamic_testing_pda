import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_game = CardGame()
    
    def test_check_for_ace_returns_true(self):
        self.card = Card(1,1)
        self.assertTrue(self.card_game.check_for_ace(self.card))

    def test_check_for_ace_returns_false(self):
        self.card = Card(1, 2)
        self.assertFalse(self.card_game.check_for_ace(self.card))

    def test_highest_card_card1_gt_card2_returns_card1(self):
        self.card1 = Card(2, 10)
        self.card2 = Card(0, 4)
        self.assertEqual(self.card1, self.card_game.highest_card(self.card1, self.card2))
    
    def test_highest_card_card1_lt_card2_returns_card2(self):
        self.card1 = Card(3, 7)
        self.card2 = Card(0, 9)
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))
    
    def test_highest_card_card1_eq_card2_returns_card2(self):
        self.card1 = Card(3, 7)
        self.card2 = Card(0, 7)
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))

    def test_cards_total_empty_list_returns_zero(self):
        self.cards = []
        self.assertEqual("You have a total of 0", self.card_game.cards_total(self.cards))
    
    def test_cards_total(self):
        self.card1 = Card(2, 10)
        self.card2 = Card(0, 4)
        self.card3 = Card(3, 7)
        self.card4 = Card(0, 9)
        self.cards = [self.card1, self.card2, self.card3, self.card4]
        self.assertEqual("You have a total of 30", self.card_game.cards_total(self.cards))
import unittest
from deck import Deck
from hand_evaluator import HandEvaluator
from PokerBot import PokerBot

class TestPokerBot(unittest.TestCase):

    def test_deck(self):
        """Test that the deck is initialized correctly and shuffles without duplications."""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        unique_cards = set(deck.cards)
        self.assertEqual(len(unique_cards), 52)

        drawn_cards = deck.draw(5)
        self.assertEqual(len(drawn_cards), 5)
        self.assertEqual(len(deck.cards), 47)

    def test_hand_evaluator(self):
        """Test the HandEvaluator for basic hand rankings."""
        evaluator = HandEvaluator()

        # Test High Card
        high_card = ['2♠', '5♦', '8♣', 'J♥', 'A♠']
        result = evaluator.evaluate_hand(high_card)
        self.assertEqual(result[0], 1)  # High Card

        # Test Flush
        flush = ['2♠', '5♠', '8♠', 'J♠', 'A♠']
        result = evaluator.evaluate_hand(flush)
        self.assertEqual(result[0], 6)  # Flush

        # Test Straight
        straight = ['5♠', '4♦', '3♣', '2♥', '6♠']
        result = evaluator.evaluate_hand(straight)
        self.assertEqual(result[0], 5)  # Straight

    def test_poker_bot(self):
        """Test the PokerBot decision-making logic."""
        bot = PokerBot()

        # Fixed hole cards and community cards
        hole_cards = ['A♠', 'K♠']
        community_cards = ['10♠', 'J♠', 'Q♠']

        decision = bot.make_decision(hole_cards, community_cards)
        self.assertEqual(decision, "stay")  # Should stay with a royal flush draw

        # Testing fold case with weak hand
        hole_cards = ['2♣', '3♦']
        community_cards = []
        decision = bot.make_decision(hole_cards, community_cards)
        self.assertEqual(decision, "fold")

if __name__ == '__main__':
    unittest.main()

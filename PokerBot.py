from deck import Deck
from hand_evaluator import HandEvaluator
from mcts import MCTS
import random


class PokerBot:
    """
    PokerBot class using Monte Carlo Tree Search (MCTS) to decide fold or stay.
    """

    def __init__(self):
        self.deck = Deck()
        self.evaluator = HandEvaluator()
        self.mcts = MCTS(time_limit=10)

    def make_decision(self, hole_cards, community_cards):
        """
        Makes a decision (fold or stay) based on MCTS win probability.
        """
        known_state = hole_cards + community_cards

        def evaluate_simulation(state):
            simulated_deck = [card for card in self.deck.cards if card not in state]
            random.shuffle(simulated_deck)

            opponent_cards = [simulated_deck.pop(), simulated_deck.pop()]
            full_community = state + simulated_deck[:5 - len(community_cards)]

            bot_score = self.evaluator.evaluate_hand(hole_cards + full_community)
            opponent_score = self.evaluator.evaluate_hand(opponent_cards + full_community)

            return 1 if bot_score > opponent_score else 0

        root = self.mcts.search(known_state, evaluate_simulation)
        win_probability = root.children[0].wins / root.children[0].visits

        return "stay" if win_probability >= 0.5 else "fold"

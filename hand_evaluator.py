from collections import Counter

class HandEvaluator:
    """
    HandEvaluator class to rank Texas Hold'em hands.
    This class supports evaluating 5 to 7 card hands.
    """

    def evaluate_hand(self, cards):
        """
        Evaluates the strength of a poker hand and returns a score for comparison.
        Args:
            cards (list): A list of card strings (e.g., ['AS', 'KH', 'QD']).
        Returns:
            tuple: (hand_rank, high_cards) where hand_rank is an integer (higher is better).
        """
        values = sorted([self.card_value(card[0:-1]) for card in cards], reverse=True)
        suits = [card[-1] for card in cards]

        if self.is_flush(suits):
            return (6, values)
        elif self.is_straight(values):
            return (5, values)
        else:
            return (1, values)  # High card by default

    def card_value(self, rank):
        """
        Maps card rank to an integer value.
        """
        rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                       '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return rank_values[rank]

    def is_flush(self, suits):
        """
        Checks if all cards share the same suit.
        """
        return max(Counter(suits).values()) >= 5

    def is_straight(self, values):
        """
        Checks if values form a consecutive sequence.
        """
        unique_values = sorted(set(values), reverse=True)
        for i in range(len(unique_values) - 4):
            if unique_values[i] - unique_values[i + 4] == 4:
                return True
        return False

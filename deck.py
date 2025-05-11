import random

class Deck:
    """
    Deck class that manages a standard 52-card deck for Texas Hold'em Poker.
    Supports shuffling, drawing, and tracking remaining cards.
    """

    def __init__(self):
        """
        Initializes a standard 52-card deck.
        Suits: Spades (♠), Hearts (♥), Diamonds (♦), Clubs (♣).
        Ranks: 2-10, Jack, Queen, King, Ace.
        """
        self.suits = ['♠', '♥', '♦', '♣']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [rank + suit for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        """
        Shuffles the deck randomly.
        """
        random.shuffle(self.cards)

    def draw(self, count=1):
        """
        Draws the specified number of cards from the deck.
        Args:
            count (int): Number of cards to draw.
        Returns:
            list: A list of drawn cards.
        """
        if count > len(self.cards):
            raise ValueError("Not enough cards remaining in the deck.")
        drawn_cards = self.cards[:count]
        self.cards = self.cards[count:]
        return drawn_cards

    def remaining(self):
        """
        Returns the number of remaining cards in the deck.
        """
        return len(self.cards)
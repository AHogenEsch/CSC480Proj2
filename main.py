from PokerBot import PokerBot

if __name__ == "__main__":
    bot = PokerBot()

    # Deal two hole cards
    hole_cards = bot.deck.draw(2)
    print(f"Your Hole Cards: {hole_cards}")

    # Community Cards (Flop, Turn, River)
    community_cards = []

    # Pre-Flop Decision
    decision = bot.make_decision(hole_cards, community_cards)
    print(f"Pre-Flop Decision: {decision}")

    # Deal Flop (3 cards)
    community_cards += bot.deck.draw(3)
    print(f"Community Cards (Flop): {community_cards}")

    # Pre-Turn Decision
    decision = bot.make_decision(hole_cards, community_cards)
    print(f"Pre-Turn Decision: {decision}")

    # Deal Turn (1 card)
    community_cards += bot.deck.draw(1)
    print(f"Community Cards (Turn): {community_cards}")

    # Pre-River Decision
    decision = bot.make_decision(hole_cards, community_cards)
    print(f"Pre-River Decision: {decision}")

    # Deal River (1 card)
    community_cards += bot.deck.draw(1)
    print(f"Community Cards (River): {community_cards}")

    # Final Decision
    decision = bot.make_decision(hole_cards, community_cards)
    print(f"Final Decision: {decision}")

#include "pokerBot.h"

// Initializes the PokerBot with a shuffled deck
void initialize_poker_bot(PokerBot *bot) {
    initialize_deck(&bot->deck);
    shuffle_deck(&bot->deck);
}

// Makes a decision (stay or fold) using MCTS
const char *make_decision(PokerBot *bot, Card *hole_cards, Card *community_cards, int community_count) {
    Card initial_state[7];

    // Copy hole cards to initial state
    initial_state[0] = hole_cards[0];
    initial_state[1] = hole_cards[1];

    // Copy community cards
    for (int i = 0; i < community_count; i++) {
        initial_state[2 + i] = community_cards[i];
    }

    // Run MCTS
    MCTSNode *result = mcts_search(initial_state, &bot->deck);

    // Simple decision logic: if win rate > 50%, stay
    if (result->wins > result->visits / 2) {
        return "stay";
    } else {
        return "fold";
    }
}
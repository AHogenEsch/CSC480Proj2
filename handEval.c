#include "handEval.h"
#include <string.h>

// Helper function to sort cards by rank
int card_rank_value(char rank) {
    switch (rank) {
        case '2': return 2;
        case '3': return 3;
        case '4': return 4;
        case '5': return 5;
        case '6': return 6;
        case '7': return 7;
        case '8': return 8;
        case '9': return 9;
        case 'T': return 10;
        case 'J': return 11;
        case 'Q': return 12;
        case 'K': return 13;
        case 'A': return 14;
        default: return 0;
    }
}

// Evaluates the rank of a hand (simple version for now)
HandRank evaluate_hand(Card *cards, int card_count) {
    // Simple check for high card (will be expanded)
    return HIGH_CARD;
}

// Compares two hands (returns 1 if hand1 wins, -1 if hand2 wins, 0 if tie)
int compare_hands(Card *hand1, Card *hand2, int card_count) {
    HandRank rank1 = evaluate_hand(hand1, card_count);
    HandRank rank2 = evaluate_hand(hand2, card_count);

    if (rank1 > rank2) return 1;
    if (rank2 > rank1) return -1;

    // Further comparison based on high cards (not yet implemented)
    return 0;
}

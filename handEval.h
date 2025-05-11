#ifndef HANDEVAL_H
#define HANDEVAL_H

#include "deck.h"

// Hand Rank Enum (High Card = 1, Pair = 2, ..., Royal Flush = 10)
typedef enum {
    HIGH_CARD = 1, PAIR, TWO_PAIR, THREE_OF_A_KIND, STRAIGHT,
    FLUSH, FULL_HOUSE, FOUR_OF_A_KIND, STRAIGHT_FLUSH, ROYAL_FLUSH
} HandRank;

// Function Prototypes
HandRank evaluate_hand(Card *cards, int card_count);
int compare_hands(Card *hand1, Card *hand2, int card_count);

#endif

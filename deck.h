#ifndef DECK_H
#define DECK_H

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define DECK_SIZE 52

// Structure representing a card
typedef struct {
    char rank;
    char suit;
} Card;

// Structure representing the deck
typedef struct {
    Card cards[DECK_SIZE];
    int top_card_index;
} Deck;

// Deck Functions
void initialize_deck(Deck *deck);
void shuffle_deck(Deck *deck);
Card draw_card(Deck *deck);

#endif

#include "deck.h"

// Initializes the deck with 52 standard playing cards
void initialize_deck(Deck *deck) {
    char suits[] = {'S', 'H', 'D', 'C'}; // Spades, Hearts, Diamonds, Clubs
    char ranks[] = {'2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'};
    int index = 0;

    for (int s = 0; s < 4; s++) {
        for (int r = 0; r < 13; r++) {
            deck->cards[index].suit = suits[s];
            deck->cards[index].rank = ranks[r];
            index++;
        }
    }
    deck->top_card_index = 0;
}

// Shuffles the deck using Fisher-Yates algorithm
void shuffle_deck(Deck *deck) {
    srand(time(NULL));
    for (int i = DECK_SIZE - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        Card temp = deck->cards[i];
        deck->cards[i] = deck->cards[j];
        deck->cards[j] = temp;
    }
}

// Draws a card from the top of the deck
Card draw_card(Deck *deck) {
    if (deck->top_card_index >= DECK_SIZE) {
        fprintf(stderr, "Deck is empty. Cannot draw.");
        exit(EXIT_FAILURE);
    }
    return deck->cards[deck->top_card_index++];
}

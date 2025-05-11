#ifndef MCTS_H
#define MCTS_H

#include "deck.h"
#include "hand_evaluator.h"

// MCTS Node Structure
typedef struct MCTSNode {
    Card state[7]; // 2 hole cards + up to 5 community cards
    int wins;
    int visits;
    struct MCTSNode *parent;
    struct MCTSNode *children[100]; // Max children
    int child_count;
} MCTSNode;

// Function Prototypes
MCTSNode *create_node(Card *state, int card_count);
void expand_node(MCTSNode *node, Deck *deck);
double ucb1(MCTSNode *node, int parent_visits);
MCTSNode *mcts_search(Card *initial_state, Deck *deck);

#endif

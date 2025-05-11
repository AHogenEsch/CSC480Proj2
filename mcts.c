#include "mcts.h"
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

// Creates a new MCTS node
MCTSNode *create_node(Card *state, int card_count) {
    MCTSNode *node = (MCTSNode *)malloc(sizeof(MCTSNode));
    for (int i = 0; i < card_count; i++) {
        node->state[i] = state[i];
    }
    node->wins = 0;
    node->visits = 0;
    node->parent = NULL;
    node->child_count = 0;
    return node;
}

// Expands a node with possible moves (draw remaining community cards)
void expand_node(MCTSNode *node, Deck *deck) {
    for (int i = 0; i < 10; i++) { // Simulate 10 possible future states
        Card new_state[7];
        memcpy(new_state, node->state, sizeof(node->state));
        new_state[2 + i] = draw_card(deck); // Simulate community cards

        MCTSNode *child = create_node(new_state, 7);
        child->parent = node;
        node->children[node->child_count++] = child;
    }
}

// Calculates UCB1 value for a node
double ucb1(MCTSNode *node, int parent_visits) {
    if (node->visits == 0) return INFINITY;
    return ((double)node->wins / (double)node->visits) + 
           sqrt(2 * log(parent_visits) / node->visits);
}

// Runs MCTS search from the initial state
MCTSNode *mcts_search(Card *initial_state, Deck *deck) {
    MCTSNode *root = create_node(initial_state, 2);
    clock_t start = clock();

    while (((double)(clock() - start) / CLOCKS_PER_SEC) < 10.0) { // 10 second limit
        MCTSNode *current = root;

        // Selection and Expansion
        if (current->child_count == 0) expand_node(current, deck);

        // Randomly simulate one child
        int random_child = rand() % current->child_count;
        MCTSNode *selected = current->children[random_child];

        // Simulate game outcome
        int result = rand() % 2; // Random win/loss for now
        selected->wins += result;
        selected->visits++;
        current->visits++;
    }

    return root;
}

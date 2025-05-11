import random
import math
import time

class MCTSNode:
    """
    Represents a node in the MCTS tree.
    Each node tracks wins, visits, and potential child states.
    """

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0

    def ucb1(self):
        """
        Calculates the UCB1 value for this node.
        """
        if self.visits == 0:
            return float('inf')
        return (self.wins / self.visits) + math.sqrt(2 * math.log(self.parent.visits) / self.visits)

    def select_child(self):
        """
        Selects the child with the highest UCB1 value.
        """
        return max(self.children, key=lambda child: child.ucb1())

    def expand(self, possible_moves):
        """
        Expands this node by creating children for possible moves.
        """
        for move in possible_moves:
            child_node = MCTSNode(move, parent=self)
            self.children.append(child_node)

    def backpropagate(self, result):
        """
        Backpropagates the simulation result up the tree.
        """
        self.visits += 1
        self.wins += result
        if self.parent:
            self.parent.backpropagate(result)


class MCTS:
    """
    Monte Carlo Tree Search (MCTS) implementation with UCB1.
    """

    def __init__(self, time_limit=10):
        self.time_limit = time_limit

    def search(self, initial_state, evaluator):
        root = MCTSNode(initial_state)
        start_time = time.time()

        while time.time() - start_time < self.time_limit:
            node = root
            if not node.children:
                node.expand([initial_state])
            result = evaluator(node.state)
            node.children[0].backpropagate(result)

        return root

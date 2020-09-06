'''
To-Do:
    - Fix valid moves method (emptyCells)
    - Prune the tree when a child in it is already played (RuleAgent)
'''

from numpy import random

from exp_tree import ExpTree
from expressions import Cell, And, Or
from strategy_tree import parseStrategyTree

class RandomAgent:
    def __init__(self, color):
        self.color = color

    def step(self, state):
        valid_moves = self.emptyCells(state)
        action = valid_moves[random.randint(len(valid_moves))]
        return action
    
    def emptyCells(self, state):
        res = []
        for i in range(len(state[0])):
            for j in range(len(state[1])):
                if state[i][j] == '.':
                    res.append([i, j])
        return res


class RuleAgent:
    def __init__(self, color, exp):
        self.color = color
        exp_tree = ExpTree(exp)
        self.root = parseStrategyTree(exp_tree.root)

    def moves(self, state, last_move):
        '''
        last_move: Cell object or None - MUST
        '''
        # assert(isinstance(last_move, Cell))
        pos_moves = self.next_moves(last_move)
        return list(set(pos_moves)) # returns all possible moves

    def next_moves(self, root):
        if root is None:
            return [self.root]
        pos_moves = []
        for c in root.children:
            if isinstance(c, Or):
                pos_moves.extend(c.children)
            else:
                pos_moves.append(c)
        return pos_moves


class Human:
    def __init__(self, color):
        self.color = color

    def step(self, state):
        print(state)
        x, y = input('x space y: ')
        return [int(x), int(y)]
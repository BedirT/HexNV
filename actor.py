'''
To-Do:
    - Fix valid moves method (emptyCells)
    - Prune the tree when a child in it is already played (RuleAgent)
'''

from numpy import random

from exp_tree import ExpTree

from expressions import Cell, And, Or

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
        # exp_tree = ExpTree(exp)
        
        ##### PLACEHOLDER TREE
        c = Cell('a1')
        d = Or()
        c.left = d
        d.left = Cell('b1')
        d.right = Cell('b2')
        root = c 
        #####################

        self.strategy = root

    def moves(self, state, last_move):
        '''
        last_move: Cell object or None - MUST
        '''
        pos_moves = self.next_moves(last_move)
        return pos_moves # returns all possible moves

    def next_moves(self, root):
        if root is None:
            return [self.strategy]
        pos_moves = self.getChilds(root.left) + self.getChilds(root.right)
        return pos_moves

    def getChilds(self, root):
        children = []
        if root is None:
            return []
        elif root.val == 'or':
            children = children + self.getChilds(root.left)
            children = children + self.getChilds(root.right)
        else:
            children.append(root)
        return children


class Human:
    def __init__(self, color):
        self.color = color

    def step(self, state):
        print(state)
        x, y = input('x space y: ')
        return [int(x), int(y)]
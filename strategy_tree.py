from expressions import And
from expressions import Or
from expressions import Cell
from expressions import Root
from expressions import TrueCell

import copy
import sys

sys.setrecursionlimit(10 ** 9)

def appendToLeaves(leaves, root):
    if not leaves.children:
        leaves.children = copy.deepcopy(root)
        return
    for child in leaves.children:
        appendToLeaves(child, root)

def changeTheCorrespondingChild(target, old, new):
    if isinstance(target, Root):
        return new 
    for i, x in enumerate(target.subs):
        if x == old:
            target.subs[i] = new
            return None
    

def parseStrategyTree(root):
    '''
    Given root node, this method will parse through and re-arrange
    the tree as a strategy tree instead of an expression tree. That is
    -and            -->     -b2
    ---b2                   ---b1
    ---b1                   -----a1
    -----and                -------a2
    -------a1               -----c1
    -------a2
    -----c1
    '''
    if isinstance(root, Cell):
        return

    for i in range(len(root.subs)):
        parseStrategyTree(root.subs[i])

    end = None

    if isinstance(root, And):
        # Both branches are Cell objects
        if isinstance(root.subs[0], Cell) and isinstance(root.subs[1], Cell):
            # Find the smaller branch - To Do
            v1 = root.subs[0]
            v2 = root.subs[1]
            # 2
            # print(type(root.parent))
            v2.parent = root.parent
            root.parent.children.append(v2)
            # 4
            appendToLeaves(v2, [v1])

            end = changeTheCorrespondingChild(root.parent, root, v2)
            root = v2
        elif isinstance(root.subs[0], Or) and isinstance(root.subs[1], Cell):
            or1 = root.subs[0]
            v = root.subs[1]
            
            v.parent = root.parent
            root.parent.children.append(v)
            v.children.extend(or1.children)
            end = changeTheCorrespondingChild(root.parent, root, v)

            root = v
        elif isinstance(root.subs[0], Cell) and isinstance(root.subs[1], Or):
            v = root.subs[0]
            or1 = root.subs[1]
            
            v.parent = root.parent
            root.parent.children.append(v)
            v.children.extend(or1.children)
            end = changeTheCorrespondingChild(root.parent, root, v)

            root = v
        elif isinstance(root.subs[0], Or) and isinstance(root.subs[1], Or):
            # CHANGE NEEDED AFTER OR-ROOT
            or1 = root.subs[0]
            or2 = root.subs[1]

            # 1
            or1.parent = root.parent
            root.parent.children.append(or1)
            end = changeTheCorrespondingChild(root.parent, root, or1)
            # 2
            oldor1_children = copy.deepcopy(or1.children)
            for c in or1.children:
                appendToLeaves(c, or2.children)
            for c in or2.children:
                appendToLeaves(c, oldor1_children)
            or1.children.extend(or2.children)


    elif isinstance(root, Or):
        if isinstance(root.subs[0], Or) and isinstance(root.subs[1], Cell):
            or1 = root.subs[0]
            v = root.subs[1]
            # 1
            root.children.extend(or1.children)
            root.children.append(v)
        elif isinstance(root.subs[0], Cell) and isinstance(root.subs[1], Or):
            v = root.subs[0]
            or1 = root.subs[1]
            # 1
            root.children.extend(or1.children)
            root.children.append(v)
        elif isinstance(root.subs[0], Or) and isinstance(root.subs[1], Or):
            or1 = root.subs[0]
            or2 = root.subs[1]
            root.children.extend(or1.children)
            root.children.extend(or2.children)
        elif isinstance(root.subs[0], Cell) and isinstance(root.subs[1], Cell):
            v1 = root.subs[0]
            v2 = root.subs[1]
            root.children.extend([v1, v2])
    else:
        raise Exception
    # print(type(root.children))
    if end:
        return end

def print_tree(root, prefix=''):
    print('-' + prefix + str(root.rep))
    for c in root.children:
        print_tree(c, prefix+'--')
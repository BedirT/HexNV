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

def changeTheCorrespondingChild(target ,old, new):
    if isinstance(target, Root):
        return new 
    if target.left == old:
        target.left = new
    elif target.right == old:
        target.right = new
    else:
        raise Exception
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

    parseStrategyTree(root.left)
    parseStrategyTree(root.right)

    end = None

    if isinstance(root, And):
        # Both branches are Cell objects
        if isinstance(root.left, Cell) and isinstance(root.right, Cell):
            # Find the smaller branch - To Do
            v1 = root.left
            v2 = root.right
            # 2
            # print(type(root.parent))
            v2.parent = root.parent
            root.parent.children.append(v2)
            # 4
            appendToLeaves(v2, [v1])

            end = changeTheCorrespondingChild(root.parent, root, v2)
            root = v2
        elif isinstance(root.left, Or) and isinstance(root.right, Cell):
            or1 = root.left
            v = root.right
            
            v.parent = root.parent
            root.parent.children.append(v)
            v.children.extend(or1.children)
            end = changeTheCorrespondingChild(root.parent, root, v)

            root = v
        elif isinstance(root.left, Cell) and isinstance(root.right, Or):
            v = root.left
            or1 = root.right
            
            v.parent = root.parent
            root.parent.children.append(v)
            v.children.extend(or1.children)
            end = changeTheCorrespondingChild(root.parent, root, v)

            root = v
        elif isinstance(root.left, Or) and isinstance(root.right, Or):
            # CHANGE NEEDED AFTER OR-ROOT
            or1 = root.left
            or2 = root.right

            # 1
            or1.parent = root.parent
            root.parent.children.append(or1)
            end = changeTheCorrespondingChild(root.parent, root, or1)
            # 2
            for c in or1.children:
                appendToLeaves(c, or2.children)
    elif isinstance(root, Or):
        if isinstance(root.left, Or) and isinstance(root.right, Cell):
            or1 = root.left
            v = root.right
            # 1
            root.children.extend(or1.children)
            root.children.append(v)
        elif isinstance(root.left, Cell) and isinstance(root.right, Or):
            v = root.left
            or1 = root.right
            # 1
            root.children.extend(or1.children)
            root.children.append(v)
        elif isinstance(root.left, Or) and isinstance(root.right, Or):
            or1 = root.left
            or2 = root.right
            root.children.extend(or1.children)
            root.children.extend(or2.children)
        elif isinstance(root.left, Cell) and isinstance(root.right, Cell):
            v1 = root.left
            v2 = root.right
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
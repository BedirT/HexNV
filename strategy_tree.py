from expressions import And
from expressions import Or
from expressions import Cell
from expressions import Root

def appendToLeaves(leaves, root):
    if leaves.children.isempty():
        leaves.children = root
        return
    for child in leaves.children:
        appendToLeaves(child, root)

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
    print(root.rep)
    
    if isinstance(root, Cell):
        return

    parseStrategyTree(root.left)
    parseStrategyTree(root.right)

    if isinstance(root, And):
        # Both branches are Cell objects
        if isinstance(root.left, Cell) and isinstance(root.right, Cell):
            # Find the smaller branch - To Do
            v1 = root.left
            v2 = root.right
            # 2
            v2.parent = root.parent
            root.parent.children.append(v2)
            # 3
            v2.children.append(v1)
            # 4
            appendToLeaves(v1, v2)
        elif isinstance(root.left, Or) and isinstance(root.right, Cell):
            Or1 = root.left
            v = root.right
            
            v.parent = root.parent
            root.parent.children.append(v)
            v.children.extend([Or1.left, Or1.right])
        elif isinstance(root.left, Cell) and isinstance(root.right, Or):
            v = root.left
            Or1 = root.right
            
            v.parent = root.parent
            root.parent.children.append(v)
            v.children.extend([Or1.left, Or1.right])
        elif isinstance(root.left, Or) and isinstance(root.right, Or):
            or1 = root.left
            or2 = root.right
            # 1
            or1.parent = root.parent
            root.parent.children.append(or1)
            # 2
            or1.left.children.extend([or2.left, or2.right])
            or1.right.children.extend([or2.left, or2.right])
    elif isinstance(root, Or):
        pass
    else:
        raise Exception
    if isinstance(root.parent, Root):
        return root

def print_tree(root, prefix=''):
    print('-' + prefix + str(root.rep))
    for c in root.children:
        print_tree(c, prefix+'--')
from expressions import And
from expressions import Or
from expressions import Cell

from exp_tree import ExpTree

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
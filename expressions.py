class Exp:
    # Parent class for each expression
    pass

class And(Exp):
    def __init__(self):
        self.right = None
        self.left = None
        self.parent = None
        self.val = self.rep = 'and'
        self.children = []
        
    def __str__(self):
        return '(' + str(self.left) + '+' + str(self.right) + ')'

class Or(Exp):
    def __init__(self):
        self.right = None
        self.left = None
        self.parent = None
        self.val = self.rep = 'or'
        self.children = []
        
    def __str__(self):
        return '(' + str(self.left) + ',' + str(self.right) + ')'
    
class Cell(Exp):
    def __init__(self, val):
        self.parent = None
        self.rep = val
        self.val = [ord(val[0])-ord('a'), int(val[1:])-1]
        self.children = []
    
    def __str__(self):
        return self.rep

class TrueCell(Exp):
    def __init__(self):
        self.parent = None
        self.children = []
        self.rep = self.val = 'True'

class Root(Exp):
    def __init__(self, the_root):
        self.children = [the_root]
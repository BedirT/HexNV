class Exp:
    # Parent class for each expression
    pass

class And(Exp):
    def __init__(self):
        self.right = None
        self.left = None
        self.val = self.rep = 'and'

    def __str__(self):
        return '(' + str(self.left) + '+' + str(self.right) + ')'

class Or(Exp):
    def __init__(self):
        self.right = None
        self.left = None
        self.val = self.rep = 'or'
        
    def __str__(self):
        return '(' + str(self.left) + ',' + str(self.right) + ')'
    
class Cell(Exp):
    def __init__(self, val):
        self.right = None
        self.left = None
        self.rep = val
        self.val = [ord(val[0])-ord('a'), int(val[1:])-1]
    
    def __str__(self):
        return self.rep

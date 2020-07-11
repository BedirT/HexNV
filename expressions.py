class Exp:
    # Parent class for each expression
    pass

class And(Exp):
    def __init__(self):
        self.right = ''
        self.left = ''
        self.val = 'And'

    def __str__(self):
        return '(' + str(self.left) + '+' + str(self.right) + ')'

class Or(Exp):
    def __init__(self):
        self.right = ''
        self.left = ''
        self.val = 'Or'

    def __str__(self):
        return '(' + str(self.left) + ',' + str(self.right) + ')'
    
class Cell(Exp):
    def __init__(self, val):
        self.val = val
    
    def __str__(self):
        return self.val

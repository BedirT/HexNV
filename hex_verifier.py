import re

def print_tree(root, prefix=''):
    print('-' + prefix + str(root.val))
    for child in root.childs:
        print_tree(child, prefix+'--')

class Exp:
    # Parent class for each expression
    pass

class And(Exp):
    def __init__(self):
        self.right = ''
        self.left = ''

    def __str__(self):
        return '(' + str(self.left) + '+' + str(self.right) + ')'

    def tree(self, exstra):
        return exstra + 'AND\n' + exstra + self.right.tree('--' + exstra) + '\n' + exstra + self.right.tree('--' + exstra) + '\n'

class Or(Exp):
    def __init__(self):
        self.right = ''
        self.left = ''

    def __str__(self):
        return '(' + str(self.left) + ',' + str(self.right) + ')'
    
    def tree(self, exstra):
        return exstra + 'OR\n' + exstra + self.right.tree('--' + exstra) + '\n' + exstra + self.right.tree('--' + exstra) + '\n'

class Cell(Exp):
    def __init__(self, val):
        self.val = val
    
    def __str__(self):
        return self.val

    def tree(self, exstra):
        return exstra + self.val + '\n'

exp = '''
a4 {    b2 {b1,c1} {a3,b3},
        c2 {c1,d1} {b3, c3{b4,c4}},
        c2 {c1,d1} {b3, a3{b2, a2{a1,b1}}},
        c2 {c1,d1} {c3{b4,c4}, a3{b2, a2{a1,b1}}}}
'''

exp = 'a3 {a1, a4} {a3, a2}'

pattern = re.compile(r'[a-d{},][1-4]?')
matches = pattern.finditer(exp)

ls = [i.group() for i in matches]
# print(ls)

# 1 - Converting exp to postfix
the_queue = [] 
the_stack = []

last_exp = None
for exp in ls:
    if exp == '{':
        # create the object depending on the prev exp
        if last_exp != ',':
            # means it was and before the bracket
            _obj = And()
        else:
            # means it was or before 
            _obj = Or()
        the_stack.append(_obj)
        the_stack.append('{')
    elif exp == '}':
        while the_stack[-1] != '{':
            the_queue.append(the_stack.pop())
        the_stack.pop()
    elif exp == ',':
        # create obj
        _obj = Or()
        the_stack.append(_obj)
    else:
        # create the object for it
        _obj = Cell(exp)
        # push the cell to the queue
        the_queue.append(_obj)
    last_exp = exp
while len(the_stack) > 0:
    the_queue.append(the_stack.pop())

# TEST
print('Postfix =', [str(a) for a in the_queue])

# 2.1 Using postfix exp to parse exp tree
the_stack = []
for exp in the_queue:
    if type(exp) is Cell:
        the_stack.append(exp)
    else:
        exp.left = the_stack.pop()
        exp.right = the_stack.pop()
        the_stack.append(exp)

root = the_stack[0]

# TEST
print(root)

# 3 - Determine Next Move
# a3
# --a4
# ----b3
# ----b2
# ------c1
# ------c2
# --b4
# root.val = a3

# 4 - Determine Completeness
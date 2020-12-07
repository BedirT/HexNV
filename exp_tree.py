import re

from expressions import And
from expressions import Or
from expressions import Cell
from expressions import Root

class ExpTree:
    def __init__(self, exp):
        self.root = self._parse_exp(exp)

    def print_tree(self, root=None, prefix=''):
        if root is None:
            root = self.root
        print('-' + prefix + str(root.rep))
        try:
            self.print_tree(root.subs[0], prefix+'--')
        except:
            pass
        try:
            self.print_tree(root.subs[1], prefix+'--') 
        except:
            pass

    def _parse_exp(self, exp):
        pattern = re.compile(r'[a-d{},][1-4]?')
        matches = pattern.finditer(exp)

        ls = [i.group() for i in matches]

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
                if last_exp == '}':
                    the_queue.append(the_stack.pop())
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

        # 2.1 Using postfix exp to parse exp tree
        the_stack = []
        for exp in the_queue:
            if isinstance(exp, Cell):
                the_stack.append(exp)
            else:
                exp.subs[0] = the_stack.pop()
                exp.subs[0].parent = exp
                exp.subs[1] = the_stack.pop()
                exp.subs[1].parent = exp
                the_stack.append(exp)

        the_stack[0].parent = Root(the_stack[0])

        return the_stack[0] # returning the root
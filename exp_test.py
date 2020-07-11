from exp_tree import ExpTree

exp = '''
a4 {    b2 {b1,c1} {a3,b3},
        c2 {c1,d1} {b3, c3{b4,c4}},
        c2 {c1,d1} {b3, a3{b2, a2{a1,b1}}},
        c2 {c1,d1} {c3{b4,c4}, a3{b2, a2{a1,b1}}}}
'''
# exp = 'a3 {a1, a4} {a3, a2}'

the_tree = ExpTree(exp)
root = the_tree.root
print(root)
the_tree.print_tree()
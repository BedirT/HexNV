from exp_tree import ExpTree
from strategy_tree import parseStrategyTree, print_tree

if __name__ == "__main__":
#     exp = '''
#     a4 {    b2 {b1,c1} {a3,b3},
#             c2 {c1,d1} {b3, c3{b4,c4}},
#             c2 {c1,d1} {b3, a3{b2, a2{a1,b1}}},
#             c2 {c1,d1} {c3{b4,c4}, a3{b2, a2{a1,b1}}}}
#     '''
    # exp = 'a3 {a1, a4} {a3, a2}'
    # exp = 'a1 {a2, a3} {b1, b2} {b3, c1} {c2, c3}'
    # exp = 'a1 {b1{d1, a3, d2}} {c2 {d2, a2}}'
    exp = 'a3 {a1, a4}'

    the_tree = ExpTree(exp)
    root = the_tree.root
    # print(root)
    the_tree.print_tree()
    root = parseStrategyTree(root)
    print_tree(root)
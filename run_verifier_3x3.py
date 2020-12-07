'''
New verifier try;

This time I will have the board fixed to 3x3. Will have the moves precalculated,
after play whatever we have in the list of strategies in a linear form instead of
recursion like we did before.
'''

from hex import HexBoard
from actor import RandomAgent, RuleAgent
from strategy_tree import print_tree

agentColors = ['W','B'] # Black is always the first player


def play_game(actor1, actor2, score, num_not_complete):
        # Reset
        cur = 0
        last_move = None
        move_seq = []
        move_seq_2 = []
        not_complete = False
        game = HexBoard()
        marked = []

        while game.check_game_status() not in agentColors:
            
            if cur % 2 == 0:
                color = agentColors[0]
                
                pos_moves = actor1.moves(game.BOARD, last_move)
                # if marked:
                #     game.printBoard()
                #     print("pos moves", [i.val for i in pos_moves])
                #     print("marked", [i.val for i in marked])
                pos_=[]
                for i in pos_moves:
                    if i.val in game.valid_moves:
                        if i not in marked:
                            pos_.append(i)
               
                pos_moves = pos_
                # if marked:
                #     print("pos moves 2", [i.val for i in pos_moves])
                if not pos_moves:
                    if not move_seq:
                        not_complete = True
                    else:
                        # Rewind the move and try again
                        marked.append(move_seq[-1])
                        # print("mov_seq", [i.val for i in move_seq])

                        game.rewind(move_seq[-1].val)
                        game.rewind(move_seq_2[-1])

                        ### add if initial move is wrong
                        move_seq.pop()
                        move_seq_2.pop()

                        if move_seq:
                            last_move = move_seq[-1]
                        else:
                            last_move = None
                        continue

                else:
                    for i, cell in enumerate(pos_moves):
                        action = cell.val
                        last_move = cell
                    move_seq.append(cell)
                    game.step(color, action)
                
            else:
                color, action = agentColors[1], actor2.step(game.BOARD)
                move_seq_2.append(action)
                game.step(color, action)
            cur += 1

        # Results 
        if not_complete:
            num_not_complete += 1
        elif game.check_game_status() == 'W':
            score['W'] += 1
        elif game.check_game_status() == 'B':
            score['B'] += 1
        
    

if __name__ == "__main__":
    num_of_games = 10 ** 5
    score = {'W':0, 'B':0}
    num_not_complete = 0

    # exp = 'b2 {a1, b1} {b3, c3}'
    # exp = 'a3 {a2 {a1, b1}, c1 {b2, c2 {b3, c3}}}'
    exp = 'a1 {a2 {a3, b3}, c3 {b2, c2 {b1, c1}}}'
    # exp = 'a3 {a2 {a1, b1}, c1}'

    actor1 = RuleAgent(agentColors[0], exp)
    actor2 = RandomAgent(agentColors[1])

    print_tree(actor1.root)

    for _ in range(num_of_games):
        # print(score['W'], score['B'])
        play_game(actor1, actor2, score, num_not_complete)
        
    print('White wins: ', score['W'])
    print('Black wins: ', score['B'])
    print('Number of incomplete: ', num_not_complete)

    

        
        


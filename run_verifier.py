'''
This file is the main runner. We are checking if the given sequence
is winning strategy or not. If not, we are giving out all the sequences
that fails to be replied.

The logic;
- We have a strategy tree for the RuleAgent 'X'. X is playing as given in
the tree. 
- The verifier gives every possible response to the given move.
- On this point there are four things that could happen:
    - The game results in win for X, meaning that the branch can be closed.
    (Happens before verifier gives any response)
    - The game continues with the next branch on the strategy tree.
    - The game results in a loss for X, meaning that given strategy has a
    loosing sequence, so we give the prompt and end game state to the user.
    - The game continues but there is no more moves left on the strategy given,
    meaning the given strategy is incomplete. We prompt that to the user.
'''

from hex import HexBoard
from actor import RuleAgent
from strategy_tree import print_tree

import copy

agentColors = ['B', 'W'] # Black is always RuleAgent - FIx

losses = []
incompletes = []

def print_customBoards(boards, board_size):
    for i in boards:
        for j in range(len(i)):
            print(" "*(board_size-j), end="")
            for x in i[j]:
                print(x, end=" ")
            print()
        print()

def unique_elements(given_list):
    new_list = []
    uq_set = set()

    for item in given_list:
        s = ''.join(str(v) for v in item)
        if s not in uq_set:
            uq_set.add(s)
            new_list.append(item)
        else:
            pass
    return new_list

def loss_reached(game):
    '''
    :: Call if game state is a loss

    Gives the prompt if the game state is a loss
    '''
    losses.append(game.BOARD)

def not_complete(game):
    '''
    :: Call if game state is incomplete

    Gives the prompt if the game state is incomplete
    '''
    incompletes.append(game.BOARD)

def play_game(game_x, player, last_move):
    '''
    game_x: game to evaluate
    player: the player to evaluate the game for - [0, 1]
    last_move: the last move made on the given game   

    Evaluates the given game state for the given player, and
    makes the next move, or gives the result.
    '''
    game = copy.deepcopy(game_x)    # We need a deep copy of the game, so
                                    # we don't edit the original game
                                    # (Necessary for recursion)
    game_stat = game.check_game_status()
    
    if game_stat != '=':  
        if game_stat != agentColors[0]:
            # loss
            loss_reached(game)
            return
        # strategy branch won
        return
    if player % 2 == 0:
        pos_moves = actor.moves(game.BOARD, last_move)
        pos_moves = [u for u in pos_moves if u.val in game.valid_moves]

        if not pos_moves:
            # Since no more move left and yet we still didn't win
            # this is an incomplete sequence
            not_complete(game)
            return
        for i, cell in enumerate(pos_moves):
            action = cell.val
            game.step(agentColors[0], action)
            play_game(game, 1, cell)
            if i != len(pos_moves)-1:
                game.rewind(action)
    else:
        # for each possible action play it
        pos_moves = copy.deepcopy(game.valid_moves)
        for i, action in enumerate(pos_moves):
            game.step(agentColors[1], action)
            play_game(game, 0, last_move)
            if i != len(pos_moves)-1:
                game.rewind(action)


if __name__ == '__main__':
    # exp = 'a1 {a2 {a3, b3} b2 {b3, c3}}'
    # 3x3 winning strgs
    exp = 'b2 {a1, b1} {b3, c3}'
    # exp = 'a3{a2 {a1, b1}, c1{b2, c2{b3, c3}}}'
    # exp = 'a2{a1, b1}{a3, c2{b2, c1}{b3, c3}}'

    actor = RuleAgent('B', exp)
    counter = {'W':0, 'B':0}
    # print_tree(actor.root)
    board_size = [3, 3]

    game = HexBoard(board_size) # initial game - empty board

    play_game(game, 0, None)

    print('loss:', len(unique_elements(losses)))
    print('incomplete:', len(unique_elements(incompletes)))

    
    if not losses and not incompletes:
        print("Entered sequence is a winning strategy!")
    else:
        print("Losing games")
        losses = unique_elements(losses)
        print_customBoards(losses, board_size[0])

        print("Incomplete games")
        incompletes = unique_elements(incompletes)
        print_customBoards(incompletes, board_size[0])
    
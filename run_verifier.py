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

import copy

verified = True
agentColors = ['B', 'W'] # Black is always RuleAgent - FIx

def loss_reached(game):
    print("\n------\nEntered expression has a losing sequence.\
                \nHere is the game it lost:")
    game.printBoard()
    global verified
    verified = False

def not_complete(game):
    print(  "\n????\nEntered expression is not complete. \
            \nHere is the game it has no answer to:")
    # game.printBoard()
    global verified 
    verified = False

def win_reached(game):
    print("\n+++++Branch won!+++++\n")
    game.printBoard()

def play_game(game_x, player, last_move):
    game = copy.deepcopy(game_x)
    game_stat = game.check_game_status()
    if game_stat != '=':  
        if game_stat != agentColors[0]:
            # loss
            loss_reached(game)
            return
        # strategy branch won
        win_reached(game)
        return
    if player % 2 == 0:
        moved = False
        pos_moves = actor.moves(game.BOARD, last_move)
        if not pos_moves:
            # Since no more move left and yet we still didn't win
            # this is a losing sequence
            not_complete(game)
            # play_game(game, 1, last_move)
            return
        for cell in pos_moves:
            action = cell.val
            # Check if the action is possible on the given board
            if action in game.valid_moves:  
                moved = True
                game.step(agentColors[0], action)
                play_game(game, 1, cell)
                # game.rewind(action)
        if not moved:
            not_complete(game)
            return
    else:
        for action in game.valid_moves:
            game.step(agentColors[1], action)
            play_game(game, 0, last_move)
            # game.rewind(action)
        # for each possible action play it


if __name__ == '__main__':
    # exp = 'a1 {a2 {a3, b3} b2 {b3, c3}}'
    # 3x3 winning strgs
    exp = 'b2 {b1, c1} {a3, b3}'
    # exp = 'a3{ a2{a1, b1}, c1{b2, c2{b3, c3}}}'
    # exp = 'a2{a1, b1}{a3, c2{b2, c1}{b3, c3}}'
    actor = RuleAgent('B', exp)
    counter = {'W':0, 'B':0}

    board_size = [3, 3]

    game = HexBoard(board_size) # initial game - empty board

    play_game(game, 0, None)

    if verified:
        print("Entered sequence is a winning strategy!")
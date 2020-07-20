from hex import HexBoard
from actor import RuleAgent

import copy

verified = True
agentColors = ['B', 'W'] # Black is always RuleAgent - FIx

def loss_reached(game):
    print("Entered expression has a losing sequence.\
                \nHere is the game it lost:")
    game.printBoard()
    global verified
    verified = False

def not_complete(game):
    print(  "Entered expression is not complete. \
            \nHere is the game it has no answer to:")
    game.printBoard()
    global verified 
    verified = False

def win_reached(game):
    print("Branch won!")
    game.printBoard()

def play_game(game_x, player, last_move):
    game = copy.copy(game_x)
    # print(id(game))
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
        if len(pos_moves) == 0:
            # Since no more move left and yet we still didn't win
            # this is a losing sequence
            play_game(game, 1, last_move)
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
    exp = 'a1 {b1, b2}'
    actor = RuleAgent('B', exp)
    counter = {'W':0, 'B':0}

    board_size = [2, 2]

    game = HexBoard(board_size) # initial game - empty board

    play_game(game, 0, None)

    if verified:
        print("Entered sequence is a winning strategy!")
from hex import HexBoard
from actor import RuleAgent

verified = True
agentColors = ['B', 'W'] # Black is always RuleAgent - FIx

def loss_reached():
    print("Entered expression has a losing sequence. (Not Complete)\
                \nHere is the game it lost:")
    game.printBoard()
    verified = False

def play_game(game, player, last_move):
    
    game_stat = game.check_game_status()
    if game_stat != '=':
        if game_stat != agentColors[0]:
            # loss
            loss_reached()
            return
        # strategy branch won
        return
    if player % 2 == 0:
        pos_moves = actor.moves(game.BOARD, last_move)
        if pos_moves is None:
            # Since no more move left and yet we still didn't win
            # this is a loosing sequence
            loss_reached()
            return
        for cell in pos_moves:
            action = cell.val
            # Check if the action is possible on the given board
            if action in game.valid_moves:  
                game.step(agentColors[0], action)
                play_game(game, (player+1)%2, cell)
    else:
        for action in game.valid_moves:
            game.step(agentColors[1], action)
            play_game(game, (player+1)%2, last_move)
        # for each possible action play it
    game.printBoard()


if __name__ == '__main__':
    # exp = 'a1 {a2 {a3, b3} b2 {b3, c3}}'
    exp = 'a1 {a2, b2}'
    actor = RuleAgent('B', exp)
    counter = {'W':0, 'B':0}

    board_size = [2, 2]

    game = HexBoard(board_size) # initial game - empty board

    play_game(game, 0, None)

    if verified:
        print("Entered sequence is a winning strategy!")
from hex import HexBoard
from actor import RandomAgent

if __name__ == '__main__':
    exp = 'a1 {a2 {a3, b3} b2 {b3, c3}}'
    actors = [RandomAgent('B'), RandomAgent('W')]
    counter = {'W':0, 'B':0}

    board_size = [3, 3]
    num_of_games = 5

    for _ in range(num_of_games):
        game = HexBoard(board_size)
        for i in range(board_size[0] * board_size[1]):
            actor = actors[i % 2]
            action = actor.step(game.BOARD)
            # game.printBoard()
            info = game.step(actor.color, action)
            if info[1]:
                counter[info[2]] += 1
                break
        
    print('White wins:', counter['W'])
    print('Black wins:', counter['B'])

        
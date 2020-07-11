from hex import HexBoard
from actor import RandomAgent

if __name__ == '__main__':
    actors = [RandomAgent('W'), RandomAgent('B')]
    counter = {'W':0, 'B':0}

    size_x, size_y = 4, 4

    for _ in range(1000):
        game = HexBoard([size_x, size_y])
        for i in range(size_x * size_y):
            actor = actors[i % 2]
            action = actor.step(game.BOARD)
            # game.printBoard()
            info = game.step(actor.color, action)
            if info[1]:
                counter[info[2]] += 1
                break
        
    print('White wins:', counter['W'])
    print('Black wins:', counter['B'])

        
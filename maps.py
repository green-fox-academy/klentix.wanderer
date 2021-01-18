import random

class Map:
    def __init__(self):
        self.tiles = [
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
             [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
             [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
             [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 1, 1, 0, 0, 0]]

    def is_wall(self, x, y):
        return self.tiles[y][x] == 1


    def get_random():
        return random.randint(1, 6)
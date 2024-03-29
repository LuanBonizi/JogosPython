import pygame as pg

_ = False

mini_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,3,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,3,_,_,_,4,_,_,2,_,_,_,_,1],
    [1,_,_,3,_,_,_,4,_,_,2,_,_,_,_,1],
    [1,_,_,3,_,_,_,3,_,_,5,2,2,_,_,1],
    [1,_,_,3,_,_,_,3,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,3,_,_,_,_,_,_,_,1],
    [1,_,_,4,_,_,_,4,_,_,_,_,_,_,_,1],
    [1,1,1,3,1,3,1,1,1,3,3,3,3,1,1,1]
]

class Map:
    def __init__(self,game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i,j)] = value


import pygame as pg

# Map has 20
_ = False
mini_map = [
#    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,12,23,24,25,26,27,28,29,30,31,32,33
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, 2, 2, 2, 2, 2, 2, 2, _, 3, 3, 1, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, _, _, _, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, _, _, _, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, _, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3, 1, 3, 4, 1, _, _, _, 3, _, _, _, 1],
    [1, _, _, _, _, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4, _, _, _, 1],
    [1, _, _, _, _, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, 1],
    [1, _, _, _, _, _, _, 4, _, _, _, _, _, _, _, 5, 5, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, 1],
    [1, _, _, 3, 3, 3, 3, 4, _, _, _, _, _, _, _, 5, 5, _, _, _, _, _, _, _, 1, _, _, _, 3, _, _, _, 1],
    [1, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4, _, _, _, 4, _, _, _, 1],
    [1, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4, 3, 1, 1, 3, _, _, _, 3, _, _, _, 1],
    [1, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, 4, 3, 1, 1, 1],
    [1, _, _, 3, _, _, _, 2, 2, 2, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, 3, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 5, _, 2, _, _, 1, 1, 1, 3, 3, 4, 4, 3, 4, 4, 1, 1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 3, 1, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, _, _, _, _, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [_, _, _, _, _, _, _, _, 6, 6, 7, 8, 7, 6, _, _, _, _, 6, 7, 8, 7, 6, 6],
    [_, _, _, _, _, _, _, _, 6, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 6],
    [_, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7],
    [_, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7],
    [_, _, _, _, _, _, _, _, 8, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 8],
    [_, _, _, _, _, _, _, _, 8, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 8],
    [_, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7],
    [_, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7],
    [_, _, _, _, _, _, _, _, 6, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 6],
    [_, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7],
    [_, _, _, _, _, _, _, _, 8, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 8],
    [_, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7],
    [_, _, _, _, _, _, _, _, 7, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 7],
    [_, _, _, _, _, _, _, _, 6, 6, 6, 6, 7, 7, 8, 6, 6, 8, 7, 7, 6, 6, 6, 6],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
        
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
    
    def draw(self):
        for y, row in enumerate(self.mini_map):
            for x, wall_id in enumerate(row):
                if wall_id:
                    texture = self.game.object_renderer.wall_textures[wall_id]
                    self.game.screen.blit(texture, (x * 100, y * 100))
        
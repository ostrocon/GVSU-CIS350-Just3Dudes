import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
    
    def draw(self):
        self.render_game_objects()
    
    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key = lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)
        
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        return {
<<<<<<< Updated upstream
            1: self.get_texture('src/cis350doom/resources/textures/1.png'),
            2: self.get_texture('src/cis350doom/resources/textures/2.png'),
            3: self.get_texture('src/cis350doom/resources/textures/3.png'),
            4: self.get_texture('src/cis350doom/resources/textures/4.png'),
            5: self.get_texture('src/cis350doom/resources/textures/5.png'),
=======
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
            4: self.get_texture('resources/textures/4.png'),
            5: self.get_texture('resources/textures/5.png'),
>>>>>>> Stashed changes
        }
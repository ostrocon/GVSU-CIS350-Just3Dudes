import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

        self.blood_screen = self.get_texture('src/cis350doom/resources/textures/blood_screen.png', RES)
        self.digit_size = 90
        self.digit_images = [self.get_texture(f'src/cis350doom/resources/textures/digits/{i}.png', [self.digit_size] * 2)
                             for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))

        self.game_over_image = self.get_texture('src/cis350doom/resources/textures/game_over.png', RES)

    def draw(self):
        self.render_game_objects()
        self.draw_player_health()

    def game_over(self):
        self.screen.blit(self.game_over_image,(0,0))

    def draw_player_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size, 0))
        self.screen.blit(self.digits['10'], ((i +1) * self.digit_size, 0))

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0,0))
    
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
            1: self.get_texture('src/cis350doom/resources/textures/1.png'),
            2: self.get_texture('src/cis350doom/resources/textures/2.png'),
            3: self.get_texture('src/cis350doom/resources/textures/3.png'),
            4: self.get_texture('src/cis350doom/resources/textures/4.png'),
            5: self.get_texture('src/cis350doom/resources/textures/5.png'),
        }
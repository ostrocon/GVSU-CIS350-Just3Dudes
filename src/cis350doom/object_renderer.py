import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('src/cis350doom/resources/textures/hellsky.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        
        self.blood_screen = self.get_texture('src/cis350doom/resources/textures/blood_screen.png', RES)
        self.digit_size = 90
        self.digit_images = [self.get_texture(f'src/cis350doom/resources/textures/digits/{i}.png', [self.digit_size] * 2)
                             for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))

        self.game_over_image = self.get_texture('src/cis350doom/resources/textures/game_over.png', RES)
        self.game_win_image = self.get_texture('src/cis350doom/resources/textures/winscreen.png', RES)
    
    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()
        
    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        #floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def game_over(self, score, won):
        self.screen.blit(self.game_over_image,(0,0))
        if not won:
            score_text = "SCORE: " + str(score)
            font = pg.font.Font(None, 55)  # You can adjust the font size here

            # Create a surface with the "SCORE: " text
            text_surface = font.render(score_text, True, (255, 215, 0))  # Color can be adjusted as needed

            # Calculate the position to center the text horizontally and shift it downward
            text_width, text_height = text_surface.get_size()
            text_x = (WIDTH - text_width) // 2 + 50
            text_y = (HEIGHT - text_height) // 2 + 200  # Shifted downward by 50 pixels

            # Blit the "SCORE: " text onto the screen
            self.screen.blit(text_surface, (text_x, text_y))
            
    def win_game(self, score, won):
        self.screen.blit(self.game_win_image,(0,0))
        if won:
            self.draw_player_score(score)
        
    def draw_player_score(self, score):
        score_text = "SCORE: " + str(score)
        font = pg.font.Font(None, 55)  # You can adjust the font size here

        # Create a surface with the "SCORE: " text
        text_surface = font.render(score_text, True, (255, 215, 0))  # Color can be adjusted as needed

        # Calculate the position to center the text horizontally and shift it downward
        text_width, text_height = text_surface.get_size()
        text_x = (WIDTH - text_width) // 2
        text_y = (HEIGHT - text_height) // 2 + 150  # Shifted downward by 50 pixels

        # Blit the "SCORE: " text onto the screen
        self.screen.blit(text_surface, (text_x, text_y))

        font = pg.font.Font(None, 36)
        text = font.render("Score: 5", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        self.screen.blit(text, text_rect)

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
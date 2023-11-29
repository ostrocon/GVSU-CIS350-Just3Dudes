import pygame as pg
import sys
from pygame import gfxdraw
from random import randint

WIN_SIZE = WIDTH, HEIGHT = 1200, 800
STEPS_BETWEEN_COLORS = 9
COLORS = ['black', 'red', 'orange', 'yellow', 'white']
PIXEL_SIZE = 4

FIRE_REPS = 4
FIRE_WIDTH = WIDTH // (PIXEL_SIZE * FIRE_REPS)
FIRE_HEIGHT = HEIGHT // PIXEL_SIZE


class DoomFire:
    def __init__(self, app):
        self.app = app
        self.palette = self.get_palette()
        self.fire_array = self.get_fire_array()
        self.fire_surf = pg.Surface([PIXEL_SIZE * FIRE_WIDTH, HEIGHT])
        self.fire_surf.set_colorkey('black')

        self.logo = pg.image.load('src/cis350doom/resources/textures/doom_logo.png').convert_alpha()
        self.logo = pg.transform.scale2x(self.logo)
        self.logo_x, self.logo_y = (WIDTH // 2 - self.logo.get_width() // 2,
                                    HEIGHT // 3 - self.logo.get_height() // 2)
        self.logo_start_y = HEIGHT

    def draw_logo(self):
        #track initail position of logo 
        pg.init()
        if self.logo_start_y > self.logo_y:
            #moves logo up
            self.logo_start_y -= 5
        self.app.screen.blit(self.logo, (self.logo_x, self.logo_start_y))

        
        # Add a message below the logo
        font = pg.font.Font(None, 36)
        message = font.render("Press the UP arrow to START", True, (255, 255, 255))

        # Adjust the message position based on the current logo position
        message_rect = message.get_rect(center=(WIDTH // 2, self.logo_start_y + self.logo.get_height() + 30))
        self.app.screen.blit(message, message_rect)

    def do_fire(self):
        #iterate over fire array and skip index 0, assign the next value above to be the next color
        for x in range(FIRE_WIDTH):
            for y in range(1, FIRE_HEIGHT):
                color_index = self.fire_array[y][x]
                if color_index:
                    #gives fire a random "burning" look
                    rnd = randint(0, 3)
                    #fire can "spread" left and right
                    self.fire_array[y - 1][(x - rnd + 1) % FIRE_WIDTH] = color_index - rnd % 2
                else:
                    #if a zero color (black) appears than no other color will spread for it...helps with frame rate
                    self.fire_array[y - 1][x] = 0

    def draw_fire(self):
        self.fire_surf.fill('black')
        #iterate over all thegiven colors
        for y, row in enumerate(self.fire_array):
            for x, color_index in enumerate(row):
                if color_index:
                    color = self.palette[color_index]
                    #imported to help draw fire particles 
                    gfxdraw.box(self.fire_surf, (x * PIXEL_SIZE, y * PIXEL_SIZE,
                                                  PIXEL_SIZE, PIXEL_SIZE), color)

        #also used to help with frame rate
        #"splits" fire into 4 parts of the same visual and displays them together on screen
        for i in range(FIRE_REPS):
            self.app.screen.blit(self.fire_surf, (self.fire_surf.get_width() * i, 0))

    def get_fire_array(self):
        #iterate over the color array to get a white row which represents the source
        #2D array for fire on screen both left to right and bottom up to a certain point on screen
        fire_array = [[0 for i in range(FIRE_WIDTH)] for j in range(FIRE_HEIGHT)]
        for i in range(FIRE_WIDTH):
            fire_array[FIRE_HEIGHT - 1][i] = len(self.palette) - 1
        return fire_array

    def draw_palette(self):
        size = 90
        for i, color in enumerate(self.palette):
            pg.draw.rect(self.app.screen, color, (i * size, HEIGHT // 2, size - 5, size - 5))

    @staticmethod
    def get_palette():
        palette = [(0, 0, 0)]
        #get the values of each color step
        for i, color in enumerate(COLORS[:-1]):
            c1, c2 = color, COLORS[i + 1]
            for step in range(STEPS_BETWEEN_COLORS):
                #linear interpretation (.lerp) for shading
                c = pg.Color(c1).lerp(c2, (step + 0.5) / STEPS_BETWEEN_COLORS)
                palette.append(c)
        return palette

    def update(self):
        self.do_fire()

    def draw(self):
        
        #self.draw_palette()
        self.draw_fire()
        self.draw_logo()


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(size=WIN_SIZE)
        self.clock = pg.time.Clock()
        self.doom_fire = DoomFire(self)

    def update(self):
        self.doom_fire.update()
        self.clock.tick(60)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        self.doom_fire.draw()
        pg.display.flip()

    def run(self):
        while True:     
            for event in pg.event.get():
                if event.type == pg.KEYUP:
                    return False
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()
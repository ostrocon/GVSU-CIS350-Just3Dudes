# from sprite_object import *

# class Weapon(AnimatedSprite):
#     def __init__(self, game, path, scale=0.4, animation_time=90):
#         super().__init__(game=game,path=path,scale=scale,animation_time=animation_time)
#         self.images = deque (
#             [pg.transform.smoothscale(img , (self.image.get_width() * scale, self.image.get_height() * scale))
#              for img in self.images])
#         self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
#         self.reloading = False
#         self.num_images = len(self.images)
#         self.frame_counter = 0
#         self.damage = 50

#     def animate_shot(self):
#           if self.reloading:
#                 self.game.player.shot = False
#                 if self.animation_tigger:
#                       self.images.rotate(-1)
#                       self.image = self.images[0]
#                       self.frame_counter += 1
#                       if  self.frame_counter == self.num_images:
#                             self.reloading = False
#                             self.frame_counter = 0

#     def draw(self):
#             self.game.screen.blit(self.images[0], self.weapon_pos)

#     def update(self):
#             self.check_animation_time()
#             self.animate_shot()

# class Shotgun(Weapon):
#     def __init__(self, game):
#         super().__init__(game=game,path='src/cis350doom/resources/sprites/weapon/shotgun/shotgun1.png',scale=0.4,animation_time=90)
#         self.damage = 60

# class DoubleShotgun(Weapon):
#     def __init__(self, game):
#         super().__init__(game=game,path='src/cis350doom/resources/sprites/weapon/doubleshotgun/shotgun1.png',scale=0.4,animation_time=90)
#         self.damage = 100

# class Pistol(Weapon):
#     def __init__(self, game):
#         super().__init__(game=game,path='src/cis350doom/resources/sprites/weapon/pistol/pistol1.png',scale=0.4,animation_time=90)
#         self.damage = 30

from sprite_object import *

class Weapon(AnimatedSprite):
    def __init__(self, game, path, scale=0.4, animation_time=90):
        super().__init__(game=game,path=path,scale=scale,animation_time=animation_time)
        self.images = deque (
            [pg.transform.smoothscale(img , (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 50
        self.shot_counter = 0 # Test
        self.max_shots = 0 # Test

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_tigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if  self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
            self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
            self.check_animation_time()
            self.animate_shot()

class Shotgun(Weapon):
    def __init__(self, game):
        super().__init__(game=game,path='src/cis350doom/resources/sprites/weapon/shotgun/shotgun1.png',scale=0.4,animation_time=90)
        self.damage = 60

class DoubleShotgun(Weapon):
    def __init__(self, game):
        super().__init__(game=game,path='src/cis350doom/resources/sprites/weapon/doubleshotgun/shotgun1.png',scale=0.4,animation_time=90)
        self.damage = 100
        self.shot_counter = 0
        self.max_shots = 2
        self.reload_images = self.get_images('src/cis350doom/resources/sprites/weapon/shotgun/shotgun1.png')
    
    def animate_shot(self):
        if self.reloading:
            if self.shot_counter >= self.max_shots:
                self.images = self.reload_images
                self.game.player.shot = False
                if self.animation_tigger:
                    self.images.rotate(-1)
                    self.image = self.images[0]
                    self.frame_counter += 1
                    if  self.frame_counter == self.num_images:
                        self.shot_counter += 1
                        self.reloading = False
                        self.frame_counter = 0
            else:
                self.game.player.shot = False
                if self.animation_tigger:
                    self.images.rotate(-1)
                    self.image = self.images[0]
                    self.frame_counter += 1
                    if  self.frame_counter == self.num_images:
                        self.shot_counter += 1
                        self.reloading = False
                        self.frame_counter = 0

class Pistol(Weapon):
    def __init__(self, game):
        super().__init__(game=game,path='src/cis350doom/resources/sprites/weapon/pistol/pistol1.png',scale=0.4,animation_time=90)
        self.damage = 30
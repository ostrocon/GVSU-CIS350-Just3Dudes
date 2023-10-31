from sprite_object import *

class ObjectHandler:
    def __init__(self,game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'src/cis350doom/resources/sprites/static_sprites'
        self.anim_sprite_path = 'src/cis350doom/resources/sprites/animated_sprites'
        add_sprite = self.add_sprite

        #sprite map
        add_sprite(SpriteObject(game, pos=(1.5,7.5)))
        add_sprite(SpriteObject(game, pos=(4, 8)))
        add_sprite(SpriteObject(game, pos=(8, 4)))
        add_sprite(AnimatedSprite(game, pos=(3,9)))
        add_sprite(AnimatedSprite(game, pos=(1,6)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + '/red_light/0.png', pos=(6,6)))


    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
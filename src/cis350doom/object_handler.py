from sprite_object import *
from npc import *

class ObjectHandler:
    def __init__(self,game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'src/cis350doom/resources/sprites/npc'
        self.static_sprite_path = 'src/cis350doom/resources/sprites/static_sprites'
        self.anim_sprite_path = 'src/cis350doom/resources/sprites/animated_sprites'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        #sprite map
        # add_sprite(SpriteObject(game, pos=(1.5,7.5)))
        # add_sprite(SpriteObject(game, pos=(4, 8)))
        # add_sprite(SpriteObject(game, pos=(8, 4)))
        # add_sprite(AnimatedSprite(game, pos=(3,9)))
        # add_sprite(AnimatedSprite(game, pos=(1,6)))
        # add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + '/red_light/0.png', pos=(6,6)))

        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game,pos=(1.5,1.5)))
        add_sprite(AnimatedSprite(game,pos=(1.5,7.5)))
        add_sprite(AnimatedSprite(game,pos=(5.5,4.75)))
        add_sprite(AnimatedSprite(game,pos=(7.5,2.5)))
        add_sprite(AnimatedSprite(game,pos=(7.5,5.5)))
        add_sprite(AnimatedSprite(game,pos=(14.5,1.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + '/red_light/0.png', pos=(14.5,7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + '/red_light/0.png', pos=(12.5,7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + '/red_light/0.png', pos=(9.5,7.5)))

        #npc map
        add_npc(NPC(game))
        add_npc(NPC(game, pos=(11.5,4.5)))


    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]


    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self,npc):
        self.npc_list.append(npc)
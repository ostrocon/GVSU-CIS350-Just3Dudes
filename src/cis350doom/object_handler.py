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

        # Sprite map
        # add_sprite(SpriteObject(game))
        # add_sprite(AnimatedSprite(game))
        
        # Animated Green Light Sprites
        add_sprite(GreenLight(game,pos=(5.5,3.3)))
        add_sprite(GreenLight(game,pos=(5.5,4.7)))
        add_sprite(GreenLight(game,pos=(2.8,2.5)))
        add_sprite(GreenLight(game,pos=(2.8,5.5)))
        add_sprite(GreenLight(game,pos=(2.8,10.3)))
        add_sprite(GreenLight(game,pos=(2.8,14.7)))
        
        # Animated Red Light Sprites
        add_sprite(RedLight(game, pos=(1.15,1.15)))
        add_sprite(RedLight(game, pos=(1.15,18.85)))
        add_sprite(RedLight(game, pos=(31.85,1.15)))
        add_sprite(RedLight(game, pos=(31.85,18.85)))

        
        # Static Candle Sprites
        add_sprite(Candle(game,pos=(17.15,8.85)))
        add_sprite(Candle(game,pos=(14.85,8.85)))
        add_sprite(Candle(game,pos=(17.15,11.15)))
        add_sprite(Candle(game,pos=(14.85,11.15)))

        # Npc map
        add_npc(CyberDemon(game, pos=(16.5,28.5)))
        # add_npc(CyberDemon(game, pos=(11.5,4.5)))
        # add_npc(CyberDemon(game, pos=(11.5,4.5)))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]


    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self,npc):
        self.npc_list.append(npc)
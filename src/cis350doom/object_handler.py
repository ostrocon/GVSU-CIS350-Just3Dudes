from sprite_object import *
from npc import *
import random
from pathfinding import *

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

        # Animated Fire Barrel Sprite
        add_sprite(FireBarrel(game, pos=(0, 0)))
        
        # Static Candle Sprites
        add_sprite(Candle(game,pos=(17.15,8.85)))
        add_sprite(Candle(game,pos=(14.85,8.85)))
        add_sprite(Candle(game,pos=(17.15,11.15)))
        add_sprite(Candle(game,pos=(14.85,11.15)))

        # Static Fire Barrel Sprites
        add_sprite(FireBarrel(game, pos=(12.6, 30.8)))
        add_sprite(FireBarrel(game, pos=(21, 31)))
        add_sprite(FireBarrel(game, pos=(15, 25.7)))
        add_sprite(FireBarrel(game, pos=(19, 21.8)))
        add_sprite(FireBarrel(game, pos=(13, 21.8)))

        # Static guy-on-stick Sprites
        add_sprite(StickGuy(game, pos=(0, 0)))

        # Static heads-on-stick Sprites
        add_sprite(HeadStick(game, pos=(22, 22)))
        add_sprite(HeadStick(game, pos=(17, 26)))
        add_sprite(HeadStick(game, pos=(12, 29)))

        # Static Tree-related Sprites
        add_sprite(Tree(game,pos=(21, 21)))
        add_sprite(Tree(game,pos=(19, 31)))
        add_sprite(Tree(game,pos=(11, 30)))
        add_sprite(Tree(game,pos=(12, 23)))
        add_sprite(Tree(game,pos=(16, 25)))

        # Places GraySpikes, BrownSpikes, and BrokenTrees
        columns = range(9, 23)
        rows = range(19,33)
        interval = 2.0

        for x in columns:
            for y in rows:
                if random.random() < 0.2:
                    pos = (x + 0.5 + random.uniform(-0.3, 0.3), y + 0.5 + random.uniform(-0.3, 0.3))
                    rand = random.random()
                    if  0 < rand < 0.4:
                        add_sprite(GraySpike(game, pos=pos))
                    elif 0.4 < rand < 0.8:
                        add_sprite(BrownSpike(game, pos=pos))
                    else:
                        add_sprite(BrokenTree(game, pos=pos))
            y += interval

        # Places StickGuys, HeadSticks, and HeadPiles
        columns1 = range(1, 8)
        rows1 = range(19,33)
        interval1 = 1.0

        for x in columns1:
            for y in rows1:
                if random.random() < 0.2:
                    pos = (x + 0.5 + random.uniform(-0.3, 0.3), y + 0.5 + random.uniform(-0.3, 0.3))
                    rand = random.random()
                    if 0 < rand < 0.3:
                        add_sprite(StickGuy(game, pos=pos))
                    elif 0.3 < rand < 0.6:
                        add_sprite(HeadStick(game, pos=pos))
                    else:
                        add_sprite(HeadPile(game, pos=pos))
            y += interval1
        
        # Npc map
        # add_npc(Soldier(game, pos=(12,10)))
        add_npc(Guy(game, pos=(3, 26)))
        # add_npc(Guy(game, pos=(11.5,4.5)))
        add_npc(Soldier(game, pos=(11.5,4.5)))
        add_npc(CacoDemon(game,pos=(11,3.5)))
        
        add_npc(CacoDemon(game,pos=(12,12)))
        add_npc(CyberDemon(game,pos=(13,12)))
        add_npc(Soldier(game,pos=(14,12)))
        add_npc(CacoDemon(game,pos=(15,12)))


        add_npc(CacoDemon(game,pos=(11,28)))
        add_npc(CacoDemon(game,pos=(12,28)))
        add_npc(CacoDemon(game,pos=(13,28)))
        add_npc(CacoDemon(game,pos=(14,28)))
        add_npc(CyberDemon(game,pos=(15,28)))
        add_npc(CyberDemon(game,pos=(16,28)))
        add_npc(CacoDemon(game,pos=(17,28)))
        add_npc(CacoDemon(game,pos=(18,28)))
        add_npc(CacoDemon(game,pos=(19,28)))
        add_npc(CacoDemon(game,pos=(20,28)))
        
        add_npc(Soldier(game, pos=(31,8.2)))
        add_npc(Soldier(game, pos=(31,9.5)))
        add_npc(CacoDemon(game, pos=(31,6.5)))
        add_npc(CacoDemon(game, pos=(30.3,8.5)))
        add_npc(Soldier(game, pos=(30.3,8.5)))
        
        # Gun Sprites
        add_sprite(DoubleShotgunSprite(game,pos=(3,3.3)))
        add_sprite(ShotgunSprite(game,pos=(3,6.3)))
        add_sprite(PistolSprite(game,pos=(3,9.3)))
        add_sprite(AutoShotgunSprite(game,pos=(3,7.3)))
    
    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.remove_picked_health_packs()
        self.score()
    
    def remove_picked_health_packs(self):
        health_packs = [sprite for sprite in self.sprite_list if isinstance(sprite, HealthPack) and not sprite.is_active]
        for pack in health_packs:
            if pack.picked_up:
                self.sprite_list.remove(pack)
        
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self,npc):
        self.npc_list.append(npc)
    
    def score(self):
        points = 0
        enemies_killed = 0
        for enemy in self.npc_list:
            if isinstance(enemy, Soldier) and not enemy.alive:
                points += 10
                enemies_killed += 1
            elif isinstance(enemy, CacoDemon) and not enemy.alive:
                points += 15
                enemies_killed += 1
            elif isinstance(enemy, CyberDemon) and not enemy.alive:
                points += 40
                enemies_killed += 1
            elif isinstance(enemy, Guy) and not enemy.alive:
                points += 80
                enemies_killed += 1
            if enemies_killed == len(self.npc_list):
                pg.time.delay(100)
                print(points)
                return True, points
        return False, points
    
    def get_health_packs(self):
        return [sprite for sprite in self.sprite_list if isinstance(sprite, HealthPack)]
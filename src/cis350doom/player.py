from settings import *
import pygame as pg
from sprite_object import*
import math
from weapon import *

class Player:
    def __init__(self, game):
        self.game = game
        self.current_weapon_sprite = None
        self.weapon_pickup_cooldown = False
        self.weapon_pickup_cooldown_duration = 2000  # 2 seconds in milliseconds
        self.weapon_pickup_cooldown_timer = 0
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shot = False
        self.rel = 0
        
        #Comment out from here to line 27 to stop health regen
        self.health = PLAYER_MAX_HEALTH
        self.health_recovery_delay = 700
        self.time_prev = pg.time.get_ticks()
        self.diag_move_corr = 1/math.sqrt(2)

    def recover_health(self):
        if self.check_health_recovery_delay() and self.health < PLAYER_MAX_HEALTH:
            self.health += 1

    def check_health_recovery_delay(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            return True
    #Comment out above here to line 14 to stop health regen

    def check_game_over(self):
        won, score = self.game.object_handler.score()
        if self.health < 1 and not won:
            self.game.object_renderer.game_over(score, won)
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()
    
    def check_for_win(self):
        won, score = self.game.object_handler.score()
        if won:
            self.game.object_renderer.win_game(score, won)
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def get_damge(self, damage):
        self.health -= damage
        self.game.object_renderer.player_damage()
        self.game.sound.player_pain.play()
        self.check_game_over()

    def single_fire_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloading = True
        
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        num_key_pressed = -1
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            num_key_pressed += 1
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            num_key_pressed += 1
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            num_key_pressed += 1
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            num_key_pressed += 1
            dx += -speed_sin
            dy += speed_cos
            
        if num_key_pressed:
            dx *= self.diag_move_corr
            dy *= self.diag_move_corr

        self.check_wall_collision(dx, dy)
        
        # if keys[pg.K_LEFT]:
        #     self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        # if keys[pg.K_RIGHT]:
        #     self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau
        
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def heal(self, amount):
        self.health += amount
        if self.health > PLAYER_MAX_HEALTH:
            self.health = PLAYER_MAX_HEALTH
            
    def check_health_pack_collision(self):
        for item in self.game.object_handler.sprite_list:
            if isinstance(item, HealthPack) and item.is_active:
                distance = ((self.x - item.x) ** 2 + (self.y - item.y) ** 2) ** 0.5
                if distance < 1:  # Adjust this threshold as needed
                    self.pickup_health_pack(item)

    def pickup_health_pack(self, health_pack):
        if health_pack.is_active:
            self.heal(int(self.health * .2))
            health_pack.is_active = False
            # Remove the health pack from the sprite list
            if health_pack in self.game.object_handler.sprite_list:
                self.game.object_handler.sprite_list.remove(health_pack)

    def check_weapon_collision(self):
        for item in self.game.object_handler.sprite_list:
            if isinstance(item, ShotgunSprite) and item.is_active:
                distance = ((self.x - item.x) ** 2 + (self.y - item.y) ** 2) ** 0.5
                if distance < 0.5 and not self.weapon_pickup_cooldown:  # Adjust this threshold as needed
                    self.pickup_weapon(item)
                    self.weapon_pickup_cooldown = True
                    self.weapon_pickup_cooldown_timer = pg.time.get_ticks()

            elif isinstance(item, DoubleShotgunSprite) and item.is_active:
                distance = ((self.x - item.x) ** 2 + (self.y - item.y) ** 2) ** 0.5
                if distance < 0.5 and not self.weapon_pickup_cooldown:  # Adjust this threshold as needed
                    self.pickup_weapon(item)
                    self.weapon_pickup_cooldown = True
                    self.weapon_pickup_cooldown_timer = pg.time.get_ticks()
            
            elif isinstance(item, PistolSprite) and item.is_active:
                distance = ((self.x - item.x) ** 2 + (self.y - item.y) ** 2) ** 0.5
                if distance < 0.5 and not self.weapon_pickup_cooldown:  # Adjust this threshold as needed
                    self.pickup_weapon(item)
                    self.weapon_pickup_cooldown = True
                    self.weapon_pickup_cooldown_timer = pg.time.get_ticks()

            elif isinstance(item, AutoShotgunSprite) and item.is_active:
                distance = ((self.x - item.x) ** 2 + (self.y - item.y) ** 2) ** 0.5
                if distance < 0.5 and not self.weapon_pickup_cooldown:  # Adjust this threshold as needed
                    self.pickup_weapon(item)
                    self.weapon_pickup_cooldown = True
                    self.weapon_pickup_cooldown_timer = pg.time.get_ticks()
    
    def pickup_weapon(self, weapon):
        if weapon.is_active:
            previous_weapon = self.game.weapon
            weapon.is_active = False

            # Swap weapons between player and ground sprite
            if isinstance(weapon, ShotgunSprite):
                self.game.weapon = Shotgun(self.game)
            elif isinstance(weapon, DoubleShotgunSprite):
                self.game.weapon = DoubleShotgun(self.game)
            elif isinstance(weapon, PistolSprite):
                self.game.weapon = Pistol(self.game)
            elif isinstance(weapon, AutoShotgunSprite):
                self.game.weapon = AutoShotgun(self.game)

            # Remove the picked-up weapon sprite from the sprite list
            if weapon in self.game.object_handler.sprite_list:
                self.game.object_handler.sprite_list.remove(weapon)

            # Create the ground sprite for the player's previous weapon and add it to the sprite list
            if isinstance(previous_weapon, Shotgun):
                previous_weapon_sprite = ShotgunSprite(game=self.game, pos=(weapon.x, weapon.y))
            elif isinstance(previous_weapon, DoubleShotgun):
                previous_weapon_sprite = DoubleShotgunSprite(game=self.game, pos=(weapon.x, weapon.y))
            elif isinstance(previous_weapon, Pistol):
                previous_weapon_sprite = PistolSprite(game=self.game, pos=(weapon.x, weapon.y))
            elif isinstance(previous_weapon, AutoShotgun):
                previous_weapon_sprite = AutoShotgunSprite(game=self.game, pos=(weapon.x, weapon.y))

            self.game.object_handler.add_sprite(previous_weapon_sprite)

    def draw(self):
        # pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
        #             (self.x * 100 + WIDTH * math.cos(self.angle),
        #              self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT or my < MOUSE_BORDER_TOP or my > MOUSE_BORDER_BOTTOM:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time
    
    def update(self):
        self.movement()
        self.mouse_control()
        self.recover_health()
        self.check_health_pack_collision()
        self.check_weapon_collision()
        self.check_for_win()
        if self.weapon_pickup_cooldown:
            current_time = pg.time.get_ticks()
            if current_time - self.weapon_pickup_cooldown_timer >= self.weapon_pickup_cooldown_duration:
                self.weapon_pickup_cooldown = False
        
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
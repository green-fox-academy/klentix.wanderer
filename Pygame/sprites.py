import pygame as pg
from settings import *
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'wanderer_img')

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0,0
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder,'wall.gif')).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Floor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.floor
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder,'hefloor.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
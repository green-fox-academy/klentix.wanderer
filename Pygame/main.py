import pygame as pg
import sys
from os import path
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'wanderer_img')
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)
        self.player_img = pg.image.load(path.join(img_folder,HERO)).convert_alpha()
        self.player_imgup = pg.image.load(path.join(img_folder,'hero-up.gif')).convert_alpha()
        self.player_imgleft = pg.image.load(path.join(img_folder,'hero-left.gif')).convert_alpha()
        self.player_imgright = pg.image.load(path.join(img_folder, 'hero-right.gif')).convert_alpha()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        # create a wall group to hold it
        self.walls = pg.sprite.Group()
        self.floor = pg.sprite.Group()
        #self.player = Player(self,50,50)
        # to read from a map file
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    # when see 1 = create a wall
                    Wall(self, col, row)
                #if tile == 'P':
                #    self.player = Player(self, col, row)
                if tile == '.' or tile == 'P':
                    Floor(self,col,row)
        self.player = Player(self,1,1) #starting position of the player

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'wanderer_img')
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
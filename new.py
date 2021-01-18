from tkinter import *
from maps import Map
from sprites import Hero,Skeleton,Boss
import random

size = 720

root = Tk()
root.title ('My Wanderer Game')
root.configure(background ='grey')
canvas = Canvas(root, width=size, height=size)
canvas.pack()

class Game():
    def __init__(self,width = 720, height= 720):
        self.width = width
        self.height = height

        # for the status bar
        self._stats = Canvas(root, width=self.width, height="32")
        self._stats.pack()
        self.rect = None

        # import floor and wall images
        self.floor_image = PhotoImage(file='wanderer_img/thefloor.gif')
        self.wall_image = PhotoImage(file='wanderer_img/wall.gif')
        self.map = Map()
        self.draw_map(self.map.tiles)


    def draw_map(self, map):
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 0:
                    image = self.floor_image
                else:
                    image = self.wall_image
                canvas.create_image(j * 72, i * 72, anchor=NW, image=image)



    def stats(self,hero): # to display status
        self._stats.delete("all")
        text_display = f"Hero (Level: {hero.level}) HP: {int(hero.HP)}/38 | DP: {hero.DP} | SP: {hero.SP}"
        self._stats.create_rectangle(0, 0, 600,20,fill = "black")
        self._stats.create_text(10, 10, text=text_display , font=('arial', 11), anchor=NW)
        self._stats.pack()

class Sprite():
    def __init__(self):

        # importing images of hero , skeleton and boss
        self.hero_down = PhotoImage(file='wanderer_img/hero-down.gif')
        self.hero_up = PhotoImage(file='wanderer_img/hero-up.gif')
        self.hero_left = PhotoImage(file='wanderer_img/hero-left.gif')
        self.hero_right = PhotoImage(file='wanderer_img/hero-right.gif')
        self.skeleton_image = PhotoImage(file='wanderer_img/skeleton.gif')
        self.boss_image = PhotoImage(file='wanderer_img/boss.gif')
        self.pos_x = 0 # position
        self.pos_y = 0 # position

    def hero_draw(self): # draw hero
        self.hero = canvas.create_image(36, 36, image=self.hero_down)

    def move(self, dx, dy): # when hero moves
        canvas.move(self.hero, dx * 72, dy * 72)

    def enemy_one(self): # draw enemy no.1
        self.enemy_one = canvas.create_image(9 * 72 + 36, 9 * 72 + 36, image=self.skeleton_image)

    def enemy_two(self): # draw enemy no.2
        self.enemy_one = canvas.create_image(2 * 72 + 36, 1 * 72 + 36, image=self.skeleton_image)

    def enemy_three(self): # draw enemy no.2
        self.enemy_one = canvas.create_image(4 * 72 + 36, 3 * 72 + 36, image=self.skeleton_image)

    def boss(self): # draw boss
        self.boss = canvas.create_image(5 * 72 + 36 , 0 * 72 + 36, image=self.boss_image)


def on_key_press(e): # function when pressing a key
    try:
        # print(e.keycode) : tracking which number for keycode
        # when clicking Up Arrow
        if e.keycode == 38:
            if not myapp.map.is_wall(hero.pos_x, hero.pos_y - 1) and hero.pos_y > 0:
                hero.move(0, -1)
                canvas.itemconfig(hero.hero, image=hero.hero_up)
                hero.pos_y -= 1

        # when clicking Down Arrow
        elif e.keycode == 40:
            if not myapp.map.is_wall(hero.pos_x, hero.pos_y + 1) and hero.pos_y < 9:
                hero.move(0, 1)
                canvas.itemconfig(hero.hero, image=hero.hero_down)
                hero.pos_y += 1

        # when clicking Left Arrow
        elif e.keycode == 37:
            if not myapp.map.is_wall(hero.pos_x - 1, hero.pos_y) and hero.pos_x > 0:
                hero.move(-1, 0)
                canvas.itemconfig(hero.hero, image=hero.hero_left)
                hero.pos_x -= 1

        # when clicking Right Arrow
        elif e.keycode == 39:
            if not myapp.map.is_wall(hero.pos_x + 1, hero.pos_y) and hero.pos_x < 9:
                hero.move(1, 0)
                canvas.itemconfig(hero.hero, image=hero.hero_right)
                hero.pos_x += 1
    except IndexError:
        pass

    # when clicking Esc Button
    if e.keycode == 27:  # esc button
        root.destroy()



#binding key press event
root.bind("<KeyPress>", on_key_press)
canvas.pack()



myapp = Game()
hero = Sprite()
hero.hero_draw()
enemy_one = Sprite()
enemy_one.enemy_one()
enemy_two = Sprite()
enemy_two.enemy_two()
enemy_three = Sprite()
enemy_three.enemy_three()
boss = Sprite()
boss.boss()


canvas.focus_set()
root.mainloop()
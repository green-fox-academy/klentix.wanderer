from tkinter import *
from maps import Map

class Hero():
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x * 60
        self.y = y * 60
        # self.image = image
        self.HP = 20 + 3 * Map.get_random()
        self.maxHP = 38
        self.DP = 2 * Map.get_random()
        self.SP = 5 + Map.get_random()
        self.level = 1

    def get_position(self):
        return self.x, self.y

    def get_level(self,level):
        self.level = level

    def get_HP(self,HP):
        self.HP = HP

    def get_DP(self,DP):
        self.DP = DP

    def get_SP(self,SP):
        self.SP = SP


class Skeleton(Hero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.HP = 2 * self.level * Map.get_random()
        self.DP = self.level / 2 * Map.get_random()
        self.SP = self.level * Map.get_random()

class Boss(Hero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.HP = 2 * self.level * Map.get_random() + Map.get_random()
        self.DP = self.level / 2 * Map.get_random() +Map.get_random()/2
        self.SP = self.level * Map.get_random() + self.level


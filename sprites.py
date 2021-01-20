from tkinter import *
from maps import Map


class Hero():
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x * 60
        self.y = y * 60
        # self.image = image
        self.HP = 20 + 3 * Map.get_D6()  # health point
        self.DP = 2 * Map.get_D6()       # defend point
        self.SP = 5 + Map.get_D6()       # strike point
        self.level = 1                   # current level status

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

    def level_up(self): # when hero levels up
        self.level += 1
        self.HP += Map.get_D6()
        self.DP += Map.get_D6()
        self.SP += Map.get_D6()

    def strike(self,enemy): # when hero strikes
        if isinstance(self,Hero):
            strike_value = self.SP + Map.get_D6()
            if ((2 * Map.get_D6() + strike_value)) > enemy.DP:
                enemy.HP -= strike_value - enemy.DP
        else:
            strike_value = enemy.strike_value + Map.get_D6()
            if ((2* Map.get_D6() + strike_value)) > self.DP:
                self.HP -= strike_value - self.DP

    def battle(self,enemy):
        if self.HP and enemy.HP > 0:
            self.strike(enemy)
            enemy.strike(self)
        else:
            if isinstance(self,Hero) and enemy.HP < self.HP:
                self.HP += Map.get_D6()
                self.DP += Map.get_D6()
                self.SP += Map.get_D6()
                return enemy
            else:
                print ("You died")


class Skeleton(Hero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.HP = 2 * self.level * Map.get_D6()
        self.DP = self.level / 2 * Map.get_D6()
        self.SP = self.level * Map.get_D6()

class Boss(Hero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.HP = 2 * self.level * Map.get_D6() + Map.get_D6()
        self.DP = self.level / 2 * Map.get_D6() + Map.get_D6()/2
        self.SP = self.level * Map.get_D6() + self.level


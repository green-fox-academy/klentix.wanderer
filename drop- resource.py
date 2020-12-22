import tkinter
from PIL import ImageTk,Image,ImageFile
import os

class Resource:
#create empty list for coordinate arrays to be append to:

    def __init__(self):
        self.images = {}
        self.images["floor"] = self.load_image(Image.open("Pygame/wanderer_img/floor.png"))
        self.images["wall"] = self.load_image(Image.open("Pygame/wanderer_img/wall.png"))
        self.images["herodown"] = self.load_image(Image.open("Pygame/wanderer_img/hero-down.png"))
        self.images["heroleft"] = self.load_image(Image.open("Pygame/wanderer_img/hero-left.png"))
        self.images["heroright"] = self.load_image(Image.open("Pygame/wanderer_img/hero-right.png"))
        self.images["heroup"] = self.load_image(Image.open("Pygame/wanderer_img/hero-up.png"))
        self.images["skeleton"] = self.load_image(Image.open("Pygame/wanderer_img/skeleton.png"))
        self.images["boss"] = self.load_image(Image.open("Pygame/wanderer_img/boss.png"))
# #choose image:
# img =  ImageTk.PhotoImage(Image.open("wanderer_img/floor.png"))
# panel = tkinter.Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = 'yes')
# root.mainloop()

    def load_image(self,path):
        img = ImageTk.PhotoImage(file=path)
        return img

    def get_image(self,key):
        return self.images[key]
from tkinter import *
from resource import Resource
from grid import Grid

# class Box(object):
#     def __init__(self):
#         self.testBoxX = 300
#         self.testBoxY = 300
#
#     def draw(self, canvas):
#         canvas.create_rectangle(0, 0, 600, 600, fill='white')
#         canvas.create_rectangle(self.testBoxX, self.testBoxY, self.testBoxX+100, self.testBoxY+100, fill='lime green')

# Create the tk environment as usual
image_size = 40
board_szie = 20
root = Tk()
canvas = Canvas(root, width=image_size*board_szie, height=image_size*board_szie)

# Creating a box that can draw itself in a certain position
#box = Box()
resource = Resource()
grid = Grid(board_szie)

# Create a function that can be called when a key pressing happens
def on_mouse_click(e):
    #print('Pressed')
    #print(e.keycode)
    print(e.x,e.y)
    #38 up, 40 down, 39 right, 37 left
    # When the keycode is 38 (up arrow) we move the position of our box higher
    # if e.keycode == 38:
    #     box.testBoxY = box.testBoxY - 100
    # elif e.keycode == 40:
    #     box.testBoxY = box.testBoxY + 100
    # and lower if the key that was pressed the down arrow
    # draw the box again in the new position
    # box.draw(canvas)

# Tell the canvas that we prepared a function that can deal with the key press events
canvas.bind("<ButtonRelease>", on_mouse_click)
canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()

# Draw the box in the initial position
box.draw(canvas)

root.mainloop()
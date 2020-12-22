#skeleton of the game
import pygame
import random

width = 800
height = 800
fps = 30

#define colors:
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#initialize pygame and create window
pygame.init ()
pygame.mixer.init() #enter sound
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("My Wanderer Game")
clock =  pygame.time.Clock()

#command create a group with all sprites
all_sprites = pygame.sprite.Group()
#game loop
running = True
while running:
    # keep loop running at right speed
    clock.tick(fps)
    # Process input (events: using keyboard, mouse, etc)
    for event in pygame.event.get():
        #check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()

    # Draw / Render
    screen.fill(black)
    all_sprites.draw(screen)
    
    # after drawing everything, flip the display
    # every time it moves, we wont have to draw again so we do double buffering
    pygame.display.flip()

pygame.quit()
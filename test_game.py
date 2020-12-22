# 1. Import library
import pygame
from pygame.locals import *

# 2. Initialize the game
pygame.init()
width, height = 720, 720
screen = pygame.display.set_mode((width,height))

player_up = False
player_down= False
player_left = False
player_right = False
player_x = 1
player_y = 1
playerpos = [1,1]
player_speed = 1

# 3. Load images
player = pygame.image.load(r'C:\Users\Cheryl L\Documents\greenfox\klentix.wanderer\Pygame\wanderer_img\hero-down.png')
floor = pygame.image.load(r'C:\Users\Cheryl L\Documents\greenfox\klentix.wanderer\Pygame\wanderer_img\hefloor.png')
wall = pygame.image.load(r'C:\Users\Cheryl L\Documents\greenfox\klentix.wanderer\Pygame\wanderer_img\wall.png')

# 4. Keep looping
running = 1
while running == 1:
    # 5. clear the screen before drawing it again:
    for x in range (int(width/floor.get_width()+1)):
        for y in range(int(height/floor.get_height()+1)):
            screen.blit(floor,(x*72,y*72))
    #screen.blit(floor,(100,100))
    screen.blit(player,(player_x,player_y))
    screen.blit(wall,(3*72,0*72))
    screen.blit(wall,(3*72,1*72))
    screen.blit(wall, (3 * 72, 2 * 72))
    screen.blit(wall, (2 * 72, 2 * 72))
    screen.blit(wall, (1 * 72, 2 * 72))
    #group 2
    screen.blit(wall, (3 * 72, 4 * 72))
    screen.blit(wall, (3 * 72, 5 * 72))
    screen.blit(wall, (3 * 72, 6 * 72))
    screen.blit(wall, (2 * 72, 4 * 72))
    screen.blit(wall, (1 * 72, 4 * 72))
    screen.blit(wall, (1 * 72, 5 * 72))
    screen.blit(wall, (1 * 72, 6 * 72))
    screen.blit(wall, (0 * 72, 4 * 72))
    #group 3
    screen.blit(wall, (1 * 72, 8 * 72))
    screen.blit(wall, (2 * 72, 8 * 72))
    screen.blit(wall, (3 * 72, 8 * 72))
    screen.blit(wall, (3 * 72, 9 * 72))
    #group 4
    screen.blit(wall, (5 * 72, 1 * 72))
    screen.blit(wall, (5 * 72, 2 * 72))
    screen.blit(wall, (5 * 72, 3 * 72))
    screen.blit(wall, (5 * 72, 4 * 72))
    screen.blit(wall, (6 * 72, 4 * 72))
    screen.blit(wall, (7 * 72, 4 * 72))
    screen.blit(wall, (8 * 72, 4 * 72))
    #group 5
    screen.blit(wall, (7 * 72, 1 * 72))
    screen.blit(wall, (8 * 72, 1 * 72))
    screen.blit(wall, (7 * 72, 2 * 72))
    screen.blit(wall, (8 * 72, 2 * 72))
    #group 6
    screen.blit(wall, (5 * 72, 6 * 72))
    screen.blit(wall, (5 * 72, 7 * 72))
    screen.blit(wall, (6 * 72, 6 * 72))
    screen.blit(wall, (6 * 72, 7 * 72))
    #GROUP 7
    screen.blit(wall, (5 * 72, 9 * 72))
    screen.blit(wall, (6 * 72, 9 * 72))
    #GROUP 8
    screen.blit(wall, (8 * 72, 6 * 72))
    screen.blit(wall, (8 * 72, 7 * 72))
    screen.blit(wall, (8 * 72, 8 * 72))
    # 7. update the screen
    pygame.display.update()


    # 8. loop through the event:
    for event in pygame.event.get():
        #check if the event is the X button:
        if event.type == pygame.QUIT:
            # if it is then quit game:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                player_up = True
            elif event.key == K_a:
                player_left = True
            elif event.key == K_s:
                player_down  = True
            elif event.key == K_d:
                player_right = True

        if event.type == KEYUP:
            if event.key == K_w:
                player_up = False
            elif event.key == K_a:
                player_left = False
            elif event.key == K_s:
                player_down = False
            elif event.key == K_d:
                player_right = False

    # 9. Move player:
    if player_up == True:
        player_y -= player_speed
    elif player_down:
        player_y += player_speed
    if player_left == True:
        player_x -= player_speed
    elif player_right:
        player_x += player_speed


#import modules
import pygame, sys
import random

#import some useful constants
from pygame.locals import *

#import classes
from .world import World

#constants
FPS = 10
TILESIZE = 40
MAP_WIDTH = 10
MAP_HEIGHT = 10

#colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
fpsClock  =pygame.time.Clock()

#images
AGENT  = pygame.image.load('agent.bmp')
FOOD = pygame.image.load('food.bmp')

#set up display
DISPLAYSURF = pygame.display.set_mode((MAP_WIDTH*TILESIZE,MAP_HEIGHT*TILESIZE))
pygame.display.set_caption('tilemap')

#world loop
while True:
    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(BLACK)
    for row in range(MAP_HEIGHT):
        for column in range(MAP_WIDTH):
            #add a white square (drawing surface, colour, coords)
            #the last parameter sets the border
            pygame.draw.rect(DISPLAYSURF, WHITE, (column*TILESIZE, row*TILESIZE, TILESIZE,TILESIZE), 1)
    #update the display
    fpsClock.tick(FPS)
    pygame.display.update()
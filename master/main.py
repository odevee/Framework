#import modules
import pygame, sys, random

#import some useful constants
from pygame.locals import *

#import classes
from master.entity import Entity
from master.world import World
from master.entityType import EntityType
from master.agent import Agent
from master.food import Food
from master.obstacle import Obstacle
from master.goal import Goal

#constants
FPS = 10
TILESIZE = 40
MAP_WIDTH = 10
MAP_HEIGHT = 10

#colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (200, 0, 0)
GREEN = (0,200,0)
BLUE = (0,0,200)

pygame.init()
fpsClock = pygame.time.Clock()

#images
AGENT  = pygame.image.load('agent.bmp')
FOOD = pygame.image.load('food.bmp')
GOAL = pygame.image.load('goal.bmp')
OBSTACLE = pygame.image.load('obstacle.bmp')

#set up display
DISP_SURF = pygame.display.set_mode((MAP_WIDTH*TILESIZE, MAP_HEIGHT*TILESIZE))
pygame.display.set_caption('tilemap')

#initialize world
world = World(MAP_WIDTH, MAP_HEIGHT)
world.spawn(EntityType.Agent, 5, 5)
world.spawn(EntityType.Food, 7, 7)
world.spawn(EntityType.Goal, 9, 9)
world.spawn(EntityType.Obstacle, 3, 3)

def WorldRender():
    for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
           # print("i=",i," j=", j)
            #if world.entities[i][j] != 0:
             #  print("Objekt gefunden", world.entities[i][j])
            #print(type(world.entities[i][j]))
            if type(world.entities[i][j]) is Agent:
                #print("Agent gezeichnet")
                DISP_SURF.blit(AGENT, (i * TILESIZE, j * TILESIZE))
            if type(world.entities[i][j]) is Food:
                DISP_SURF.blit(FOOD, (i * TILESIZE, j * TILESIZE))
            if type(world.entities[i][j]) is Goal:
                DISP_SURF.blit(GOAL, (i * TILESIZE, j * TILESIZE))
            if type(world.entities[i][j]) is Obstacle:
                DISP_SURF.blit(OBSTACLE, (i * TILESIZE, j * TILESIZE))

#world loop
while True:
    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISP_SURF.fill(BLACK)
    for row in range(MAP_HEIGHT):
        for column in range(MAP_WIDTH):
            #add a white square (drawing surface, colour, coords)
            #the last parameter sets the border
            pygame.draw.rect(DISP_SURF, WHITE, (column*TILESIZE, row*TILESIZE, TILESIZE,TILESIZE), 1)
    #update the display
    fpsClock.tick(FPS)
    for row in world.entities:
        for entity in row:
            if (type(entity) != type(None)):
                print(type(entity))
                print("Es ist eine Entity")
                entity.update()

    WorldRender()
    pygame.display.update()

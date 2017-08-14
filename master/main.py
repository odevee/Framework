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
images = {Agent:AGENT, Food:FOOD, Goal:GOAL, Obstacle:OBSTACLE}

#set up display
DISP_SURF = pygame.display.set_mode((MAP_WIDTH*TILESIZE, MAP_HEIGHT*TILESIZE))
pygame.display.set_caption('tilemap')

#initialize world
world = World(MAP_WIDTH, MAP_HEIGHT)
world.spawn(EntityType.Agent, 5, 5)
world.spawn(EntityType.Food, 7, 7)
world.spawn(EntityType.Goal, 8, 8)
world.spawn(EntityType.Obstacle, 0, 0)
world.spawn(EntityType.Obstacle, 0, 1)
world.spawn(EntityType.Obstacle, 0, 2)
world.spawn(EntityType.Obstacle, 0, 3)
world.spawn(EntityType.Obstacle, 0, 4)
world.spawn(EntityType.Obstacle, 0, 5)
world.spawn(EntityType.Obstacle, 0, 6)
world.spawn(EntityType.Obstacle, 0, 7)
world.spawn(EntityType.Obstacle, 0, 8)
world.spawn(EntityType.Obstacle, 0, 9)
world.spawn(EntityType.Obstacle, 9, 0)
world.spawn(EntityType.Obstacle, 9, 1)
world.spawn(EntityType.Obstacle, 9, 2)
world.spawn(EntityType.Obstacle, 9, 3)
world.spawn(EntityType.Obstacle, 9, 4)
world.spawn(EntityType.Obstacle, 9, 5)
world.spawn(EntityType.Obstacle, 9, 6)
world.spawn(EntityType.Obstacle, 9, 7)
world.spawn(EntityType.Obstacle, 9, 8)
world.spawn(EntityType.Obstacle, 9, 9)
world.spawn(EntityType.Obstacle, 1, 0)
world.spawn(EntityType.Obstacle, 2, 0)
world.spawn(EntityType.Obstacle, 3, 0)
world.spawn(EntityType.Obstacle, 4, 0)
world.spawn(EntityType.Obstacle, 5, 0)
world.spawn(EntityType.Obstacle, 6, 0)
world.spawn(EntityType.Obstacle, 7, 0)
world.spawn(EntityType.Obstacle, 8, 0)
world.spawn(EntityType.Obstacle, 1, 9)
world.spawn(EntityType.Obstacle, 2, 9)
world.spawn(EntityType.Obstacle, 3, 9)
world.spawn(EntityType.Obstacle, 4, 9)
world.spawn(EntityType.Obstacle, 5, 9)
world.spawn(EntityType.Obstacle, 6, 9)
world.spawn(EntityType.Obstacle, 7, 9)
world.spawn(EntityType.Obstacle, 8, 9)

def Render():
    for row in world.entities:
        for entity in row:
            if (type(entity) != type(None)):
                DISP_SURF.blit(images[type(entity)], (entity.x * TILESIZE, entity.y * TILESIZE))

#world loop
while True:
    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #draw grid
    DISP_SURF.fill(BLACK)
    for row in range(MAP_HEIGHT):
        for column in range(MAP_WIDTH):
            #add a white square (drawing surface, colour, coordinates)
            #the last parameter sets the border thickness
            pygame.draw.rect(DISP_SURF, WHITE, (column*TILESIZE, row*TILESIZE, TILESIZE,TILESIZE), 1)
    #update the display
    fpsClock.tick(FPS)
    world.update()
    Render()
    pygame.display.update()
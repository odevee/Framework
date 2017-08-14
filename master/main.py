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
MAP_WIDTH = 20
MAP_HEIGHT = 20

#colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (200, 0, 0)
GREEN = (0,200,0)
BLUE = (0,0,200)

#start the pygame library and create a clock module
pygame.init()
fpsClock = pygame.time.Clock()

#load the images
AGENT  = pygame.image.load('resources/agent.bmp')
FOOD = pygame.image.load('resources/food.bmp')
GOAL = pygame.image.load('resources/goal.bmp')
OBSTACLE = pygame.image.load('resources/obstacle.bmp')
#this dictionary allows to get the image for a known type
images = {Agent:AGENT, Food:FOOD, Goal:GOAL, Obstacle:OBSTACLE}

#set up display
DISP_SURF = pygame.display.set_mode((MAP_WIDTH*TILESIZE, MAP_HEIGHT*TILESIZE))
pygame.display.set_caption('World')

#draws a Border of Obstacles around the world to prevent agents from leaving it
def drawBorder():
    #top and bottom
    for x in range(MAP_WIDTH):
        world.spawn(EntityType.Obstacle, x, 0)
        world.spawn(EntityType.Obstacle, x, MAP_HEIGHT-1)
    #left and right
    for y in range(1, MAP_HEIGHT - 1):
        world.spawn(EntityType.Obstacle, 0, y)
        world.spawn(EntityType.Obstacle, MAP_WIDTH - 1, y)

#initialize world
world = World(MAP_WIDTH, MAP_HEIGHT)
drawBorder()
world.spawn(EntityType.Agent, 5, 5)
world.spawn(EntityType.Agent, 5, 6)
world.spawn(EntityType.Food, 1, 1)
world.spawn(EntityType.Goal, 1, 8)

#draws the entities onto the grid
def render():
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
            #add a white square (drawing surface, colour, coordinates, border thickness)
            pygame.draw.rect(DISP_SURF, WHITE, (column*TILESIZE, row*TILESIZE, TILESIZE,TILESIZE), 1)
    #update the display
    fpsClock.tick(FPS)
    world.update()
    render()
    pygame.display.update()
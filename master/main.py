# import modules
import pygame
import sys
import os
# import some useful constants
from pygame.locals import *

# open window at specified position
# position = (0, 0)
# os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
os.environ['SDL_VIDEO_CENTERED'] = '1'

# constants
FPS = 10
TILESIZE = 40

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)

# import classes
# ignore warnings - it works!
from classes.entity     import Entity
from classes.world      import World
from classes.entityType import EntityType
from classes.agent      import Agent
from classes.food       import Food
from classes.obstacle   import Obstacle
from classes.goal       import Goal

# start the pygame library and create a clock module
pygame.init()
fpsClock = pygame.time.Clock()

# load the images
AGENT = pygame.image.load('resources/agent.bmp')
FOOD = pygame.image.load('resources/food.bmp')
GOAL = pygame.image.load('resources/goal.bmp')
OBSTACLE = pygame.image.load('resources/obstacle.bmp')
# this dictionary allows searching for the pertinent image by type
images = {Agent: AGENT, Food: FOOD, Goal: GOAL, Obstacle: OBSTACLE}

# draws a Border of Obstacles around the world to prevent agents from leaving it
# def drawBorder():
#     #top and bottom
#     for x in range(MAP_WIDTH):
#         world.spawn(EntityType.Obstacle, x, 0)
#         world.spawn(EntityType.Obstacle, x, MAP_HEIGHT-1)
#     #left and right
#     for y in range(1, MAP_HEIGHT - 1):
#         world.spawn(EntityType.Obstacle, 0, y)
#         world.spawn(EntityType.Obstacle, MAP_WIDTH - 1, y)

# initialize world
world = World()
world.loadMap('resources/maps/face.txt')
world.spawn(EntityType.Agent, 1, 1)

# set up display
DISP_SURF = pygame.display.set_mode((world.width * TILESIZE, world.height * TILESIZE), pygame.NOFRAME)


# draws the entities onto the grid
def render():
    for line in world.entities:
        for entity in line:
            if isinstance(entity, Entity):
                DISP_SURF.blit(images[type(entity)], (entity.x * TILESIZE, entity.y * TILESIZE))

# world loop
hold = False
while True:
    # get all the user events
    for event in pygame.event.get():
        # if the user wants to quit (ESC)
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            hold = not hold
            if hold:
                print('GAME ON HOLD')
            else:
                print('CONTINUE')
    # draw grid
    DISP_SURF.fill(BLACK)
    for row in range(world.height):
        for column in range(world.width):
            # add a white square (drawing surface, colour, coordinates, border thickness)
            pygame.draw.rect(DISP_SURF, WHITE, (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE), 1)
    # update the display
    fpsClock.tick(FPS)
    if not hold:
        world.update()
    render()
    pygame.display.update()

import pygame

DIRT = 0
STONE = 1
WATER = 2
COAL = 3
WOOD = 4
GRASS = 5
LAVA = 6

TILESIZE = 40
MAPWIDTH = 30
MAPHEIGHT = 15

WHITE = (255,255,255)
BLACK = (0,0,0)

textures = {
	DIRT : pygame.image.load('textures/dirt.png'),
	STONE : pygame.image.load('textures/stone.png'),
	WATER : pygame.image.load('textures/water.png'),
	COAL : pygame.image.load('textures/coal.png'),
	WOOD : pygame.image.load('textures/bush.png'),
	GRASS : pygame.image.load('textures/grass.png'),
	LAVA : pygame.image.load('textures/lava.png')
}

inventory = {
	DIRT : 0,
	STONE : 0,
	WATER : 0,
	COAL : 0,
	WOOD : 0,
	GRASS : 1,
	LAVA : 0
}
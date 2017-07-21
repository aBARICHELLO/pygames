import pygame, sys

from tylemap import *

from pygame.locals import *
from random import randint

pygame.init()
fpsClock = pygame.time.Clock()

#Display configs.
DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE+50))
pygame.display.set_caption('pYAMICO')
pygame.display.set_icon(pygame.image.load('textures/player.png'))

#Player initialization.
PLAYER = pygame.image.load('textures/player.png').convert_alpha()
playerPosition = [0,0]

#Fonts
INVFONT = pygame.font.SysFont('FreeSansBold', 18)

#Terrain Generation:
resources = [DIRT, STONE, WATER, COAL, WOOD, GRASS, LAVA]
tilemap = [[DIRT for w in range(MAPWIDTH)] for w in range(MAPHEIGHT)]
for row in range(MAPHEIGHT):
	for clm in range(MAPWIDTH):
		random = randint(0,30)

		if random == 0:
			tilemap[row-1][clm] = COAL
			tile = COAL
		elif random == 2 or random == 3:
			tilemap[row-1][clm-1] = WATER
			tilemap[row-1][clm-2] = WATER
			tilemap[row][clm-2] = WATER
			tilemap[row][clm-1] = WATER
			tile = WATER
		elif random == 4:
			tile = LAVA
		elif random > 4 and random <= 7:
			tile = STONE
		elif random > 7 and random <= 8:
			tilemap[row-1][clm-1] = WOOD
			tilemap[row-1][clm] = WOOD
			tilemap[row-2][clm-1] = WOOD
			tile = WOOD
		elif random > 9 and random <= 15:
			tile = DIRT
		else:
			tile = GRASS
		
		tilemap[row][clm] = tile
		tilemap[0][0] = DIRT

def checkWalkableBlock(x, y): #Needs fix
	nextX = playerPosition[1] + x
	nextY = playerPosition[0] + y
	if tilemap[nextX][nextY] == LAVA:
		return False
	else:
		return True

def checkRemovableBlock(): #Some tiles can't be removed by hand.
	currentTile = tilemap[playerPosition[1]][playerPosition[0]]
	if currentTile == LAVA or currentTile == DIRT or currentTile == WATER:
		return False
	else:
		return True

def removeBlock(material): #Swaps the blocks when using the keys for placing (1-0)
	currentTile = tilemap[playerPosition[1]][playerPosition[0]]
	if inventory[material] > 0:
		inventory[material] -= 1
		if checkRemovableBlock():
			inventory[currentTile] += 1
		tilemap[playerPosition[1]][playerPosition[0]] = material

def digAction(): #Checks performed when the user presses space
	MATERIAL = DIRT
	if currentTile == GRASS:
		inventory[DIRT] += 1
	elif currentTile == WOOD:
		inventory[WOOD] += 1
		MATERIAL = GRASS
	elif currentTile == COAL:
		inventory[COAL] += 1
		MATERIAL = STONE
	elif currentTile == WATER:
		MATERIAL = STONE
	else:
		inventory[currentTile] += 1
	tilemap[playerPosition[1]][playerPosition[0]] = MATERIAL

#def checkNearbyWater():


#Main game loop.
while True:
	#TODO pygame.key.set_repeat(1, 50)
	#Keyboard handling.
	for event in pygame.event.get():
		currentTile = tilemap[playerPosition[1]][playerPosition[0]]
		print(event) #Debug
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_w and playerPosition[1] > 0 and checkWalkableBlock(-1, 0):
				playerPosition[1] -= 1
			elif event.key == K_a and playerPosition[0] > 0 and checkWalkableBlock(0, -1):
				playerPosition[0] -= 1
			elif event.key == K_s and playerPosition[1] < MAPHEIGHT-1 and checkWalkableBlock(1, 0):
				playerPosition[1] += 1
			elif event.key == K_d and playerPosition[0] < MAPWIDTH-1 and checkWalkableBlock(0, 1):
				playerPosition[0] += 1
			elif event.key == K_SPACE: #Dig event
				if checkRemovableBlock():
					digAction()
			elif event.key == K_1:
				removeBlock(DIRT)
			elif event.key == K_2:
				removeBlock(STONE)
			elif event.key == K_3:
				removeBlock(WATER)
			elif event.key == K_4:
				removeBlock(COAL)
			elif event.key == K_5:
				removeBlock(WOOD)
			elif event.key == K_6:
				removeBlock(GRASS)
	
	#Drawing textures.
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAY.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	
	#Drawing inventory.
	placePosition = 10
	for item in resources:
		DISPLAY.blit(textures[item], (placePosition, MAPHEIGHT*TILESIZE + 20))
		placePosition += 30
		textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
		DISPLAY.blit(textObj, (placePosition, MAPHEIGHT*TILESIZE + 20))
		placePosition += 50

	#Drawing player
	DISPLAY.blit(PLAYER ,(playerPosition[0]*TILESIZE,playerPosition[1]*TILESIZE))
	pygame.display.update()
	fpsClock.tick(24)
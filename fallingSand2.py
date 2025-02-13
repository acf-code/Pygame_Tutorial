import pygame
import numpy as np
import random

pygame.init()
WIDTH, HEIGHT = 300,500
screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()
fps = 60

size = 5
rows = HEIGHT // size
cols = WIDTH // size

grid = np.zeros((cols,rows),dtype = int)

def drawGrids():
    for i in range(cols):
        for j in range(rows):
            if grid[i,j] == 1:
                pygame.draw.rect(screen,"white",(i*size,j*size,size,size))
            else:
                pygame.draw.rect(screen,"black",(i*size,j*size,size,size))
                #pygame.draw.rect(screen,"green",(i*size,j*size,size,size),width = 1)

def placeParticle():
    #check where the mPos is
    #and change the grid value to 1
    if pygame.mouse.get_pressed()[0]:
        mPos = pygame.mouse.get_pos()
        i = mPos[0] // size
        j = mPos[1] // size
        grid[i,j] = 1

def updateGrid(oldGrid):
    newGrid = np.zeros((cols,rows),dtype = int)
    for i in range(cols):
        for j in range(rows):
            if oldGrid[i,j] == 1: #there is a particle at this particular row and column
                if j + 1 < rows:
                    #first check if the row below has a particle already
                    if oldGrid[i,j+1] == 1:#this states that row directly the current particle has a particle
                        d = random.choice([-1,1])
                        if i + d >=0 and i + d < cols:
                            if oldGrid[i+d][j+1] == 0:
                                newGrid[i+d][j+1] = 1
                            else:
                                newGrid[i][j] = 1
                        else:
                            newGrid[i][j] = 1
                    else:
                        newGrid[i,j+1] = 1
                else:
                    newGrid[i,j] = 1
    return newGrid

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    placeParticle()
    screen.fill("black")
    drawGrids()
    grid = updateGrid(grid)
    pygame.display.update()
    clock.tick(60)
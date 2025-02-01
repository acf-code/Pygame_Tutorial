import pygame
import random

pygame.init()
WIDTH, HEIGHT=800, 600
screen=pygame.display.set_mode([WIDTH, HEIGHT])
clock=pygame.time.Clock()
fps=60
size=25
rows=HEIGHT//size
cols=WIDTH//size
def createGrids(size,rows,cols):
    grids=[]
    for i in range(cols):
        grids.append([])
    for i in range(cols):
        for j in range(rows):
            grid={
                 "pos":[i*size, j*size],
                "value":0
            }
            grid["rect"]=pygame.Rect(grid["pos"][0],grid["pos"][1],size,size)

            grids[i].append(grid)
    return grids
grids=createGrids(size, rows, cols)
def drawGrids(grids):
    for i in range(cols):
        for j in range(rows):
            g = grids[i][j]
            if g["value"]==1:
                pygame.draw.rect(screen, "white",g["rect"])
            if g["value"]==0:
                pygame.draw.rect(screen,"black", g["rect"])
def placeParticle(grids, mpos):
    placeWidth=10
    placeHeight=3
    startCol=0
    endCol=0
    startRow=0
    endRow=0
    for i in range(cols):
        for j in range(rows):
            g=grids[i][j]
            if g["rect"].collidepoint(mpos):
                if i-placeWidth<0:
                    startCol=0
                else:
                    startCol=i-placeWidth
                if i+placeWidth>cols-1:
                    endCol=cols-1
                else:
                    endCol=i+placeWidth
                if j - placeHeight < 0:
                    startRow= 0
                else:
                    startRow = j - placeHeight
                if j + placeHeight > rows- 1:
                    endRow = rows- 1
                else:
                    endRow = j + placeHeight
                for i in range(startCol, endCol):
                    for j in range(startRow, endRow):
                        grids[i][j]["value"]=random.choice([0,1])
def updateGrids(grids):
    newGrids=createGrids(size,rows,cols)
    for i in range(cols):
        for j in range(rows):
            g=grids[i][j]
            if g["value"]==1:
                if j+1>rows-1:
                    newGrids[i][j]["value"]=1
                elif grids[i][j+1]["value"]==1:
                    d=random.choice([-1,1])
                    if i+d>0 and i+d<cols-1:
                        if grids[i+d][j+1]["value"]==0:
                            newGrids[i+d][j+1]["value"]=1
                        else:
                            newGrids[i][j]["value"]=1
                    else:
                        newGrids[i][j]["value"]=1
                else:
                    newGrids[i][j+1]["value"]=1
                    # newGrids[i][j]["value"]=0
    return newGrids
while True:
    pygame.display.set_caption(str(clock.get_fps()))
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            placeParticle(grids, event.pos)
    screen.fill("black")
    drawGrids(grids)
    grids=updateGrids(grids)
    pygame.display.update()
    clock.tick(fps)
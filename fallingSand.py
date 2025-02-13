import pygame
import random
from pygame.math import Vector3
import numpy as np

pygame.init()
WIDTH, HEIGHT = 150,150
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
fps = 60
size = 1
rows = HEIGHT // size
cols = WIDTH // size
colorWeight = 0
step = 0.01

# Use NumPy for grid storage
grid = np.zeros((cols, rows), dtype=int)
colors = np.full((cols, rows, 3), [255, 255, 255], dtype=int)

def drawGrids():
    for i in range(cols):
        for j in range(rows):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, colors[i, j], (i * size, j * size, size, size))
            else:
                pygame.draw.rect(screen, "black", (i * size, j * size, size, size))

def placeParticle(mpos):
    global colorWeight, step
    placeWidth = 10
    placeHeight = 3

    # Calculate grid indices from mouse position
    i = mpos[0] // size
    j = mpos[1] // size

    # Define bounds for particle placement
    startCol = max(0, i - placeWidth)
    endCol = min(cols - 1, i + placeWidth)
    startRow = max(0, j - placeHeight)
    endRow = min(rows - 1, j + placeHeight)

    # Calculate color
    startColor = Vector3(255, 255, 255)
    endColor = Vector3(255, 0, 0)
    colorWeight += step
    weight = colorWeight % 1
    color = startColor.lerp(endColor, weight)

    # Place particles
    for i in range(startCol, endCol + 1):
        for j in range(startRow, endRow + 1):
            v = random.choice([0, 1])
            grid[i, j] = v
            if v == 1:
                colors[i, j] = color

def updateGrids():
    newGrid = grid.copy()
    newColors = colors.copy()

    for i in range(cols):
        for j in range(rows - 1, -1, -1):  # Iterate from bottom to top
            if grid[i, j] == 1:
                if j + 1 >= rows:  # Particle at the bottom
                    newGrid[i, j] = 1
                    newColors[i, j] = colors[i, j]
                elif grid[i, j + 1] == 0:  # Move down
                    newGrid[i, j + 1] = 1
                    newColors[i, j + 1] = colors[i, j]
                    newGrid[i, j] = 0
                else:  # Check diagonals
                    d = random.choice([-1, 1])
                    if 0 <= i + d < cols and grid[i + d, j + 1] == 0:
                        newGrid[i + d, j + 1] = 1
                        newColors[i + d, j + 1] = colors[i, j]
                        newGrid[i, j] = 0
                    else:
                        newGrid[i, j] = 1
                        newColors[i, j] = colors[i, j]

    return newGrid, newColors


# Main loop
running = True
while running:
    pygame.display.set_caption(str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     placeParticle(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill("black")
    if pygame.mouse.get_pressed()[0]:
        placeParticle(event.pos)
    drawGrids()
    grid, colors = updateGrids()
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
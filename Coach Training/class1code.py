import pygame
from pygame import Vector2

pygame.init()

#game_setup code

size = [500,500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

rect1 = pygame.Rect(0,0,50,50)
rect1.center = [size[0]/2,size[1]/2]
speed = 3
dx = 0
dy = 0

#gameloop code
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = speed
            if event.key == pygame.K_LEFT:
                dx = -speed
            if event.key == pygame.K_UP:
                dy = -speed
            if event.key == pygame.K_DOWN:
                dy = speed
        if event.type == pygame.KEYUP:
            dx = 0
            dy = 0

    if rect1.left - dx < 0 and dx < 0:
        dx = 0
        rect1.left = 0
    if rect1.right + dx > size[0] and dx > 0:
        dx = 0
        rect1.right = size[0]
    if rect1.top - dy < 0 and dy < 0:
        dy = 0
        rect1.top = 0
    if rect1.bottom + dy > size[1] and dy > 0:
        dy = 0
        rect1.bottom = size[1]

    rect1.centerx += dx
    rect1.centery += dy
    print(dx)

    screen.fill([255,255,255])
    pygame.draw.rect(screen,[255,0,0],rect1)
    pygame.display.update()
    clock.tick(fps)


import pygame
from pygame import Vector2
from random import randint

pygame.init()

#game_setup code

size = [500,500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

rect1 = pygame.Rect(0,0,50,50)
rect1.center = [size[0]/2,size[1]/2]
speed = 3
velocity = Vector2(0,0)
gravity = 10

#gameloop code
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    tick = clock.get_time()/100

    velocity[1] += gravity*tick 
    """
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        velocity[0] = speed
    if keys[pygame.K_LEFT]:
        velocity[0] = -speed
    if keys[pygame.K_UP]:
        velocity[1] = -speed
    if keys[pygame.K_DOWN]:
        velocity[1] = speed
    """
    screen.fill([0,0,0])
    if rect1.bottom + velocity[1] >= size[1]:
        dy = size[1] - rect1.bottom
        velocity[1] = 0
    else:
        dy = velocity[1]

    dx = velocity[0]
    rect1.centerx += dx
    rect1.centery += dy

   
    pygame.draw.rect(screen,[255,0,0],rect1)
    pygame.display.update()
    clock.tick(fps)


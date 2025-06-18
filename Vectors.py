import pygame
from pygame.math import Vector2

pygame.init()

WIDTH,HEIGHT = 800,600
screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()
fps = 60

dt = 0

point1 = Vector2(100,100)
speed = 5

isRunning = True
while isRunning:
    mPos = Vector2(pygame.mouse.get_pos())
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False
    screen.fill("black")
    vec2Mouse = mPos - point1
    direction = vec2Mouse
    velocity = direction * speed
    pygame.draw.circle(screen,"green",point1,2.5)
    pygame.draw.line(screen,"red",point1,point1 + vec2Mouse.normalize() * 50)
    point1 += velocity * dt
    pygame.display.update()
    dt = clock.tick(fps)/1000

pygame.quit()

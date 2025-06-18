import pygame
from player import Player

SWIDTH, SHEIGHT = 800, 600

screen = pygame.display.set_mode([SWIDTH,SHEIGHT])
clock = pygame.time.Clock()
fps = 60

dt = 0

p = Player([SWIDTH/2, SHEIGHT * 5/6])

def draw():
    screen.fill("black")
    p.draw(screen)

def update(dt):
    p.update(dt)

isRunning = True
while isRunning:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    update(dt)
    draw()
    dt = clock.tick(fps)/1000
    pygame.display.update()
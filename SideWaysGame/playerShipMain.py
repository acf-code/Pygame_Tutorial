import pygame
from stars import Star
from random import randint
from playerShipClass import Ship
from pygame.math import lerp
from utils import *
pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()
fps = 60
stargroup = []
numStars = 750
radius = [lerp(.5,4,(randint(0,1000))/1000) for _ in range(numStars)]
radius.sort()
print(radius)
for i in range(numStars):
    x = randint(5, WIDTH-5)
    y = randint(5, HEIGHT-5)
    stargroup.append(Star(x, y,radius[i]))

dino = pygame.sprite.GroupSingle(Ship(WIDTH/2,HEIGHT/2))
while True:
    dt = clock.tick(fps)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(pygame.Color("black"))
    for star in stargroup:
        star.update(screen, dt,dino.sprite)
    dino.update(dt,events)
    dino.draw(screen)
    print(dino.sprite.vel[1])
    pygame.display.update()
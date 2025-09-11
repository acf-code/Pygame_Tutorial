import pygame
from star import Star
from random import randint

pygame.init()

WIDTH,HEIGHT = 800,600
screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()
fps = 60

starList = []
numOfStars = 150
for i in range(numOfStars):
    x = randint(0,800)
    y = randint(0,600)
    s = Star([x,y])
    starList.append(s)

def update():
    for star in starList:
        star.update()

def draw(screen):
    screen.fill("black")
    for star in starList:
        star.draw(screen)

isRunning = True
while isRunning:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False

    update()
    draw(screen)
    clock.tick(fps)
    pygame.display.update()

pygame.quit()
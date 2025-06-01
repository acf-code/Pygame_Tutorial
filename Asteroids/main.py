import pygame
from player import Player
from asteroid import Asteroid
from random import randint

pygame.init()

WIDTH,HEIGHT = 800,600

screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()
fps = 60

dt = 0

ship = Player([WIDTH/2,HEIGHT/2])

asteroids = []
for i in range(3):
    x = randint(128,WIDTH-128)
    y = randint(128,HEIGHT - 128)
    if i == 0:
        asteroids.append(Asteroid("big",[x,y]))
    elif i == 1:
        asteroids.append(Asteroid("medium",[x,y]))
    elif i == 2:
        asteroids.append(Asteroid("small",[x,y]))

def update():
    ship.update(dt)
    for a in asteroids:
        a.update(dt,ship,asteroids)
        if a.destroyed:
            asteroids.remove(a)

def draw():
    screen.fill("black")
    for a in asteroids:
        a.draw(screen)
    ship.draw(screen)

isRunning = True
while isRunning:
    pygame.display.set_caption(str(clock.get_fps()))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False

    update()
    draw()
    pygame.display.update()
    dt = clock.tick(fps)/1000

pygame.quit()
exit(1)


import pygame
from myClass import Player


pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH,HEIGHT],vsync=1)
clock = pygame.time.Clock()
fps = 60

player = Player()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()


    player.move()
    screen.fill("white")
    player.draw(screen)
    clock.tick(fps)
    pygame.display.update()
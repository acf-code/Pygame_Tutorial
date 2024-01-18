import pygame
from pygame.math import Vector2
import math

pygame.init()
WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()
fps = 60


while True:
    mPos = pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    keys = pygame.key.get_pressed()
    screen.fill([0,0,0])
    pygame.display.update()
    clock.tick(fps)




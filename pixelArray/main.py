import pygame
from pygame.math import Vector2
import math
pygame.init()
screen = pygame.display.set_mode([960,640])
clock = pygame.time.Clock()
fps = 60


player = pygame.image.load("pixelArray/player.png")
lap = pygame.transform.laplacian(player)
pos = Vector2([250,16])
playerRect = player.get_rect(center = pos)
gravity = 10
vel = Vector2(0)
delta = Vector2(0)

s = pygame.Surface([500,500])
pixelArray = pygame.PixelArray(s)
pixelArray[250,250] = (255,255,0)
pixelArray = pixelArray.close()


while True:
    dt = clock.tick(fps)/1000
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(pygame.Color("black"))
    screen.blit(s,[0,0])
    pygame.display.update()
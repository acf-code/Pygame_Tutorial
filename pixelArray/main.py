import pygame
from pygame.math import Vector2
import math
pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()
fps = 60

class Platform:
    def __init__(self,w,h,pos):
        self.surface = pygame.Surface([w,h])
        self.rect = self.surface.get_rect(bottomright = pos)
        self.fill([0,0,255])


platforms = [Platform(500,100,screen.get_size())]



player = pygame.Surface([32,32])
player.fill([255,0,0])
pos = Vector2([250,16])
playerRect = player.get_rect(center = pos)
gravity = 10
vel = Vector2(0)
delta = Vector2(0)

def platformCollision(collisionRect,platforms):
    for p in platforms:



while True:
    dt = clock.tick(fps)/1000
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    vel += Vector2(0, gravity)*dt
    delta += vel
    collisionRect = player.get_rect(center = pos + delta)
    if collisionRect.colliderect(platform1rect):
        if delta[1] > 0:
            delta[1] = math.floor(platform1rect.top - playerRect.bottom)
            vel[1] = 0
    pos += delta
    playerRect.center = pos
    screen.fill([0,0,0])
    screen.blit(platform1,platform1rect)
    screen.blit(player,playerRect)
    pygame.display.update()
import pygame
from pygame.math import Vector2
import math
pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()
fps = 60

platform1 = pygame.Surface([500,50])
platform1rect = platform1.get_rect(bottomright = screen.get_size())
platform1.fill([0,0,255])

player = pygame.Surface([32,32])
player.fill([255,0,0])
pos = Vector2([250,16])
playerRect = player.get_rect(center = pos)
gravity = 10
vel = Vector2(0)
delta = Vector2(0)


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
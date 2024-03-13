import pygame
from player import Player
from enemy import Enemy
import random
from path import Paths
from pygame.math import Vector2

pygame.init()

WIDTH = 800
HEIGHT = 640

screen = pygame.display.set_mode([WIDTH,HEIGHT])

bckgdImg = pygame.image.load("followingAI/background.png").convert_alpha()
bckgdImg = pygame.transform.scale(bckgdImg,[WIDTH,HEIGHT])
clock = pygame.time.Clock()
fps = 60

BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]

player = Player(WIDTH/2,HEIGHT/2,25,25,5,RED)

path1 = Paths([Vector2(100,100),Vector2(250,100),Vector2(250,200),Vector2(200,250)])

e_h = 30
e_w = 30
enemy = Enemy(30,30,[0,0,0],3,path1)

isRunning = True
while isRunning:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False

    screen.blit(bckgdImg,[0,0])
    player.update()
    player.render(screen)
    path1.render(screen)
    enemy.render(screen)
    enemy.update(player,screen)
    pygame.display.update()
    clock.tick(fps)


pygame.quit()

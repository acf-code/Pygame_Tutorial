import pygame
from player import Player
from enemy import Enemy
import random

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

player = Player(WIDTH/2,HEIGHT/2,50,50,5,RED)

e_h = 30
e_w = 30
enemies = []
for i in range(3):
    enemies.append(Enemy(random.randint(0,WIDTH- e_w),random.randint(0,HEIGHT - e_h),e_w,e_h,BLACK,3))

isRunning = True
while isRunning:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False

    screen.blit(bckgdImg,[0,0])
    player.update()
    player.render(screen)
    for enemy in enemies:
        enemy.update(player)
        enemy.render(screen)
    pygame.display.update()
    clock.tick(fps)


pygame.quit()

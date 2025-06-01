import pygame
from myClass import Player,Enemy
from random import randint


pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH,HEIGHT],vsync=1)
clock = pygame.time.Clock()
fps = 60

player = Player()

numOfEnemies = 3
enemies = []
for i in range(numOfEnemies):
    pos = [randint(25,WIDTH-25),randint(25,HEIGHT-25)]
    enemies.append(Enemy(pos))

healthPacks = []


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    if player.destroyed == False:
        player.update(enemies,screen)
    for enemy in enemies:
        enemy.update(player,enemies,healthPacks)
        if enemy.destroyed:
            enemies.remove(enemy)
    if len(enemies) == 0:
        numOfEnemies += 1
        for i in range(numOfEnemies):
            pos = [randint(25,WIDTH-25),randint(25,HEIGHT-25)]
            enemies.append(Enemy(pos))
    screen.fill("white")
    for pack in healthPacks:
        pack.update(player)
        pack.draw(screen)
        if pack.destroyed:
            healthPacks.remove(pack)
    if player.destroyed == False:
        player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    clock.tick(fps)
    pygame.display.update()
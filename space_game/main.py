#setup
import pygame
from pygame.math import Vector2
from random import randint
import objects, tools

pygame.init()

size = [500, 500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = tools.fps



isRunning = True
#rectanglename = pygame.Rect(x,y,width,height)
r_x = 225
r_y = 200
#t_x = 0
#t_y = 0
#target = pygame.Rect([t_x, t_y], [50, 50])
x_change = 0
y_change = 0
projectiles = []
p_speed = 7
background=pygame.image.load("space_game/images/background.png")
gameover=pygame.image.load("space_game/images/gameover.png")



#to create an object follow this syntax
#object_name = Class_name(paramters)
bob = objects.Enemy([250, 250], 3, [50, 50], (0, 0, 255))
joe = objects.Enemy([0, 0], 5, [70, 70], (255, 0, 255))
enemies = [bob, joe]
player = objects.Player([r_x, r_y], 100, 0.5, "space_game/images/spaceship.png")
waves=3
#game loop(updates each frame of the game)
while isRunning == True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projectiles.append(
                    pygame.Rect([player.pos[0] + 5, player.pos[1]], [10, 10]))
    if player.health<=0:
        for i in range(fps*5):
            screen.blit(gameover,[0,0])
            pygame.display.flip()
        isRunning = False
        pygame.quit()
    screen.blit(background,[0,0])
    player.update(events,screen)
    if len(enemies) > 0:
        for enemy in enemies:
            enemy.update(screen)
            for projectile in projectiles:
                if projectile.colliderect(enemy.rect):
                    enemy.damage()
                    projectiles.remove(projectile)
            if enemy.health <= 0:
                enemies.remove(enemy)
            if enemy.rect.colliderect(player.rect):
                player.damage()
    if len(enemies) == 0:
        for i in range(waves):            
            random_color=(randint(0,255),randint(0,255),randint(0,255))
            enemies.append(objects.Enemy([randint(0,400), randint(0,400)], 3, [randint(50,100), randint(50,100)], random_color))
        waves+=1
    #print(player.pos)
    if len(projectiles) > 0:
        for projectile in projectiles:
            pygame.draw.rect(screen, tools.orange, projectile)
            projectile.y -= p_speed
            if projectile.y < 0:
                projectiles.remove(projectile)
    
    
    clock.tick(fps)
    pygame.display.update()

pygame.quit()

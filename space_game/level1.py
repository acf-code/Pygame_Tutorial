#setup
import pygame
from pygame.math import Vector2
from random import randint
import objects, tools

def gameloop():
    pygame.mixer.init()
    pygame.init()

    size = [500, 500]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = tools.fps

    score_number= 0 







    isRunning = True
    r_x = 225
    r_y = 200
    x_change = 0
    y_change = 0
    projectiles = []
    p_speed = 7
    background=pygame.image.load("space_game/images/background.png")
    background_rect = background.get_rect()
    print(background_rect)
    gameover=pygame.image.load("space_game/images/gameover.png")



    bob = objects.Enemy([250, 250], 3, [50, 50], (0, 0, 255))
    joe = objects.Enemy([0, 0], 5, [70, 70], (255, 0, 255))
    enemies = [bob, joe]
    player = objects.Player([r_x, r_y], 100, 0.5, "space_game/images/spaceship.png")
    waves=3
    pygame.display.set_caption("Space Game")

    while isRunning == True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(player.shot_sound)
                    projectiles.append(
                        pygame.Rect([player.pos[0] + 5, player.pos[1]], [10, 10]))
        if player.health<=0:
            for i in range(fps*5):
                screen.blit(gameover,[0,0])
                pygame.display.flip()
            isRunning = False
            pygame.quit()
        score = tools.score_font.render("Score: " + str(score_number),True, tools.white)
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
                    score_number += 1
                if enemy.rect.colliderect(player.rect):
                    player.damage()
        if len(enemies) == 0:
            for i in range(waves):            
                random_color=(randint(0,255),randint(0,255),randint(0,255))
                enemies.append(objects.Enemy([randint(0,400), randint(0,400)], 3, [randint(50,100), randint(50,100)], random_color))
            waves+=1
        if len(projectiles) > 0:
            for projectile in projectiles:
                pygame.draw.rect(screen, tools.orange, projectile)
                projectile.y -= p_speed
                if projectile.y < 0:
                    projectiles.remove(projectile)
        
        screen.blit(score,[50,50])
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    gameloop()
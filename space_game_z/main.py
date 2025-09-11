#setup
import pygame
import math
from pygame.math import Vector2
import random
import stars
import player
import objects
from asteroid import Asteroid

def spawnAsteroid(asteroids):
    position = [random.randint(0, 800), random.randint(0,640),10000]
    asteroids.append(Asteroid(position,20,32))

def gameloop():
    pygame.mixer.init()
    pygame.init()

    size = [objects.Tools.SCREEN_WIDTH, objects.Tools.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 60

    score_number= 0 

    isRunning = True
    pygame.display.set_caption("Space Game")
    all_stars = []
    for _ in range(200):
        position = [random.randint(-4000, 4000), random.randint(-4000, 4000)]
        star = stars.Star(position, stars.STAR_MIN_RADIUS, stars.STAR_MAX_RADIUS)
        all_stars.append(star)
    ship = player.Player([size[0]/2,size[1]/2],"space_game_z/ship.png",[128,64])
    asteroids = []
    spawnAsteroid(asteroids)
    spawnCooldown = fps * 5
    spawnTimer = 0
    # for i in range(1):
    #     position = [random.randint(0, 800), random.randint(0,640),10000]
    #     asteroids.append(Asteroid(position,20,5))
    while isRunning == True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
        screen.fill([0,0,0])
        for star in all_stars:
            star.update(screen)
        for a in asteroids:
            a.update(screen)
            if a.destroyed:
                asteroids.remove(a)
        if spawnTimer >= spawnCooldown:
            spawnAsteroid(asteroids)
            spawnTimer = 0
        else:
            spawnTimer += 1
        ship.update(screen,asteroids )
        #pygame.draw.circle(screen,(255,0,0),[400,300],5)
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    gameloop()
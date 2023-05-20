#setup
import pygame
import math
from pygame.math import Vector2
import random
import stars
import player
import objects


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
    asteroids = []
    for _ in range(200):
        position = [random.randint(-4000, 4000), random.randint(-4000, 4000)]
        star = stars.Star(position, stars.STAR_MIN_RADIUS, stars.STAR_MAX_RADIUS)
        all_stars.append(star)
    ship = player.Player([size[0]/2,size[1]/2],"space_game_z/ship.png",[128,64])
    for i in range(5):
        asteroids.append(objects.Asteroid(1,(125,125,125),objects.Tools.random_hexagon(size[0]/8,size[1]/8)))

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
            print(a.p_verticies)
            #if a.destroyed:
                #asteroids.remove(a)
        ship.update(screen)
        #pygame.draw.circle(screen,(255,0,0),[400,300],5)
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    gameloop()
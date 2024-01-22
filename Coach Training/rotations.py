import pygame
from pygame.math import Vector2

pygame.init()

#game_setup code
WIDTH = 500
HEIGHT = 500
size = [WIDTH,HEIGHT]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

up = Vector2(0,-1)

#to load a image use pygame.image.load("path to image")
spaceship = pygame.image.load("Coach Training/spaceship.png")
spaceship_rect = pygame.Rect(0,0,128,128)
#to transform the scale of an image use pygame.transform.scale(surface,[w,h])
spaceship = pygame.transform.scale(spaceship,[spaceship_rect.w,spaceship_rect.h])
spaceship_rect.center = [WIDTH/2,HEIGHT/2]

#gameloop code
while True:
    mPos = Vector2(pygame.mouse.get_pos())
    sPos = Vector2(spaceship_rect.center)
    direction = mPos - sPos
    angle = up.angle_to(direction)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill([0,0,0])
    #to show image on screen
    spaceship_rot = pygame.transform.rotate(spaceship,-angle)
    spaceship_rot_rect = spaceship_rot.get_rect(center = spaceship_rect.center)
    pygame.draw.rect(screen,[0,255,0],spaceship_rot_rect)
    pygame.draw.rect(screen,[255,0,0],spaceship_rect)
    screen.blit(spaceship_rot,spaceship_rot_rect)
    pygame.display.update()
    clock.tick(fps)


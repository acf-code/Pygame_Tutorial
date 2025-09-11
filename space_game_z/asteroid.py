import pygame
import random
import objects
from pygame.math import Vector2,Vector3
from polygon import createAsteroidSurface

SWIDTH = objects.Tools.SCREEN_WIDTH
SHEIGHT = objects.Tools.SCREEN_HEIGHT

class Asteroid:
    def __init__(self,pos,speed,radius):
        self.pos = Vector3(pos)
        self.new_pos = Vector2(pos[0],pos[1])
        self.speed = speed
        self.t_radius = radius
        self.radius = self.t_radius
        self.r_scale = .5
        self.color = "blue"
        self.destroyed = False
        self.startSize = 16
        self.size = self.startSize
        self.rect = pygame.Rect(0,0,self.size,self.size)
        self.baseImage = createAsteroidSurface([256,256],"space_game_z/asteroidTexture.jpg")

    # def render(self,screen):
    #     if self.pos[2] != 0 and self.radius > 1:
    #         self.r_scale = .5
    #         self.radius = self.radius - self.r_scale
    #     elif self.pos[2] == 0:
    #         self.radius = self.t_radius
    #     else:
    #         self.radius = 1
    #     pygame.draw.circle(screen,self.color,self.new_pos,self.radius)
    def render(self,screen):
        image = pygame.transform.scale(self.baseImage,[self.size,self.size])
        self.rect = image.get_rect(center = self.new_pos)
        screen.blit(image,self.rect)
        
    def move(self):
        if self.pos[2] > 0:
            self.pos[2] -= self.speed
            self.new_pos = objects.Tools.projectTo(self.pos[0],self.pos[1],self.pos[2])
        else:
            self.destroyed = True

    def destroy(self):
        if self.pos[2] >= objects.Tools.SPAWN_Z:
            self.destroyed = True

    def update(self,screen):
        self.render(screen)
        self.move()
        self.size += .1
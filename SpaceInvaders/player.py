import pygame
from pygame.math import Vector2
import math
SWIDTH, SHEIGHT = 800, 600
class Player:
    def __init__(self,startPos):
        self.pos = Vector2(startPos)
        self.vel = Vector2(0)
        self.image = pygame.Surface([32,32])
        self.image.fill("green")
        self.rect = self.image.get_rect(center = self.pos)
        self.speed = 100
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def getInput(self):
        self.vel = Vector2(0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.vel[0] = self.speed
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.vel[0] = -self.speed

    def boundary(self):
        #check the left boundary
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel.x = 0
        if self.rect.right > SWIDTH:
            self.rect.right = SWIDTH
            self.vel.x = 0
        self.pos = Vector2(self.rect.center)


    def update(self,dt):
        self.getInput()
        if self.vel != Vector2(0):
            dist = abs(self.vel.x*dt)
            dist = math.ceil(dist)
            if self.vel.x < 0:
                dist *= -1
            self.pos.x += dist
        self.rect.center = self.pos
        self.boundary()
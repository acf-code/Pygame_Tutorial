import pygame
from pygame.math import Vector2
from utils import *

class Ship(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.gravity = 10/1000
        self.pos = Vector2(x,y)
        self.image = pygame.image.load("SideWaysGame/ship.png")
        self.rect = self.image.get_rect(center = self.pos)
        self.vel = Vector2(0)
        self.impulse = 0
        self.upImpulse = 6
        self.maxFallingSpeed = 100

    def getKeys(self,events):
        self.impulse = 0
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.impulse = self.upImpulse
                    return True
            else:
                return False
                

    def update(self,dt,events):
        vel = self.vel
        if self.getKeys(events):
            vel[1] = -self.impulse
        else:
            vel[1] += self.gravity * dt
        if vel[1] < self.maxFallingSpeed:
            self.vel[1]=vel[1]
        else:
            #self.vel[1]= self.maxFallingSpeed 
            self.vel[1]=vel[1]
        self.pos += self.vel
        self.rect.center = self.pos
        if self.pos[1] > HEIGHT:
            self.pos[1] = 0
            #self.vel[1] = 0




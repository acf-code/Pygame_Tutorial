import pygame
from pygame.math import Vector2,Vector3

class Particle:
    def __init__(self,startPos,direction,speed,color:Vector3,size = 1,lifetime = .1):
        self.pos = Vector2(startPos)
        self.direction = Vector2(direction)
        self.speed = speed
        self.color = color.xyz
        self.size = size
        self.lifetime = lifetime
        self.destroyed = False

    def update(self,dt):
        vel = self.direction * self.speed
        self.pos += vel*dt
        self.lifetime -= dt
        if self.lifetime < 0:
            self.destroyed = True

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,self.pos,self.size)
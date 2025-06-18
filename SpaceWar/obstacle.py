import pygame
from pygame.math import Vector2,Vector3
from random import randint

class Obstacle:

    def __init__(self,pos):
        self.pos = pos
        self.width = 100
        self.height = 50
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.pos
        self.pSize = 10
        self.tag = "obstacle"
        self.startColor = Vector3(226, 183, 247)
        self.endColor = Vector3(143, 6, 113)
        self.particles = self.generateParticles(self.rect.topleft)

    def generateParticles(self,startPos):
        pList = []
        cols = int(self.width/self.pSize)
        rows = int(self.height/self.pSize)
        for i in range(rows):
            for j in range(cols):
                color = self.startColor.smoothstep(self.endColor,i/rows)
                particle = Particle([startPos[0] + j*self.pSize,startPos[1] + i*self.pSize],self.pSize,color)
                pList.append(particle)
        return pList
    
    def update(self):
        self.rect.center = self.pos
        for particle in self.particles:
            particle.update()
            if particle.destroyed:
                self.particles.remove(particle)

    def draw(self,screen):
        #pygame.draw.rect(screen,"red",self.rect)
        for particle in self.particles:
            particle.draw(screen)




class Particle:
    def __init__(self,pos,size,color):
        self.size = size
        self.pos = Vector2(pos)
        self.rect = pygame.Rect(0,0,self.size,self.size)
        self.rect.topleft = self.pos
        self.destroyed = False
        self.tag = "particle"
        self.color = color

    def update(self):
        self.rect.topleft = self.pos

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)
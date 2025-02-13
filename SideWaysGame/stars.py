import pygame
from pygame.math import Vector2, lerp, Vector3
from random import randint
from utils import *

class Star:
    def __init__(self, x, y,radius,color):
        self.baseColor = color
        self.enter(x, y,radius)
    def enter(self, x ,y,radius):
        self.pos = Vector2(x, y)
        self.direction = Vector2(-1, 0)
        maxRadius = 4
        self.radius = radius
        self.maxSpeed = 15
        self.speed = self.maxSpeed // (maxRadius-self.radius + 1)
        self.newColor = self.baseColor
        self.oldColor = Vector3(255 - self.newColor[0],255 - self.newColor[1],255 - self.newColor[2])
        #self.color = self.blue.lerp(self.red,(maxRadius-self.radius)/maxRadius)
        self.color = self.oldColor.lerp(self.newColor,(self.maxSpeed-self.speed)/self.maxSpeed)
    def render(self, screen):
        # pygame.draw.circle(screen, self.color, self.pos, self.radius)
        # pygame.draw.line(screen,self.color,self.pos,[self.pos[0],HEIGHT],int(self.radius)*5)
        surface = pygame.Surface([self.radius*20,HEIGHT-self.radius])
        rect = surface.get_rect(center = [self.pos[0],self.pos[1]-self.radius])
        surface.fill(self.color)
        screen.blit(surface,rect)
    def update(self, screen, dt,player):
        distanceFromCenter = abs(self.pos[0] - WIDTH/2)
        #self.color = self.oldColor.lerp(self.newColor,(WIDTH/2-distanceFromCenter)/(WIDTH/2))
        #self.color = self.red.lerp(self.blue,(player.maxFallingSpeed-abs(player.vel[1]))/player.maxFallingSpeed)
        self.render(screen)
        velocity = self.direction*self.speed
        self.pos += velocity
        if self.pos[0] < 0:
            x = WIDTH
            y = randint(0, HEIGHT)
            self.enter(x, y,self.radius)


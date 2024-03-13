import pygame
from pygame.math import Vector2

class Player:

    def __init__(self,start_x,start_y,w,h,speed,color):
        self.pos = Vector2(start_x,start_y)
        self.w = w
        self.h = h
        self.speed = speed
        self.color = color
        self.rect = pygame.Rect(0,0,self.w,self.h)
        self.detectRadius = self.w
        self.vel = Vector2(0)

    def move(self):
        self.vel = Vector2(0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vel[0] = -1
        if keys[pygame.K_d]:
            self.vel[0] = 1
        if keys[pygame.K_w]:
            self.vel[1] = -1
        if keys[pygame.K_s]:
            self.vel[1] = 1

        if self.vel != Vector2(0):
            self.vel = self.vel.normalize()

        self.vel = self.vel*self.speed
        self.pos += self.vel
        self.rect.center = self.pos

    def render(self,screen):
        #pygame.draw.rect(screen,self.color,self.rect)
        pygame.draw.circle(screen,self.color,self.pos,self.detectRadius)

    def update(self):
        self.move()

        
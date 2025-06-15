import pygame
from pygame.math import Vector2

class Projectile:
    def __init__(self,pos,direction):
        self.pos = Vector2(pos)
        self.direction = Vector2(direction)
        self.speed = 500
        self.image = pygame.image.load("Asteroids/bullet.png")
        self.image = pygame.transform.scale_by(self.image,.5)
        self.imageRot = self.image
        self.rect = self.image.get_rect(center = self.pos)
        self.destroyed = False
    
    def update(self,dt):
        self.move(dt)
        self.checkBoundary()
        self.rect.center = self.pos

    def draw(self,screen):
        angle = Vector2(0,-1).angle_to(self.direction)
        imageRot = pygame.transform.rotate(self.image,-angle)
        imageRotRect = imageRot.get_rect(center = self.pos)
        self.imageRot = pygame.Surface(imageRotRect.size)
        self.imageRot.fill("green")
        self.imageRot.set_colorkey("green")
        self.imageRot.blit(imageRot,[0,0])
        screen.blit(self.imageRot,imageRotRect)

    def move(self,dt):
        vel = self.direction*self.speed
        self.pos += vel*dt

    def checkBoundary(self):
        if self.pos.x < 0 or self.pos.x > 800:
            self.destroyed = True
        if self.pos.y < 0 or self.pos.y > 600:
            self.destroyed = True
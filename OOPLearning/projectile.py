import pygame
from pygame.math import Vector2

class Projectile:
    def __init__(self,startPos,direction,speed):
        self.pos = Vector2(startPos)
        self.direction = Vector2(direction).normalize()
        self.speed = speed
        self.image = pygame.Surface([32,32])
        self.rect = self.image.get_rect(center = self.pos)
        self.image.fill("yellow")
        self.lifeTime = 15
        self.destroyed = False
        self.damage = 1

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def update(self,player):
        self.move()
        self.collide(player)
        self.rect.center = self.pos
        self.lifeTime -= 1
        if self.lifeTime < 0:
            self.destroyed = True

    def move(self):
        velocity = self.speed * self.direction
        self.pos += velocity 

    def collide(self,object):
        if self.rect.colliderect(object.hitBox):
            self.destroyed = True
            object.gotHit(self)
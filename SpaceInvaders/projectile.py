import pygame
from pygame.math import Vector2

class Projectile:
    def __init__(self,startPos,speed):
        self.pos = Vector2(startPos)
        self.speed = speed
        self.vel = Vector2(0)
        self.image = pygame.Surface([8,8])
        self.rect = self.image.get_rect(center = self.pos)

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def update(self,dt):
        self.move(dt)

    def move(self,dt):
        pass


class PlayerBullet(Projectile):
    def __init__(self, startPos, speed):
        super().__init__(startPos, speed)

    def move(self,dt):
        self.vel = Vector2(0,-self.speed)
        self.pos += self.vel * dt
import pygame
from pygame.math import Vector2

class Bullet:
    def __init__(self,startPos,direction,speed):
        self.pos = Vector2(startPos)
        self.direction = Vector2(direction)
        self.speed = speed
        self.image = pygame.Surface([4,16])
        self.image.fill("green")
        self.rect = self.image.get_rect(center = self.pos)
        self.destroyed = False
        self.damage = 1

    def update(self,objects):
        self.move()
        self.collide(objects)
        self.rect.center = self.pos
        if self.rect.bottom < 0 or self.rect.top > 500:
            self.destroyed = True

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def move(self):
        velocity = self.direction * self.speed
        self.pos += velocity

    def obstacleCollide(self,object):
        if object.tag == "obstacle":
            for particle in object.particles:
                if self.rect.colliderect(particle.rect):
                    particle.destroyed = True
                    self.destroyed = True

    def collide(self,objects):
        for object in objects:
            if self.rect.colliderect(object.rect):
                print(object.tag)
            self.obstacleCollide(object)

class PlayerBullet(Bullet):
    def __init__(self, startPos, direction, speed):
        super().__init__(startPos, direction, speed)

    def collide(self,objects):
        for object in objects:
            if object.tag == "enemy":
                if self.rect.colliderect(object.rect):
                    if not object.destroyed:
                        print(object.destroyed)
                        self.destroyed = True
                        object.health -= self.damage
            self.obstacleCollide(object)


class EnemyBullet(Bullet):
    def __init__(self, startPos, direction, speed):
        super().__init__(startPos, direction, speed)

    def collide(self,objects):
        for object in objects:
            if object.tag == "player":
                if self.rect.colliderect(object.rect):
                    self.destroyed = True
            self.obstacleCollide(object)



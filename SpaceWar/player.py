import pygame
from pygame.math import Vector2
from bullet import Bullet,PlayerBullet

class Player:
    def __init__(self,startPos):
        self.pos = Vector2(startPos)
        self.vel = Vector2(0) #velocity
        self.speed = 2.5
        self.input = 0
        self.image = pygame.image.load("SpaceWar/player.png")
        self.image = pygame.transform.scale(self.image,[24,24])
        self.rect = self.image.get_rect(center = self.pos)
        self.bullets = []
        self.canShoot = False
        self.shootTimer = 0
        self.shootCooldown = 30
        self.tag = "player"

    def draw(self,screen):
        for bullet in self.bullets:
            bullet.draw(screen)
        screen.blit(self.image,self.rect)

    def update(self,objects):
        self.getInput()
        self.move()
        self.checkBoundary()
        if self.canShoot:
            self.shoot()
        self.rect.center = self.pos
        for bullet in self.bullets:
            bullet.update(objects)
            if bullet.destroyed:
                self.bullets.remove(bullet)
        if self.shootTimer < self.shootCooldown:
            self.shootTimer += 1

    def getInput(self):
        self.input = 0
        self.canShoot = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.input = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.input = 1
        if keys[pygame.K_SPACE]:
            if self.shootTimer >= self.shootCooldown and self.input == 0:
                self.canShoot = True
                self.shootTimer = 0

    def move(self):
        self.vel.x = self.input * self.speed
        self.pos += self.vel

    def checkBoundary(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel.x = 0
            self.pos = Vector2(self.rect.center)
        if self.rect.right > 500:
            self.rect.right = 500
            self.vel.x = 0
            self.pos = Vector2(self.rect.center)

    def shoot(self):
        b = PlayerBullet(self.pos,Vector2(0,-1),5)
        self.bullets.append(b)


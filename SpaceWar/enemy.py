import pygame
from pygame.math import Vector2
from random import randint
from bullet import EnemyBullet

class Enemy:
    def __init__(self,startPos,size,destroyed = False,health = 1):
        self.pos = Vector2(startPos)
        self.image = pygame.image.load("SpaceWar/enemy.png")
        self.image = pygame.transform.scale(self.image,[size,size])
        self.rect = self.image.get_rect(center = self.pos)
        self.tag = "enemy"
        self.destroyed = destroyed
        self.health = health
        self.shootChance = 5
        self.bullets = []
        self.shootTimer = 0
        self.shootCooldown = 2
    
    def update(self,dt,objects,bullets):
        if self.health <= 0:
            self.destroyed = True
        self.rect.center = self.pos
        if self.shootTimer <= self.shootCooldown:
            self.shootTimer += dt
        if self.shootTimer > self.shootCooldown and not self.destroyed:
            value = randint(0,100)
            if value < self.shootChance:
                self.shoot(bullets)
            self.shootTimer = 0
        if not self.destroyed:
            for bullet in self.bullets:
                bullet.update(objects)

    def draw(self,screen):
        if not self.destroyed:
            screen.blit(self.image,self.rect)
            for bullet in self.bullets:
                bullet.draw(screen)

    def shoot(self,bullets):
        bullet = EnemyBullet(self.pos,Vector2(0,1),5)
        bullets.append(bullet)
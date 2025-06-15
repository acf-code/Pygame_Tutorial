import pygame
from pygame.math import Vector2
from projectile import Projectile


class Shooter:
    def __init__(self,player):
        self.player = player
        self.pos = player.rect.center
        self.direction = player.direction
        self.bullets = []
        self.timer = 0
        self.cooldown = .5


    def update(self,dt):
        self.direction = self.player.direction
        self.pos = self.player.rect.center
        canShoot = self.getInput()
        if canShoot:
            self.shoot()
        if self.timer < self.cooldown:
            self.timer += dt
        for bullet in self.bullets:
            bullet.update(dt)
            if bullet.destroyed:
                self.bullets.remove(bullet)

    def draw(self,screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def getInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.timer >= self.cooldown:
            self.timer = 0
            return True
        else:
            return False
        
    def shoot(self):
        bullet = Projectile(self.pos,self.direction)
        self.bullets.append(bullet)
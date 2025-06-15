import pygame
from pygame.math import Vector2
from random import randint

#It needs a size("BIG,"MEDIUM","SMALL") and pos as arguments for the class constructor
#Depending size will depend the image and size of the asteroid
#It will have an update method and a draw method

class Asteroid:
    def __init__(self,type,pos):
        self.type = type
        self.pos = Vector2(pos)
        self.dir = Vector2(-1,0).rotate(randint(0,360))
        if self.type == "big":
            self.size = [128,128]
            self.image = self.getImage("Asteroids/asteroidBig.png",self.size)
            self.speed = 30
        elif self.type == "medium":
            self.size = [64,64]
            self.image = self.getImage("Asteroids/asteroidMedium.png",self.size)
            self.speed = 60
        elif self.type == "small":
            self.size = [32,32]
            self.image = self.getImage("Asteroids/asteroidSmall.png",self.size)
            self.speed = 120
        self.rect = self.image.get_rect(center = self.pos)
        self.hitbox = self.image.get_bounding_rect()
        self.hitbox.center = self.pos
        self.collided = False
        self.destroyed = False
        
    
    def getImage(self,image,size):
        surface = pygame.Surface(size)
        surface.fill("white")
        surface.set_colorkey("white")
        baseImage = pygame.image.load(image)
        baseImage = pygame.transform.scale(baseImage,size)
        surface.blit(baseImage,[0,0])
        return surface
    
    def update(self,dt,player,asteroids):
        self.playerCollide(player)
        self.bulletCollide(player)
        if self.collided:
            if self.type != "small":
                self.spawn(asteroids)
            self.destroyed = True
        self.move(dt)
        self.rect.center = self.pos
        self.hitbox.center = self.pos

    def draw(self,screen):
        # if not self.collided:
        #     pygame.draw.rect(screen,"green",self.rect)
        # else:
        #     pygame.draw.rect(screen,"red",self.rect)
        screen.blit(self.image,self.rect)

    def playerCollide(self,player):
        if self.rect.colliderect(player.hitBox):
            offset = Vector2(self.rect.topleft) - Vector2(player.hitBox.topleft)
            playerMask = pygame.mask.from_surface(player.imageRot)
            asteroidMask = pygame.mask.from_surface(self.image)
            area = playerMask.overlap_area(asteroidMask,offset)
            if area > 0:
                self.collided = True
            else:
                self.collided = False
        else:
            self.collided = False
    
    def spawn(self,asteroids):
        if self.type == "big":
            t = "medium"
            distance = 125
        else:
            t = "small"
            distance = 75
        for i in range(2):
            pos = self.pos + Vector2(-1,0).rotate(randint(0,360))*distance
            asteroids.append(Asteroid(t,pos))

    def bulletCollide(self,player):
        bullets = player.shooter.bullets
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                self.collided = True
                bullet.destroyed = True

    def move(self,dt):
        vel = self.dir*self.speed
        self.pos += vel*dt
        if self.rect.right < 0:
            self.rect.left = 800
            self.pos = self.rect.center
        if self.rect.left > 800:
            self.rect.right = 0
            self.pos = self.rect.center
        if self.rect.bottom < 0:
            self.rect.top = 600
            self.pos = self.rect.center
        if self.rect.top > 600:
            self.rect.bottom = 0
            self.pos = self.rect.center
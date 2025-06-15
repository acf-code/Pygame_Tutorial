import pygame
from pygame.math import Vector2
from thruster import Thruster
from shooter import Shooter

class Player:
    def __init__(self,startPos):
        self.pos = Vector2(startPos)
        self.size = 32
        self.direction = Vector2(0,-1)
        self.vel = Vector2(0)
        self.input = Vector2(0)
        self.speed = 300
        self.rotationSpeed = 150
        self.acc = 5
        self.deAcc = 1
        self.image = pygame.image.load("Asteroids/player.png")
        self.image = pygame.transform.scale(self.image,[self.size,self.size])
        self.imageRot = self.image
        self.rect = self.image.get_rect(center = self.pos)
        self.hitBox = self.rect
        self.thruster = Thruster(30,[255,255,0],[255,0,0],700)
        self.shooter = Shooter(self)
        self.maxLives = 3
        self.lives = self.maxLives

    def update(self,dt):
        self.input = self.getInput()
        self.move(dt)
        self.rotate(dt)
        self.checkBoundary()
        self.thruster.update(dt)
        self.shooter.update(dt)
        self.rect.center = self.pos

    def draw(self,screen):
        #pygame.draw.circle(screen, "green", self.pos,self.size)
        angle = Vector2(0,-1).angle_to(self.direction)
        imageRot = pygame.transform.rotate(self.image,-angle)
        imageRotRect = imageRot.get_rect(center = self.rect.center)
        self.imageRot = pygame.Surface(imageRotRect.size)
        self.imageRot.fill("green")
        self.imageRot.set_colorkey("green")
        self.imageRot.blit(imageRot,[0,0])
        #pygame.draw.rect(screen,"yellow",imageRotRect)
        self.shooter.draw(screen)
        screen.blit(self.imageRot,imageRotRect)
        self.thruster.draw(screen)
        self.hitBox = imageRotRect
        #pygame.draw.line(screen,"red",self.pos,self.pos + self.direction*self.size)


    def getInput(self):
        input = Vector2(0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            input.y = 1
        if keys[pygame.K_d]:
            input.x = 1
        if keys[pygame.K_a]:
            input.x = -1
        return input
    
    def move(self,dt):
        desiredVel = self.direction*self.input.y*int(self.speed*dt)
        if self.input.y == 1:
            maxSpeedChange = self.acc*dt
            thrustDirection = self.direction.rotate(180)
            thrustPos = self.pos + thrustDirection*self.size/2
            self.thruster.shoot(thrustDirection,100,thrustPos)
        else:
            maxSpeedChange = self.deAcc*dt
        self.vel.move_towards_ip(desiredVel,maxSpeedChange)
        self.pos += self.vel

    def rotate(self,dt):
        rSpeed = int(self.rotationSpeed * dt)
        self.direction.rotate_ip(rSpeed*self.input.x)

    def checkBoundary(self):
        if self.pos.x < 0:
            self.pos.x = 800
        elif self.pos.x > 800:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = 600
        elif self.pos.y > 600:
            self.pos.y = 0
        


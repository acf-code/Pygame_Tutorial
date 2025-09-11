import pygame
from pygame.math import Vector2, lerp, Vector3
from random import randint

#We are going to create a class Star
#You can think of a class as a blueprint to create a certain object
#in this case we are creating a class star so that we can multiple star objects in our scene
#that move and behave all in the same way

#lerp:
#lerp: linear interpolation
#it takes in two values (a,b) and a weight value (t)
#t has to be between 0 and 1
#lerp will take the point between (a) and (b) that is (t) away from (a)

#example: a = 0, b = 10, t = 0.2
#x = lerp(a,b,t)
#x will be equzl to 2

class Star:
    #The first thing we need in our star class is a constructor method
    #the constructor method works very similarily to our createPlayer() function
    #it defines what attributes define a start object
    #such as position,radius,color,speed....
    #these attributes are called instance variables

    #CONSTRUCTOR METHOD
    def __init__(self,startPos):
        #INSTANCE VARIABLES
        self.pos = Vector2(startPos)
        self.minRadius = 1
        self.maxRadius = 4
        t = randint(1,100)/100
        self.radius = lerp(self.minRadius,self.maxRadius,t)
        self.startColor = Vector3(1, 44, 51)
        self.endColor = Vector3(184, 184, 24)
        self.minSpeed = 2
        self.maxSpeed = 10
        self.speed = lerp(self.minSpeed,self.maxSpeed,self.radius/self.maxRadius)
        self.color = self.startColor.lerp(self.endColor,self.radius/self.maxRadius)


    def draw(self,screen):
        pygame.draw.circle(screen,self.color,self.pos,self.radius)

    def update(self):
        self.move()
        self.checkBoundary()

    def move(self):
        self.pos.y += self.speed

    def checkBoundary(self):
        if self.pos.y > 600 - self.radius:
            self.pos.y = 0
            self.pos.x = randint(0,800)
    

import pygame
from pygame.math import Vector2,Vector3
from particle import Particle
from random import randint

class Thruster:
    def __init__(self,thrustAngle, startColor,endColor,speed):
        self.thrustAngle = thrustAngle
        self.startColor = Vector3(startColor)
        self.endColor = Vector3(endColor)
        self.speed = speed
        self.particles = []

    def update(self,dt):
        for particle in self.particles:
            particle.update(dt)
            if particle.destroyed:
                self.particles.remove(particle)

    def draw(self,screen):
        for particle in self.particles:
            particle.draw(screen)

    def shoot(self,direction:Vector2,amount,pos):
        for i in range(amount):
            angle = randint(-self.thrustAngle//2,self.thrustAngle//2)
            d = direction.rotate(angle)
            speed = randint(100,self.speed)
            t = abs(angle)/(self.thrustAngle//2)
            if t < 0:
                t = 0
            if t > 1:
                t = 1
            color = self.startColor.lerp(self.endColor,t)
            particle = Particle(pos,d,speed,color)
            self.particles.append(particle)
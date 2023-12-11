#creating collisions between enemy blocks and player

import pygame
from pygame import Vector2
from random import randint

pygame.init()

#game_setup code

size = [500,500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

rect1 = pygame.Rect(0,0,50,50)
rect1.center = [size[0]/2,size[1]/2]
speed = 3
velocity = Vector2(0,0)

class Enemy:
    def __init__(self,x,y,w,h,speed,color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.speed = speed
        self.color = color
        self.center = Vector2(x,y)
        self.vel = Vector2(0)

    def render(self, screen):
        self.rect.center = self.center
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        self.vel[1] = self.speed
        self.center += self.vel
        if self.rect.top > size[1]:
            self.center[0] = randint(0,size[0])
            self.center[1] = -self.h/2
    
    def update(self,screen):
        self.render(screen)
        self.move()

enemies = []
for i in range(3):
    enemies.append(Enemy(randint(25,size[0]),25,50,50,5,[255,255,0]))


#gameloop code
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYUP:
            velocity[0] = 0
            velocity[1] = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        velocity[0] = speed
    if keys[pygame.K_LEFT]:
        velocity[0] = -speed
    if keys[pygame.K_UP]:
        velocity[1] = -speed
    if keys[pygame.K_DOWN]:
        velocity[1] = speed

    if rect1.left - velocity[0] < 0 and velocity[0] < 0:
        velocity[0] = 0
        rect1.left = 0
    if rect1.right + velocity[0] > size[0] and velocity[0] > 0:
        velocity[0] = 0
        rect1.right = size[0]
    if rect1.top - velocity[1] < 0 and velocity[1] < 0:
        velocity[1] = 0
        rect1.top = 0
    if rect1.bottom + velocity[1] > size[1] and velocity[1] > 0:
        velocity[1] = 0
        rect1.bottom = size[1]
    
    if velocity != Vector2(0):
        velocity = velocity.normalize()
    velocity[0] = velocity[0] * speed
    velocity[1] = velocity[1] * speed

    rect1.centerx +=  velocity[0]
    rect1.centery += velocity[1]

    screen.fill([0,0,0])
    for e in enemies:
        e.update(screen)
        if e.rect.colliderect(rect1):
            pygame.quit()
    pygame.draw.rect(screen,[255,0,0],rect1)
    pygame.display.update()
    clock.tick(fps)


import pygame
from pygame.math import Vector2
import math

pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()
fps = 60

class Player:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,w,h)
        self.speed = 5
        self.image = pygame.image.load("pygameRotations/spaceship.png")
        self.image = pygame.transform.scale(self.image,[self.rect.w,self.rect.h])
        self.angle = 270
        self.angularspeed = 3
        self.direction = Vector2.from_polar([self.rect.h/2,self.angle])
        #self.direction = Vector2(0,-self.rect.h/2)


    def move(self,keys):
        old_angle = self.angle
        vel = Vector2(0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.angle += self.angularspeed
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.angle -= self.angularspeed
        else:
            pass
        self.direction = Vector2.from_polar([self.rect.h/2,self.angle])
        d = self.direction.normalize()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            vel[1] = d[1]
            vel[0] = d[0]
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            vel[1] = -d[1]
            vel[0] = -d[0]
        if vel != Vector2(0):
            vel = vel.normalize()
            vel[0] *= self.speed
            vel[1] *= self.speed
        if abs(self.angle) == 360:
            self.angle = 0
        
        if old_angle != self.angle:
            print(d)
            print(self.angle)
            old_angle = self.angle
        self.x += vel[0]
        self.y += vel[1]


        

    def render(self,screen):
        self.rect.center = [self.x,self.y]
        up = Vector2(0,-1)
        angleFromUp = up.angle_to(self.direction)
        image_rot = pygame.transform.rotate(self.image,-angleFromUp)
        image_rect = image_rot.get_rect()
        image_rect.center = [self.x,self.y]
        screen.blit(image_rot,image_rect)
        #pygame.draw.rect(screen,[255,0,0],self.rect)
        #pygame.draw.circle(screen,[255,0,0],[self.x,self.y],10)



    def update(self,screen,keys,dt):
        self.move(keys)
        self.render(screen)
        pygame.draw.line(screen,[0,255,0],[self.x,self.y],[self.x + self.direction[0],self.y + self.direction[1]])



player = Player(WIDTH/2,HEIGHT/2,50,50)

while True:
    mPos = pygame.mouse.get_pos()
    events = pygame.event.get()
    dt = clock.get_time()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    screen.fill([0,0,0])
    player.update(screen,keys,dt)
    pygame.display.update()
    clock.tick(fps)
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
        self.projectiles = []
        self.p_speed = 10
        self.p_image = pygame.image.load("pygameRotations/projectile.png")
        self.p_w = 3
        self.p_h = 10
        self.p_cooldown = 500
        self.p_timer = 0


    def move(self,keys):
        vel = Vector2(0)
        if keys[pygame.K_RIGHT]:
            vel[0] = self.speed
        elif keys[pygame.K_LEFT]:
            vel[0] = -self.speed
        if keys[pygame.K_UP]:
            vel[1] = -self.speed
        elif keys[pygame.K_DOWN]:
            vel[1] = self.speed
        if vel != Vector2(0):
            vel = vel.normalize()
            vel[0] *= self.speed
            vel[1] *= self.speed
        self.x += vel[0]
        self.y += vel[1]

    def shoot(self,dt):
        direction = Vector2(0)
        if  keys[pygame.K_d]:
            direction[0] = 1
        if keys[pygame.K_a]:
            direction[0] = -1
        if keys[pygame.K_w]:
            direction[1] = -1
        if keys[pygame.K_s]:
            direction[1] = 1
        if direction != Vector2(0):
            if self.p_timer >= self.p_cooldown:
                self.projectiles.append(Projectile(self.x,self.y,self.p_w,self.p_h,self.p_speed,self.p_image,direction))
                self.p_timer = 0

        if self.p_timer < self.p_cooldown:
            self.p_timer += dt

        

    def render(self,screen):
        self.rect.center = [self.x,self.y]
        pygame.draw.rect(screen,[255,0,0],self.rect)
        #pygame.draw.circle(screen,[255,0,0],[self.x,self.y],10)

    def p_update(self,screen):
        if len(self.projectiles) > 0:
            for p in self.projectiles:
                p.update(screen)

    def update(self,screen,keys,dt):
        self.move(keys)
        self.render(screen)
        self.shoot(dt)
        self.p_update(screen)


class Projectile:
    def __init__(self,x,y,w,h,speed,image,direction):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.image = pygame.transform.scale(image,[self.w,self.h])
        self.direction = direction
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)

    def render(self,screen):
        self.rect.center = [self.x,self.y]
        d = self.direction
        up = Vector2(0,-1)
        angle = up.angle_to(d)
        print(angle)
        image_rot = pygame.transform.rotate(self.image,-angle)
        image_rect = image_rot.get_rect()
        image_rect.center = [self.x,self.y]
        screen.blit(image_rot,image_rect)

    def move(self):
        d = self.direction.normalize()
        d[0] *= self.speed
        d[1] *= self.speed
        self.x += d[0]
        self.y += d[1]

    def update(self,screen):
        self.move()
        self.render(screen)



player = Player(WIDTH/2,HEIGHT/2,36,36)

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
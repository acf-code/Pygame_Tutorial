import pygame
from objects import *
from pygame.math import Vector3,Vector2

SCREEN_WIDTH = Tools.SCREEN_WIDTH
SCREEN_HEIGHT = Tools.SCREEN_HEIGHT

class Player:

    def __init__(self,pos,image,size,max_acc = 0.25,max_speed = 7):
        self.pos = Vector3(pos[0],pos[1],0)
        self.vel = Vector3(0)
        self.acc = Vector3(0)
        self.image_raw = pygame.image.load(image)
        self.w,self.h = size[0],size[1]
        self.max_acc = max_acc
        self.max_speed = max_speed
        self.image = pygame.transform.scale(self.image_raw,[self.w,self.h])
        self.rect = self.image.get_bounding_rect()
        self.acc_on = False
        self.lasers = []
        self.laser_color = (255,0,0)
        self.cooldown = 15
        self.time = self.cooldown
        self.fire = True
    
    def render(self,screen):
        self.rect.center = [self.pos[0],self.pos[1]]
        pos_adj = [self.pos[0] - (self.w/2),self.pos[1] - (self.h/2)]
        screen.blit(self.image,pos_adj)
        #pygame.draw.rect(screen,(0,0,255),self.rect)
        #pygame.draw.circle(screen,(255,255,0),[self.pos[0],self.pos[1]],5)


    def move(self):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acc[0] = -self.max_acc
            self.acc_on = True
        if keys[pygame.K_d]:
            self.acc[0] = self.max_acc
            self.acc_on = True
        if keys[pygame.K_w]:
            self.acc[1] = -self.max_acc
            self.acc_on = True
        if keys[pygame.K_s]:
            self.acc[1] = self.max_acc
            self.acc_on = True

        if self.acc_on != True:
            self.acc[0] = 0
            self.acc[1] = 0
            if self.vel.magnitude() > 0:
                d_acc = self.vel.magnitude() - self.max_acc
                if d_acc > 0:
                    self.vel.scale_to_length(d_acc)
        #if self.acc.magnitude() > self.max_acc:
            #self.acc.scale_to_length(self.max_acc)
        if self.vel.magnitude() > self.max_speed:
            self.vel.scale_to_length(self.max_speed)
        if self.vel.magnitude() > self.max_speed:
            self.vel.scale_to_length(self.max_speed)
        if self.pos[0] <= self.w/2:
            self.pos[0] = self.w/2
            self.vel[0] = 0
        if self.pos[0] >= SCREEN_WIDTH - self.w/2:
            self.pos[0] = SCREEN_WIDTH - self.w/2
            self.vel[0] = 0
        if self.pos[1] <= self.h/2:
            self.pos[1] = self.h/2
            self.vel[1] = 0
        if self.pos[1] >= SCREEN_HEIGHT - self.h/2:
            self.pos[1] = SCREEN_HEIGHT - self.h/2
            self.vel[1] = 0
        self.vel = self.vel + self.acc
        self.pos = self.pos + self.vel + (0.5)*self.acc
        self.acc_on = False

    def reticle(self,screen,r_z):
        size = [self.w,self.h]
        ret_pos = Tools.projectTo(self.pos[0],self.pos[1],p_z=r_z)
        ret_radius = 10
        ret_trail = []
        i = 0
        while r_z < (Tools.SPAWN_Z*(0.25)):
            ret_trail.append(Tools.projectTo(self.pos[0],self.pos[1],p_z=r_z))
            r_z += 15
            i += 1
        pygame.draw.circle(screen,(0,255,0),ret_pos,ret_radius,width = 1)
        trailing_r = 5
        for r in ret_trail:
            pygame.draw.circle(screen,(0,255,0),r,trailing_r)
            if trailing_r > 1:
                trailing_r -= .5
            else:
                trailing_r = 1

    def shoot(self,screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.fire:
            self.lasers.append(Projectile((self.pos[0],self.pos[1],0),100,8,self.laser_color))
            self.time = 0
        if len(self.lasers) > 0:
            for laser in self.lasers:
                laser.update(screen)
                if laser.destroyed == True:
                    self.lasers.remove(laser)
        if self.time >= self.cooldown:
            self.fire = True
        else:
            self.fire = False
            self.time += 1
        

    def update(self,screen,asteroids):
        self.reticle(screen,75)
        self.shoot(screen)
        self.render(screen)
        self.move()
        self.checkBulletCollision(asteroids)

    def checkBulletCollision(self,asteroids):
        for asteroid in asteroids:
            for laser in self.lasers:
                if asteroid.rect.collidepoint(laser.new_pos):
                    asteroid.destroyed = True
                    laser.destroyed = True
                    print("asteroid hit")
        

        
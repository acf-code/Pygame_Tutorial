import pygame
from pygame.math import Vector2
from random import randint
import tools


class Player:

    def __init__(self, pos, health, max_acc, image):
        self.pos = Vector2(pos)
        self.health = health
        self.max_health = health
        self.max_acc = max_acc
        self.max_speed = 3
        self.image_raw = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image_raw, [64, 64])
        self.rect = self.image.get_bounding_rect()
        self.health_rect = pygame.Rect([10,465],[self.health,25])
        self.damage_rect = pygame.Rect([10,465],[self.max_health,25])
        self.vel = Vector2(0)
        self.acc = Vector2(0)
        self.invincibility = 60
        self.time = 0
        self.start_frame = 0
        self.fps = tools.fps

    def move(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.acc[0] = self.max_acc
                    self.time,self.start_frame = tools.increase_time(self.time,self.start_frame,self.fps)
                if event.key == pygame.K_LEFT:
                    self.acc[0] = -self.max_acc
                    self.time,self.start_frame = tools.increase_time(self.time,self.start_frame,self.fps)
                if event.key == pygame.K_UP:
                    self.acc[1] = -self.max_acc
                    self.time,self.start_frame = tools.increase_time(self.time,self.start_frame,self.fps)
                if event.key == pygame.K_DOWN:
                    self.acc[1] = self.max_acc
                    self.time,self.start_frame = tools.increase_time(self.time,self.start_frame,self.fps)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.acc[0] = 0
                    self.time = 0
                    self.start_frame = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.acc[1] = 0
                    self.acc[0] = 0
                    self.time = 0
                    self.start_frame = 0
        if self.acc.magnitude() > self.max_acc:
            self.acc.scale_to_length(self.max_acc)
        if self.vel.magnitude() > self.max_speed:
            self.vel.scale_to_length(self.max_speed)
        if self.pos[0] <= 0:
            self.pos[0] = 0
            self.vel[0] = 0
        if self.pos[0] >= 436:
            self.pos[0] = 436
            self.vel[0] = 0
        if self.pos[1] <= 0:
            self.pos[1] = 0
            self.vel[1] = 0
        if self.pos[1] >= 436:
            self.pos[1] = 436
            self.vel[1] = 0
        self.vel = self.vel + self.acc
        self.pos = self.pos + self.vel + (0.5)*self.acc
        
        

    def render(self,screen):
        screen.blit(self.image, self.pos)
        self.rect.center = [self.pos[0] + 32, self.pos[1] + 32]
        pygame.draw.rect(screen,tools.red,self.damage_rect)
        pygame.draw.rect(screen,tools.green,self.health_rect)
        #pygame.draw.rect(screen, white, self.rect)

    def update(self, events,screen):
        self.move(events)
        self.render(screen)
        if self.invincibility<60:
            self.invincibility+=1
        
    def damage(self):
        if self.invincibility>=60:
            self.health -= 10
            self.health_rect = pygame.Rect([10,465],[self.health,25])  
            self.invincibility = 0

class Enemy:
    #method is a funtion inside the class
    #the first method for any class is called the constructor method
    def __init__(self, pos, health, size, color):
        #instance variables from these parameters
        self.pos = pos
        self.health = health
        self.size = size
        self.area = self.size[0] * self.size[1]
        self.color = color
        self.save_color = color
        self.max_speed = 5 - (self.area / 1500)
        self.velocity = Vector2(randint(1, 7), randint(1, 7))
        self.rect = pygame.Rect(self.pos, self.size)
        self.hit_timer = tools.fps

    def move(self):
        if self.velocity.magnitude() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)
        if self.pos[0] < 0:
            self.pos[0] = 0
            self.velocity[0] = -self.velocity[0]
        if self.pos[0] > 500:
            self.pos[0] = 500
            self.velocity[0] = -self.velocity[0]
        if self.pos[1] < 0:
            self.pos[1] = 0
            self.velocity[1] = -self.velocity[1]
        if self.pos[1] > 500:
            self.pos[1] = 500
            self.velocity[1] = -self.velocity[1]
        self.pos += self.velocity
        self.rect.topleft = self.pos

    def render(self,screen):
        if self.hit_timer < tools.fps:
            self.color = tools.red
            self.hit_timer += 1
        else:
            self.color = self.save_color
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self,screen):
        self.move()
        self.render(screen)

    def attack(self):
        pass

    def damage(self):
        self.health -= 1
        self.hit_timer = 0

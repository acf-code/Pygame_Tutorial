import pygame
from pygame.math import Vector2

class Enemy:

    def __init__(self,start_x,start_y,w,h,color,speed):
        self.pos = Vector2(start_x,start_y)
        self.w = w
        self.h = h
        self.image = pygame.image.load("followingAI/enemy.png").convert_alpha()
        self.image.set_colorkey([255,255,255])
        self.image = pygame.transform.scale(self.image,[self.w,self.h])
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(0,0,self.w,self.h)
        self.vel = Vector2(0)
        self.direction = Vector2(0,-1)
        self.following = False
        self.follow_distance = 250
        self.stop_distance = 50

    def findPlayer(self,player):
        distanceFromPlayer = self.pos.distance_to(player.pos)
        if distanceFromPlayer <= self.follow_distance and distanceFromPlayer >= self.stop_distance:
            self.following = True
        else:
            self.following = False


    def move(self,player):
        if self.following:
            self.direction = player.pos - self.pos
            self.direction = self.direction.normalize()
            self.vel = self.direction * self.speed
        else:
            self.vel = Vector2(0)

        self.pos += self.vel
        self.rect.center = self.pos

    def render(self,screen):
        #pygame.draw.rect(screen,self.color,self.rect)
        up = Vector2(0, -1)
        angleFromUp = up.angle_to(self.direction)
        # Rotate the player's image based on its direction
        image_rot = pygame.transform.rotate(self.image, -angleFromUp).convert_alpha()
        image_rect = image_rot.get_rect(center=self.pos)
        screen.blit(image_rot,image_rect)

    def update(self,player):
        self.findPlayer(player)
        self.move(player)


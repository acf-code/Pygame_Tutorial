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
        self.follow_distance_not_found = 50
        self.follow_distance_found = 150
        self.follow_distance = self.follow_distance_not_found
        self.stop_distance = 10
        self.viewAngle = 45

    def findPlayer(self,player,screen):
        distanceVector = self.pos - player.pos
        distanceVector = distanceVector.normalize() * player.detectRadius
        distantPoint = distanceVector + player.pos
        distanceFromPlayer = self.pos.distance_to(distantPoint)
        if distanceFromPlayer <= self.follow_distance and distanceFromPlayer >= self.stop_distance:
            self.follow_distance = self.follow_distance_found
            self.following = self.checkViewAngle(distanceVector,screen)
        else:
            self.follow_distance = self.follow_distance_not_found
            steps = 100
            for i in range(steps):
                pygame.draw.line(screen,[255,0,0],self.pos,self.pos + self.direction.rotate(pygame.math.lerp(0,self.viewAngle,i/steps))*self.follow_distance)
            for i in range(steps):
                pygame.draw.line(screen,[255,0,0],self.pos,self.pos + self.direction.rotate(-pygame.math.lerp(0,self.viewAngle,i/steps))*self.follow_distance)
            #pygame.draw.line(screen,[0,255,0],self.pos,self.pos + self.direction.rotate(self.viewAngle)*self.follow_distance)
            self.following = False


    def checkViewAngle(self,distanceVector,screen):
        steps = 100
        for i in range(steps):
            pygame.draw.line(screen,[0,255,0],self.pos,self.pos + self.direction.rotate(pygame.math.lerp(0,self.viewAngle,i/steps))*self.follow_distance)
        for i in range(steps):
            pygame.draw.line(screen,[0,255,0],self.pos,self.pos + self.direction.rotate(-pygame.math.lerp(0,self.viewAngle,i/steps))*self.follow_distance)
        angleToPlayer = self.direction.angle_to(distanceVector)
        if angleToPlayer > 0:
            angleToPlayer -= 180
        elif angleToPlayer < 0:
            angleToPlayer += 180
        print(angleToPlayer)
        if angleToPlayer > -self.viewAngle and angleToPlayer < self.viewAngle:
            pygame.draw.line(screen,[255,0,0],self.pos,self.pos + self.direction.rotate(angleToPlayer)*self.follow_distance)
            return True
        else:
            pygame.draw.line(screen,[255,255,0],self.pos,self.pos + self.direction.rotate(angleToPlayer)*self.follow_distance)
            return False




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

    def update(self,player,screen):
        self.findPlayer(player,screen)
        self.move(player)


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

    def move(self,keys):
        moving = False
        vel = Vector2(0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            vel[0] = self.speed
            moving = True
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            vel[0] = -self.speed
            moving = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            vel[1] = -self.speed
            moving = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            vel[1] = self.speed
            moving = True
        if not moving:
            vel = Vector2(0)
        if vel != Vector2(0):
            vel = vel.normalize()
        vel[0] *= self.speed
        vel[1] *= self.speed
        self.x += vel[0]
        self.y += vel[1]

        

    def render(self,screen):
        self.rect.center = [self.x,self.y]
        pygame.draw.rect(screen,[255,0,0],self.rect)
        #pygame.draw.circle(screen,[255,0,0],[self.x,self.y],self.rect.w)

    def update(self,screen,keys):
        self.move(keys)
        self.render(screen)

class Dagger:
    def __init__(self,x,y,w,h,image):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,w,h)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,[self.rect.w,self.rect.h])

    def render(self,screen,player,mPos):
        #finding angle between pos and mouse pos
        angle = math.atan2(mPos[1]-player.y,mPos[0]- player.x)*180/math.pi + 90
        #rotating image based on the angle
        image_rot = pygame.transform.rotate(self.image,angle*-1)
        #getting current rect that is covering the image
        image_rect = image_rot.get_rect()
        #setting that rect center position to be equal to the dagger pos
        image_rect.center= [self.x,self.y]
        #pygame.draw.rect(screen,[0,0,255],image_rect)
        #drawing the dagger on the screen using the image_rect
        screen.blit(image_rot,image_rect)

    def move(self,player,mPos):
        #setting the distance of dagger to player to be dist_from_player 
        dist_from_player = 100
        mPos = Vector2(mPos)
        pos = mPos - Vector2(player.x,player.y)
        pos.scale_to_length(dist_from_player)
        self.x = player.x + pos[0]
        self.y = player.y + pos[1]


    def update(self,screen,mPos,player):
        self.render(screen,player,mPos)
        self.move(player,mPos)

player = Player(WIDTH/2,HEIGHT/2,36,36)
dagger = Dagger(WIDTH/2,HEIGHT/2,16,32,"dagger.png")

while True:
    mPos = pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    screen.fill([0,0,0])
    player.update(screen,keys)
    dagger.update(screen,mPos,player)
    pygame.display.update()
    clock.tick(fps)




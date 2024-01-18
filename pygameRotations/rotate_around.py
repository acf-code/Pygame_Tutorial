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
        vel = Vector2(0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            vel[0] = self.speed
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            vel[0] = -self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            vel[1] = -self.speed
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            vel[1] = self.speed
        if vel != Vector2(0):
            vel = vel.normalize()
            vel[0] *= self.speed
            vel[1] *= self.speed
        self.x += vel[0]
        self.y += vel[1]

        

    def render(self,screen):
        self.rect.center = [self.x,self.y]
        pygame.draw.rect(screen,[255,0,0],self.rect)
        #pygame.draw.circle(screen,[255,0,0],[self.x,self.y],10)

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

    def render_vector(self,screen,player,mPos):
        up = Vector2(0,-1)
        #finding angle between pos and mouse pos
        direction = Vector2(mPos[0]-player.x,mPos[1] - player.y)
        angle = up.angle_to(direction)
        # angle = math.acos(up.dot(pos)/(up.magnitude()*pos.magnitude()))*180/math.pi
        # if mPos[0] - player.x > 0:
        #     angle *= -1
        print(angle)
        #rotating image based on the angle
        image_rot = pygame.transform.rotate(self.image,-angle)
        #getting current rect that is covering the image
        image_rect = image_rot.get_rect()
        #setting that rect center position to be equal to the dagger pos
        image_rect.center= [self.x,self.y]
        #pygame.draw.rect(screen,[0,0,255],image_rect)
        #drawing the dagger on the screen using the image_rect
        screen.blit(image_rot,image_rect)

    def move(self,player,mPos):
        #setting the distance of dagger to player to be dist_from_player 
        dist_from_player = 50
        mPos = Vector2(mPos)
        pos = mPos - Vector2(player.x,player.y)
        pos.scale_to_length(dist_from_player)
        self.x = player.x + pos[0]
        self.y = player.y + pos[1]
        pygame.draw.line(screen,[0,255,0],[player.x,player.y],[self.x,self.y])


    def update(self,screen,mPos,player):
        self.render_vector(screen,player,mPos)
        self.move(player,mPos)

player = Player(WIDTH/2,HEIGHT/2,36,36)
dagger = Dagger(WIDTH/2,HEIGHT/2,16,32,"pygameRotations/dagger.png")

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




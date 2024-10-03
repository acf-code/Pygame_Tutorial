import pygame,sys
from pygame.math import Vector2,Vector3,lerp
import numpy as np

class Body:
    def __init__(self,startX,startY,width = 96,height = 16):
        self.up = Vector3(0,-1,0)
        self.pos = Vector3(startX,startY,0)
        self.size = Vector2(width,height)
        self.updateJoints()

    def updateJoints(self):
        self.right = self.up.rotate(90,[0,0,1])
        self.forward = self.up.rotate(-90,[1,0,0])
        self.rShoulderJoint = self.pos + self.right*self.size[0]//2
        self.lShoulderJoint = self.pos - self.right*self.size[0]//2

    def render(self,screen):
        leftJoint = Vector2(self.lShoulderJoint.x,self.lShoulderJoint.y)
        rightJoint = Vector2(self.rShoulderJoint.x,self.rShoulderJoint.y)
        up = Vector2(self.up.x,self.up.y)
        pos = Vector2(self.pos.x,self.pos.y)
        up.scale_to_length(self.size[1])
        pygame.draw.line(screen,"green",leftJoint,rightJoint)
        pygame.draw.line(screen,"cyan",pos,up+pos)

    def update(self):
        #self.rotateToMouse()
        self.updateJoints()


if __name__ == "__main__":
    pygame.init()
    SWIDTH = 800
    SHEIGHT = 640
    screen = pygame.display.set_mode([SWIDTH,SHEIGHT])
    clock = pygame.time.Clock()
    fps = 60
    body = Body(SWIDTH/2,SHEIGHT/2)
    dt = 0

    font = pygame.font.SysFont(None,12)

    def displayText(text,pos,screen):
        t = font.render(text, True, "white")
        screen.blit(t,t.get_rect(center = pos))

    rot = 0


    while True:
        pygame.display.set_caption(str(clock.get_fps()))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rot = 100
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    rot = 0
        screen.fill("black")
        body.render(screen)
        body.update()
        body.up.rotate_ip(rot*dt/1000,[0,0,1])
        dt = clock.tick(fps)
        pygame.display.flip()

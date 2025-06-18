import pygame,sys
from pygame.math import Vector2,Vector3,lerp
import numpy as np

class Body:
    def __init__(self,startX,startY,width = 96,height = 16):
        self.pos = Vector3(startX,startY,0)
        self.forward = Vector3(0,-1,0)
        self.size = Vector2(width,height)
        self.updateJoints()
        self.rightArm = Arm(self.rightJoint,self.right)
        
    def updateJoints(self):
        self.right = self.forward.rotate(90,[0,0,1])
        self.leftJoint = self.pos - self.right*self.size[0]//2
        self.rightJoint = self.pos + self.right*self.size[0]//2

    def render(self,screen):
        leftJoint = Vector2(self.leftJoint.x,self.leftJoint.y)
        rightJoint = Vector2(self.rightJoint.x,self.rightJoint.y)
        pygame.draw.line(screen,"green",leftJoint,rightJoint)
        self.rightArm.render(screen)

    def update(self):
        #self.rotateToMouse()
        self.updateJoints()
        self.rightArm.update(self.right,self.rightJoint)

    def rotateToMouse(self):
        direction = Vector3(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],0) - self.pos
        self.forward = direction.normalize()

class Arm:
    def __init__(self,shoulderJoint,forward,armLength = 32):
        self.shoulderJoint = shoulderJoint
        self.forward = forward
        self.right = self.forward.rotate(90,[0,0,1])
        self.fullArmLength = armLength
        self.armLength = self.fullArmLength
        self.wristJoint = self.shoulderJoint + self.forward*self.armLength
        self.maxTwistAngle = 120
        self.angle = 0

    def render(self,screen):
        shoulderJoint = Vector2(self.shoulderJoint.x,self.shoulderJoint.y)
        wristJoint = Vector2(self.wristJoint.x,self.wristJoint.y)
        pygame.draw.line(screen,"red",shoulderJoint,wristJoint)

    def updateJoints(self,refForward,shoulderJoint):
        self.shoulderJoint = shoulderJoint
        self.right = refForward.rotate(90,[0,0,1])
        self.wristJoint = self.shoulderJoint + self.forward*self.armLength

    def update(self,refForward,shoulderJoint):
        self.updateForward(refForward)
        self.updateJoints(refForward,shoulderJoint)

    def updateForward(self,refForward):
        #constrain arm to angle
        forward = self.rotateToMouse()
        angle = forward.angle_to(refForward)
        refLeft = refForward.rotate_z(-90)
        if angle < self.maxTwistAngle:
            self.forward = forward
            self.angle = angle
        else:
            if refLeft.y < 0:
                if self.forward.y > refForward.y:
                    self.angle = self.maxTwistAngle
                    self.forward = refForward.rotate_z(self.maxTwistAngle)
                else:
                    self.angle = -self.maxTwistAngle
                    self.forward = refForward.rotate_z(-self.maxTwistAngle)
            elif refLeft.y > 0:
                if self.forward.y > refForward.y:
                    self.angle = -self.maxTwistAngle
                    self.forward = refForward.rotate_z(-self.maxTwistAngle)

                else:
                    self.angle = self.maxTwistAngle
                    self.forward = refForward.rotate_z(self.maxTwistAngle)
                    
                
        
    
    def rotateToMouse(self):
        direction = Vector3(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],0) - self.shoulderJoint
        # if direction.magnitude() < self.fullArmLength:
        #     self.armLength = direction.magnitude()
        # else:
        #     self.armLength = self.fullArmLength
        return direction.normalize()

    



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
        screen.fill("black")
        body.render(screen)
        body.update()
        displayText(str(body.rightArm.angle),[100,50],screen)
        body.forward.rotate_z_ip(rot)
        dt = clock.tick(fps)
        pygame.display.flip()
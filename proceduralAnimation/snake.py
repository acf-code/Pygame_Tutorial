import pygame
from pygame.math import Vector2,lerp
from pygame.gfxdraw import filled_polygon,textured_polygon
import random
import math
import texture

class Snake:
    def __init__(self):
        self.headPos = Vector2(250,250)
        self.headSize = 25
        self.color = [0,0,0]
        self.segmentLength = 25
        self.numOfJoints = 10
        self.startWidth = self.headSize
        self.endWidth = 5
        self.body = self.createBody()
        self.angleConstrain = 90
        self.v1 = Vector2(0)
        self.v2 = Vector2(0)
        self.texture = texture.Texture(500,500)

    def update(self):
        #check if mousebutton is pressed down
        if pygame.mouse.get_pressed()[0]:
            #update snake head pos
            mPos = Vector2(pygame.mouse.get_pos())
            self.headPos = mPos
        self.updateBody() #update the body Joints to follow the head

    def draw(self,screen):
        self.texture.update()
        #draw snake head
        pygame.draw.circle(screen,self.color,self.headPos,self.headSize)
        #draw snake body
        points = []
        for i in range(self.numOfJoints):
            width = lerp(self.startWidth,self.endWidth,i/(self.numOfJoints-1))
            if i == 0:
                direction = self.body[i] - self.headPos
                direction.normalize_ip()
                normal = Vector2(-direction.y,direction.x)
                pos = self.headPos + normal*width
                points.append(pos)
            else:
                direction = self.body[i] - self.body[i-1]
                direction.normalize_ip()
                normal = Vector2(-direction.y,direction.x)
                pos = self.body[i] + normal*width
                points.append(pos)
        reversePoints = []
        for i in range(self.numOfJoints):
            width = lerp(self.startWidth,self.endWidth,i/(self.numOfJoints-1))
            if i == 0:
                direction = self.body[i] - self.headPos
                direction.normalize_ip()
                normal = -1 *Vector2(-direction.y,direction.x)
                pos = self.headPos + normal*width
                reversePoints.append(pos)
            else:
                direction = self.body[i] - self.body[i-1]
                direction.normalize_ip()
                normal = -1 *Vector2(-direction.y,direction.x)
                pos = self.body[i] + normal*width
                reversePoints.append(pos)
        reversePoints.reverse()
        points.extend(reversePoints)
        #filled_polygon(screen,points,[0,0,255])
        textured_polygon(screen,points,self.texture.texture,0,0)
        #draw the tail of the snake
        pygame.draw.circle(screen,self.color,self.body[-1],self.endWidth)
        # pygame.draw.line(screen,"red",self.body[0],self.body[0] + self.v1,3)
        # pygame.draw.line(screen,"red",self.body[0],self.body[0] + self.v2,3)

            

    def createBody(self):
        body = []
        for i in range(self.numOfJoints):
            joint = Vector2(self.headPos.x - self.segmentLength*(i+1),self.headPos.y)
            body.append(joint)
        return body
    
    def updateBody(self):
        oldBody = self.body
        for i in range(self.numOfJoints):
            if i == 0:
                #direction from the first joint to the head pos
                direction = oldBody[i] - self.headPos
                if direction != Vector2(0):
                    direction.normalize_ip()
                v1 = self.headPos - oldBody[i]
                v2 = oldBody[i + 1] - oldBody[i]
                if self.getAngle(v1,v2) < self.angleConstrain:
                    pass
                pos = self.headPos + direction*self.segmentLength
                oldBody[i] = pos
            else:
                #direction from the previous join to the current joint
                direction = oldBody[i] - oldBody[i-1]
                if direction != Vector2(0):
                    direction.normalize_ip()
                if i + 1 < self.numOfJoints:
                    v1 = oldBody[i-1] - oldBody[i]
                    v2 = oldBody[i+1] - oldBody[i]
                    if self.getAngle(v1,v2) < self.angleConstrain:
                        #print(self.getAngle(v1,v2))
                        pass
                pos = oldBody[i-1] + direction*self.segmentLength
                oldBody[i] = pos
        self.body = oldBody

    def getAngle(self,v1,v2):
        v1Normalized = v1.normalize()
        v2Normalized = v2.normalize()
        angle = math.acos(v1Normalized.dot(v2Normalized))
        angle = math.degrees(angle)
        return angle


"""
First Things I want to do:
1.intialize a snake "head"
2.this snake head will need a position(Vector2), and it will need a size (radius)
3.set a color for the snake head
4.in the update, I want the snake head position to always follow the mouse position if the left mouse button(single press on trackpad) is being pressed down
5.in the draw method, I want to draw the snake head as a circle with the size as the radius of the circle
"""

"""
Second Things I want to do:
1.intialize my snake "body"
2.I want to have 3 snake "body" joints, each body joint will be a vector pos
3.I want each joint to be equally spaced apart by some body length
4.in the draw method, I want to draw each joint as a circle and connect each joint and head with a line
"""

"""
Third Things I want to do:
1. in the update, I want the body joints to follow the head pos
2. I need to make sure that the length between each joint and body stays the same
3. I need to make sure that the direction from the joint to the previous joint is pointing correctly
"""


"""
MISC. INFO

Vector2: is a special list, that only contains two values. These values are usally a position in the x direction and a position in the y direction
a vector2 is usually a coordinate position
"""
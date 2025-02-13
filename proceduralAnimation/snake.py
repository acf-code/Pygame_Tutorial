import pygame
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.headPos = Vector2(250,250)
        self.headSize = 5
        self.color = "cyan"
        self.segmentLength = 32
        self.numOfJoints = 10
        self.body = self.createBody() 

    def update(self):
        #check if mousebutton is pressed down
        if pygame.mouse.get_pressed()[0]:
            #update snake head pos
            mPos = Vector2(pygame.mouse.get_pos())
            self.headPos = mPos
        self.updateBody() #update the body Joints to follow the head

    def draw(self,screen):
        #draw snake head
        pygame.draw.circle(screen,self.color,self.headPos,self.headSize)
        #draw snake body
        for i in range(self.numOfJoints):
            if i == 0:
                pygame.draw.circle(screen,self.color,self.body[i],self.headSize)
                pygame.draw.line(screen,self.color,self.headPos,self.body[i])
            else:
                pygame.draw.circle(screen,self.color,self.body[i],self.headSize)
                pygame.draw.line(screen,self.color,self.body[i-1],self.body[i])

    def createBody(self):
        body = []
        for i in range(self.numOfJoints):
            joint = Vector2(self.headPos.x - self.segmentLength*(i+1),self.headPos.y)
            body.append(joint)
        return body
    
    def updateBody(self):
        oldBody = self.body
        newBody = []
        for i in range(self.numOfJoints):
            if i == 0:
                #direction from the first joint to the head pos
                direction = oldBody[i] - self.headPos
                direction.normalize_ip()
                pos = self.headPos + direction*self.segmentLength
                newBody.append(pos)
            else:
                #direction from the previous join to the current joint
                direction = oldBody[i] - oldBody[i-1]
                direction.normalize_ip()
                pos = oldBody[i-1] + direction*self.segmentLength
                newBody.append(pos)
        self.body = newBody


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
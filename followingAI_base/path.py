import pygame

class Paths:
    def __init__(self,points):
        self.points = points

    def render(self,screen):
        pointsLength = len(self.points)
        for i in range(pointsLength - 1):
            pygame.draw.line(screen,[0,255,0],self.points[i],self.points[i+1])

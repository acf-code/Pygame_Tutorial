import pygame
import random
from pygame.math import Vector2,lerp

# def createTexture(width,height):
#     texture = pygame.Surface([width,height])
#     texture.fill("black")
#     for i in range(500):
#         if random.randint(1,100) <= 1:
#             radius = random.randint(1,4)
#             color = [255,255,255]
#             pos = Vector2(random.randint(0,500),random.randint(0,500))
#             pygame.draw.circle(texture,color,pos,radius)
#     return texture

class Star:
    def __init__(self,boundX,boundY,velocity):
        self.boundX = boundX
        self.boundY = boundY
        self.createStar()
        self.startColor = [75,75,75]
        self.endColor = [255,255,255]
        self.vel = Vector2(velocity)
    
    def createStar(self):
        self.pos = Vector2(random.randint(0,self.boundX),random.randint(0,self.boundY))
        self.maxZ = 400
        self.z = random.randint(0,self.maxZ)

    def draw(self,surface):
        color_r = lerp(self.startColor[0],self.endColor[0],self.z/self.maxZ)
        color_g = lerp(self.startColor[1],self.endColor[1],self.z/self.maxZ)
        color_b = lerp(self.startColor[2],self.endColor[2],self.z/self.maxZ)
        color = [color_r,color_g,color_b]
        pygame.draw.circle(surface,color,self.pos,self.z/100)

    def update(self):
        self.pos += self.vel
        if self.pos.x < 0:
            self.createStar()
            self.pos.x = self.boundX
        elif self.pos.x > self.boundX:
            self.createStar()
            self.pos.x = 0
        if self.pos.y < 0:
            self.createStar()
            self.pos.y = self.boundY
        elif self.pos.y > self.boundY:
            self.createStar()
            self.pos.y = 0

class Texture:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.texture = pygame.Surface([width,height])
        self.stars = []
        self.numOfStars = 400
        self.starVel = Vector2(0,3)
        for i in range(self.numOfStars):
            self.stars.append(Star(width,height,self.starVel))

    def update(self):
        self.texture.fill("black")
        self.stars.sort(key= lambda star : star.z, reverse= True)
        for star in self.stars:
            star.draw(self.texture)
            star.update()



if __name__ == "__main__":
    SWIDTH, SHEIGHT = 500,500
    screen = pygame.display.set_mode([SWIDTH,SHEIGHT])
    clock = pygame.time.Clock()
    fps = 60
    texture = Texture(SWIDTH,SHEIGHT)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill("black")
        screen.blit(texture.texture,[0,0])
        texture.update()
        clock.tick(fps)
        pygame.display.update()
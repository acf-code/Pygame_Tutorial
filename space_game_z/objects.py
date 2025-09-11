import pygame
import math
import random
from pygame.math import Vector2,Vector3

class Tools:

    SPAWN_Z = 2000
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 640

    @staticmethod
    def projectTo(t_x,t_y,p_z = SPAWN_Z,screen_w = SCREEN_WIDTH, screen_h = SCREEN_HEIGHT):
        if screen_w + p_z == 0:
            p_x = 0
            p_cx = 0
        else:
            p_x = (screen_w*((t_x)/(screen_w + p_z)))
            p_cx = (screen_w*((screen_w/2)/(screen_w + p_z)))
        if screen_h + p_z == 0:
            p_y = 0
            p_cy = 0
        else:
            p_y = (screen_h*((t_y)/(screen_h + p_z)))
            p_cy = (screen_h*((screen_h/2)/(screen_h + p_z)))
        center = [screen_w/2,screen_h/2]
        offset= [center[0]- p_cx,center[1]- p_cy]
        p_x += offset[0]
        p_y += offset[1]
        pos = Vector2(p_x,p_y)               
        return pos
    
    @staticmethod
    def random_hexagon(max_w,max_h,screen_w = SCREEN_WIDTH, screen_h = SCREEN_HEIGHT):
        vertices = []
        cx = max_w / 2
        cy = max_h / 2
        r = min(max_w, max_h) / 2
        v_x = []
        v_y = []
        pos = [random.randint(0,(screen_w - max_w)),random.randint(0,(screen_h-max_h))]
        for i in range(6):
            x = cx + r * math.cos(i * math.pi / 3) + random.randint(-1,1)*random.randint(-20,20)
            y = cy + r * math.sin(i * math.pi / 3) + random.randint(-1,1)*random.randint(-20,20)
            v_x.append(x)
            v_y.append(y)
        for i in range(6):
            vertices.append([v_x[i] + pos[0],v_y[i] + pos[1]])
        return vertices
        

class Projectile:

    def __init__(self,pos,speed,radius,color):
        self.pos = Vector3(pos)
        self.new_pos = Vector2(pos[0],pos[1])
        self.speed = speed
        self.t_radius = radius
        self.radius = self.t_radius
        self.r_scale = .5
        self.color = color
        self.destroyed = False

    def render(self,screen):
        if self.pos[2] != 0 and self.radius > 1:
            self.r_scale = .5
            self.radius = self.radius - self.r_scale
        elif self.pos[2] == 0:
            self.radius = self.t_radius
        else:
            self.radius = 1
        pygame.draw.circle(screen,self.color,self.new_pos,self.radius)
        
    def move(self):
        self.pos[2] += self.speed
        self.new_pos = Tools.projectTo(self.pos[0],self.pos[1],self.pos[2])

    def destroy(self):
        if self.pos[2] >= Tools.SPAWN_Z:
            self.destroyed = True

    def update(self,screen):
        self.render(screen)
        self.move()
        self.destroy()

class Asteroid:
    def __init__(self,speed,color,verticies):
        self.speed = speed
        self.color = color
        self.verticies = verticies
        self.p_verticies = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.z = Tools.SPAWN_Z-1950
        for i in range(len(self.verticies)):
            self.p_verticies[i] = Tools.projectTo(abs(self.p_verticies[i][0]),abs(self.p_verticies[i][1]),p_z = self.z)
        self.destroyed = False
        self.pos = [random.randint(0,800),random.randint(0,600)]
        self.new_pos = self.pos
        

    def render(self,screen):
        pygame.draw.rect(screen,"red",)
        #pygame.draw.polygon(screen,self.color,self.p_verticies)
        #pygame.draw.circle(screen,self.color,self.new_pos,10)

    def move(self):
        self.z -= self.speed
        self.new_pos = Tools.projectTo(self.pos[0],self.pos[1],self.z)

    def destroy(self):
        if self.z < 0:
            self.destroyed = True

    def update(self,screen):
        self.render(screen)
        self.move()
        self.destroy()
#Code for platforming
import pygame
from pygame import Vector2
from random import randint

pygame.init()

#game_setup code

size = [500,500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
speed = 5
jumpCount = 10
gravity = 100
platforms = []

#Set up player
class Player:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.mass = 6
        self.isJump = False
        self.canJump = True
        self.jumpTimer = 5
        self.rect1 = pygame.Rect(self.x, self.y, 50, 50)

    def draw(self):
        # update rect1
        self.rect1 = pygame.Rect(self.x, self.y, 50, 50)
        pygame.draw.rect(screen, (255,0,0), self.rect1)

    def check_collide(self, platforms:list, velocity:Vector2):
        if self.rect1.right + velocity[0] > size[0]:
            self.dx = size[0] - self.rect1.right
            velocity[0] = 0
        else:
            self.dx = velocity[0]
        
        if self.rect1.left + velocity[0] < 0:
            self.dx = 0
            velocity[0] = 0
        else:
            self.dx = velocity[0]

        #collision code for bottom of the screen
        if self.rect1.bottom + velocity[1] > size[1]:
            self.canJump = True
            self.dy = size[1] - self.rect1.bottom
            velocity[1] = 0
        else:
            self.dy = velocity[1]

        #collision code with platorms
        for p in platforms:
            #if the change in y will hit the platform, change dy to be the distance from the bottom of player and top of platform
            #change v_y to be zero
            if p.colliderect(pygame.Rect(self.rect1.x, self.rect1.y + self.dy, self.rect1.w, self.rect1.h)) and self.dy > 0:
                self.dy = p.top - self.rect1.bottom
                if self.dy < 0:
                    self.dy = 0
                velocity[1] = 0
                self.canJump = True
            if p.colliderect(pygame.Rect(self.rect1.x, self.rect1.y + self.dy, self.rect1.w, self.rect1.h)) and self.dy < 0:
                self.dy = p.bottom - self.rect1.top
                if self.dy > 0:
                    self.dy = 0
                velocity[1] = 0
            elif p.colliderect(pygame.Rect(self.rect1.x + self.dx, self.rect1.y, self.rect1.w, self.rect1.h)) and self.dx < 0:
                self.dx = p.right - self.rect1.left
                velocity[0] = 0
            elif p.colliderect(pygame.Rect(self.rect1.x + self.dx, self.rect1.y, self.rect1.w, self.rect1.h)) and self.dx > 0:
                self.dx = p.left - self.rect1.right
                velocity[0] = 0
    

    def jump(self, velocity:Vector2):
        if self.isJump:
            F = (0.5)*self.mass*(self.jumpTimer**2)
            velocity[1] -= F
            self.jumpTimer = self.jumpTimer - 1
            if self.jumpTimer == 0:
                # making isjump equal to false  
                self.isJump = False
                # setting original values to v and m 
                self.jumpTimer = 5
        else:
            if pressed_keys[pygame.K_SPACE]:
                if self.canJump:
                    self.canJump = False
                    self.isJump = True
            else:
                self.isJump = False

    def update_move(self):
        velocity = Vector2(0,0)
        velocity[1] += gravity*tick
        if pressed_keys[pygame.K_RIGHT]:
            velocity[0] = speed
        elif pressed_keys[pygame.K_LEFT]:
            velocity[0] = -speed
        self.jump(velocity)
        self.dx = velocity[0]
        self.dy = velocity[1]
        self.check_collide(platforms, velocity)

        #update the player position with dx and dy
        self.x += self.dx
        self.y += self.dy
        


#adding platforms
def init_platforms(platforms:list):
    while(len(platforms) < 7):
        collide = False
        tplat = pygame.Rect(randint(0,size[0]-100),randint(50,size[1]-20),100,20)
        for p in platforms:
            # ensure player-sized gap
            if tplat.colliderect(pygame.Rect(p.x-50, p.y-50, p.w+100, p.h+100)):
                collide = True
        if not collide:
            platforms.append(tplat)

#gameloop code
pl = Player(0, 0)    

init_platforms(platforms)

while True:
    events = pygame.event.get()
    pressed_keys = pygame.key.get_pressed()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    tick = clock.get_time()/100
    
    screen.fill([0,0,0])
            
    for p in platforms:
        pygame.draw.rect(screen,[0,0,255],p)
    
    pl.update_move()
    pl.draw()
    pygame.display.update()
    clock.tick(fps)
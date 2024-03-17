#Code for platforming
import pygame
from pygame import Vector2


pygame.init()

#game_setup code

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()
fps = 60

class PhysicObject:
    GRAVITY = 10
    TOLERANCE = 1
    def __init__(self,x,y,w,h,jumpSpeed = 7):
        self.surf = pygame.Surface((w,h))
        self.rect = self.surf.get_rect(center = (x,y))
        self.vel = Vector2(0)
        self.dx = 0
        self.dy = 0
        self.grounded = False
        self.jumpSpeed = jumpSpeed
        self.jumping = False
        self.friction = 0
    def move_x(self,x_acc,dt):
        self.vel[0] = x_acc
        self.dx = self.vel[0]
    def move_y(self,dt):
        self.vel[1] += PhysicObject.GRAVITY*dt
        self.dy = self.vel[1]
    def groundCollision(self):
        if self.rect.bottom + self.dy > HEIGHT:
            self.dy = HEIGHT - self.rect.bottom
            self.vel[1] = 0
            self.grounded = True

        if self.rect.left + self.dx < 0:
            self.dx = -self.rect.left
            self.vel[0] = 0

        if self.rect.right + self.dx > WIDTH:
            self.dx = WIDTH - self.rect.right
            self.vel[0] = 0

    def platformCollision(self,plaforms):
        for platform in plaforms:
            if platform.rect.colliderect(pygame.Rect(self.rect.x, self.rect.y + self.dy,self.rect.w,self.rect.h)) and self.dy > 0:
                    self.dy = platform.rect.top - self.rect.bottom
                    self.vel[1] = 0
                    self.grounded = True
            elif platform.rect.colliderect(pygame.Rect(self.rect.x, self.rect.y + self.dy,self.rect.w,self.rect.h)) and self.dy < 0:
                    self.dy = platform.rect.bottom - self.rect.top
                    self.vel[1] = 0
            elif platform.rect.colliderect(pygame.Rect(self.rect.x + self.dx, self.rect.y,self.rect.w,self.rect.h)) and self.dx > 0:
                    self.dx = platform.rect.left - self.rect.right
                    self.vel[0] = 0
            elif platform.rect.colliderect(pygame.Rect(self.rect.x + self.dx, self.rect.y,self.rect.w,self.rect.h)) and self.dx < 0:
                    self.dx = platform.rect.right - self.rect.left
                    self.vel[0] = 0


    
    def jump(self):
        if self.grounded:
            self.vel[1] = -self.jumpSpeed
            self.dy = self.vel[1]

    def update(self,x_acc,dt,platforms):
        self.move_x(x_acc,dt)
        self.move_y(dt)
        self.platformCollision(platforms)
        self.groundCollision()
        if self.jumping:
            self.jump()
            self.jumping = not self.jumping
        if abs(self.dx) < PhysicObject.TOLERANCE:
            self.dx = 0
        if abs(self.dy) < PhysicObject.TOLERANCE:
            self.dy = 0      
        self.rect.centerx += self.dx
        self.rect.centery += self.dy      
        self.grounded = False  

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.color = (255,0,0)
        self.physicObject = PhysicObject(x,y,w,h)
        self.state = "IDLE"
        self.rect = self.physicObject.rect
        self.image = self.physicObject.surf
        self.image.fill(self.color)
        self.x_acc = 3

    def getInput(self):
        self.state = "IDLE"
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.state = "LEFT"
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.state = "RIGHT"
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.physicObject.jumping = True

    def update(self,dt,platforms):
        self.getInput()
        if self.state == "IDLE":
            self.physicObject.update(0,dt,platforms)
        elif self.state == "LEFT":
            self.physicObject.update(-self.x_acc,dt,platforms)
        elif self.state == "RIGHT":
            self.physicObject.update(self.x_acc,dt,platforms)
        
        

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.color = (0,0,255)
        self.surf = pygame.Surface((w,h))
        self.rect = self.surf.get_rect(topleft = (x,y))
        self.image = self.surf
        self.image.fill(self.color)
        self.friction = 0.5




        

player = pygame.sprite.GroupSingle(Player(100,100,50,50))
platforms = pygame.sprite.Group(Platform(0,450,500,50),Platform(100,350,400,20),Platform(200,250,200,20))


#gameloop code
while True:
    time = clock.get_time()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()


    screen.fill([0,0,0])   
    player.draw(screen)
    platforms.draw(screen)
    player.update(time/1000,platforms)
    pygame.display.update()
    clock.tick(fps)



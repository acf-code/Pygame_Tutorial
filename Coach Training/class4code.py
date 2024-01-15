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

#Set up player
rect1 = pygame.Rect(0,0,50,50)
rect1.center = [size[0]/2,0]

speed = 3
velocity = Vector2(0,0)
gravity = 10

#adding platforms
platforms = []
for i in range(10):
    platforms.append(pygame.Rect(randint(0,size[0]-150),randint(0,size[1]-30),150,30))

#gameloop code
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    tick = clock.get_time()/1000

    velocity[1] += gravity*tick 
    
    #move in the x direction 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        velocity[0] = speed
    elif keys[pygame.K_LEFT]:
        velocity[0] = -speed
    else:
        velocity[0] = 0
    
    
    screen.fill([0,0,0])
    #collision code for bottom of the screen
    if rect1.bottom + velocity[1] >= size[1]:
        dy = size[1] - rect1.bottom
        velocity[1] = 0
    else:
        dy = velocity[1]

    

    dx = velocity[0]
    

   #collision code with platorms
    pygame.draw.rect(screen,[255,0,0],rect1)
    for p in platforms:
        #if the change in y will hit the platform, change dy to be the distance from the bottom of player and top of platform
        #change v_y to be zero
        if p.colliderect(pygame.Rect(rect1.x,rect1.y + dy,rect1.w,rect1.h)) and dy > 0:
            dy = p.top - rect1.bottom
            if dy < 0:
                dy = 0
            velocity[1] = 0
        #if the change in x will hit the platform and player is moving to the left, change dx to be the distance from the left of player and right of platform
        #change dx to be zero
        elif p.colliderect(pygame.Rect(rect1.x + dx, rect1.y, rect1.w, rect1.h)) and dx < 0:
            dx = p.right - rect1.left
            velocity[0] = 0
        #if the change in x will hit the platform and player is moving to the right, change dx to be the distance from the right of player and left of platform
        #change dx to be zero
        elif p.colliderect(pygame.Rect(rect1.x + dx, rect1.y, rect1.w, rect1.h)) and dx > 0:
            dx = p.left - rect1.right
            velocity[0] = 0
            
    for p in platforms:
        pygame.draw.rect(screen,[0,0,255],p)

    
    #update the player position with dx and dy
    rect1.centerx += dx
    rect1.centery += dy
    pygame.display.update()
    clock.tick(fps)


#Things to Add
#Add jumping to player
#stop player from moving when key is let go
#Have platforms spawn not colliding with eachother


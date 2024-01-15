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
keys = []

#Set up player
playerRect = pygame.Rect(0,0,50,50)
playerRect.center = [size[0]/2,0]
speed = 3
velocity = Vector2(0,0)
gravity = 10
colliding = False
playerColor = [0,255,0]

#adding platforms
platforms = []
for i in range(3):
    platforms.append(pygame.Rect(randint(0,size[0]-150),randint(0,size[1]-30),150,30))

def process_input():
    global keys
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity[1] = -speed
    keys = pygame.key.get_pressed()

def move_player_based_on_input():
    global velocity, keys
    velocity[0] = 0
    velocity[1] += gravity*tick 
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        velocity[0] = speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        velocity[0] = -speed

def handle_player_collision_detection():
    global playerRect, playerColor, velocity
    #collision code for bottom of the screen
    if playerRect.bottom + velocity[1] >= size[1]:
        dy = size[1] - playerRect.bottom
        velocity[1] = 0
    else:
        dy = velocity[1]
    dx = velocity[0]
    playerColor = [0,255,0]
    #collision code with platorms
    oldx = playerRect.centerx
    oldy = playerRect.centery
    #update the player position with dx and dy
    playerRect.centerx += dx
    playerRect.centery += dy
    #process collisions
    for p in platforms:
        if p.colliderect(playerRect):
            playerColor = [255,0,0]
            #push_out_rect(playerRect, p)
            playerRect.centerx = oldx
            playerRect.centery = oldy
            velocity[0] = velocity[1] = 0

def draw_game():
    screen.fill([0,0,0])
    pygame.draw.rect(screen,playerColor,playerRect)
    for p in platforms:
        pygame.draw.rect(screen,[0,0,255],p)
    pygame.display.update()

#main loop
while True:
    tick = clock.get_time()/1000
    process_input()
    move_player_based_on_input()
    handle_player_collision_detection()
    draw_game()
    clock.tick(fps)
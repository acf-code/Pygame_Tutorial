import pygame
from pygame.math import Vector2

pygame.init()

WIDTH, HEIGHT = 800,640

screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()
fps = 60

font = pygame.font.SysFont(None,32)

player_pos = Vector2(WIDTH/2,HEIGHT/2)
player_vel = Vector2(0) # Vector2(0,0)

RED = [255,0,0] #[r,g,b]
GREEN = [0,255,0]
BLACK = [0,0,0]
WHITE = [255,255,255]

speed = 1

isRunning = True
while isRunning:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False

    player_vel = Vector2(0)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_vel[1] = -speed #getting the y velocity
        #player_vel = [x,y] , x -> player_vel[0], y -> player_vel[1]
    if keys[pygame.K_DOWN]:
        player_vel[1] = speed
    if keys[pygame.K_RIGHT]:
        player_vel[0] = speed
    if keys[pygame.K_LEFT]:
        player_vel[0] = -speed

    if (player_vel != Vector2(0)):
        player_vel = player_vel.clamp_magnitude(speed)
    player_pos += player_vel

    screen.fill(BLACK)

    magnitudeofvel = player_vel.magnitude()
    mText = font.render(str(magnitudeofvel),True,WHITE)
    screen.blit(mText,[50,50])
    pygame.draw.circle(screen,RED,player_pos,5)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()




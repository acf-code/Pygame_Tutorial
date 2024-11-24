import pygame
import spritesheet

pygame.init()

WIDTH = 800
HEIGHT = 640

BLACK = (0,0,0)

screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()
fps = 60

dino_sprite = spritesheet.SpriteSheet("animations/doux.png")

dino_idle = []
for i in range(3):
    dino_idle.append(dino_sprite.get_sprite(i,24,24,3,BLACK))
dino_run_right = []
for i in range(3,11):
    dino_run_right.append(dino_sprite.get_sprite(i,24,24,3,BLACK))
dino_run_left = []
for i in dino_run_right:
    flip = pygame.transform.flip(i,True,False)
    flip.set_colorkey(BLACK)
    dino_run_left.append(flip)
    

aniTimer = 0
aniFlip = .1
frame = 0

state = "idle"

dt = 0

isRunning = True
while isRunning:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                state = "left"
                frame = 0
            if event.key == pygame.K_d:
                state = "right"
                frame = 0
        if event.type == pygame.KEYUP:
            state = "idle"
            frame = 0
    if aniTimer > aniFlip:
        frame += 1
        aniTimer = 0
    else:
        aniTimer += dt

    if state == "idle":
        if frame >= 3:
            frame = 0
    if state == "right" or state == "left":
        if frame >= 7:
            frame = 0
    
    screen.fill((128,128,128))
    #screen.blit(dino_idle,[50,50])
    #screen.blit(dino_run[frame],[50,50])
    if state == "idle":
        screen.blit(dino_idle[frame],[50,50])
    elif state == "right":
        screen.blit(dino_run_right[frame],[50,50])
    elif state == "left":
        screen.blit(dino_run_left[frame],[50,50])

    pygame.display.update()
    dt = clock.tick(fps)/1000
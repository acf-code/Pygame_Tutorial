import pygame

pygame.init()

WIDTH = 800
HEIGHT = 640

screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()
fps = 60

dino_idle = pygame.image.load("animations/dino1.png").convert_alpha()
dino_idle.set_colorkey("white")
#dino_idle = dino_idle.convert_alpha()
dino_run_right = [pygame.image.load("animations/dino2.png").convert_alpha(),pygame.image.load("animations/dino3.png").convert_alpha()]
for d in dino_run_right:
    d.set_colorkey("white")

dino_run_left = []
for d in dino_run_right:
    dL = pygame.transform.flip(d,True,False)
    dL.set_colorkey("white")
    dino_run_left.append(dL)

aniTimer = 0
aniFlip = 100
frame = 0

state = "idle"

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
            if event.key == pygame.K_d:
                state = "right"
        if event.type == pygame.KEYUP:
            state = "idle"
    dt = clock.get_time()
    if aniTimer > aniFlip:
        frame += 1
        aniTimer = 0
    else:
        aniTimer += dt

    if frame >= 2:
        frame = 0
    
    screen.fill((128,128,128))
    #screen.blit(dino_idle,[50,50])
    #screen.blit(dino_run[frame],[50,50])
    if state == "idle":
        screen.blit(dino_idle,[50,50])
    elif state == "right":
        screen.blit(dino_run_right[frame],[50,50])
    elif state == "left":
        screen.blit(dino_run_left[frame],[50,50])

    pygame.display.update()
    clock.tick(fps)


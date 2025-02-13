import pygame
from snake import Snake

SWIDTH,SHEIGHT = 500,500

screen = pygame.display.set_mode([SWIDTH,SHEIGHT])
clock = pygame.time.Clock()
fps = 60

snake = Snake()

dt = 0 #deltaTime 

isRunning = True
while isRunning:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    snake.update()
    screen.fill([50,50,50])
    snake.draw(screen)
    pygame.display.update()
    dt = clock.tick(fps) / 1000
#setup
import pygame
import random
pygame.init()

size = [500, 500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

#color = (r,g,b)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
orange = (255, 150, 30)
isRunning = True

rect_1 = pygame.Rect(200,200,100,100)
pygame.display.set_caption("First Game")



#to create an object follow this syntax
#object_name = Class_name(paramters)

#game loop(updates each frame of the game)
while isRunning == True:
    events = pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    if rect_1.x > mouse_pos[0]:
        rect_1.x -= 1
    if rect_1.x < mouse_pos[0]:
        rect_1.x += 1
    if rect_1.y > mouse_pos[1]:
        rect_1.y -= 1
    if rect_1.y < mouse_pos[1]:
        rect_1.y += 1
    screen.fill(color)
    pygame.draw.rect(screen,black,rect_1)
    clock.tick(fps)
    pygame.display.update()

pygame.quit()

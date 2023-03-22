import pygame
from random import randint

pygame.init()
pygame.font.init()

size = [500,500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

font = pygame.font.SysFont(None, 24)

isRunning = True
circle_x = 200
circle_y = 200
color = (randint(0,225),randint(0,225),randint(0,225))
points=0
while isRunning:
  mouse = pygame.mouse.get_pos()
  #print(mouse)
  #mouse[0] = x_pos and mouse[1] = y_pos
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      isRunning = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      if mouse[0]>=circle_x-50 and mouse[0]<=circle_x+50:
        if mouse[1]>=circle_y-50 and mouse[1]<=circle_y+50:
          color = (randint(0,225),randint(0,225),randint(0,225))
          points+=1
          circle_x = randint(0,500)
          circle_y = randint(0,500)
  
  text = font.render(str(points),False,black)
  screen.fill(white)
  screen.blit(text,[25,25])
  pygame.draw.circle(screen,color,[circle_x,circle_y],50)
  clock.tick(fps)
  pygame.display.flip()
  


pygame.quit()
quit()
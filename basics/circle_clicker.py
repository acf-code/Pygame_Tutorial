import pygame
from random import randint

pygame.init()
pygame.font.init()

size = [500,500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

font = pygame.font.SysFont(None, 24)

isRunning = True
circle_x = 250
circle_y = 250
color = (0,0,0)
points = 0
#game loop(updates each frame of the game)
while isRunning:
  mouse = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      isRunning = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      if mouse[0]>=circle_x-50 and mouse[0]<=circle_x+50:
        if mouse[1]>=circle_y-50 and mouse[1]<=circle_y+50:
          color = (randint(0,225),randint(0,225),randint(0,225))
          circle_x = randint(0,500)
          circle_y = randint(0,500)
          points+=1
  
  text = font.render(str(points),False,(0,0,0))
  screen.fill((255,255,255))
  screen.blit(text,[25,25])
  pygame.draw.circle(screen,color,[circle_x,circle_y],50)
  clock.tick(fps)
  pygame.display.flip()
  


pygame.quit()
quit()
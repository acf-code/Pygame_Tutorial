import pygame
pygame.init()
WIDTH, HEIGHT = 800, 640
screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()
fps = 60
while True:
    dt = clock.tick(fps)  # dt is the time between frames in milliseconds
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill([255,255,255])
    pygame.display.update()
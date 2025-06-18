import pygame

screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()
fps = 60

grid = pygame.PixelArray(pygame.Surface([500,500]))


while True:
    dt = clock.tick(fps)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    s = grid.make_surface()
    screen.fill([0,0,0])
    screen.blit(s,[0,0])
    pygame.display.update()
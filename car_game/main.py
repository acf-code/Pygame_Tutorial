import pygame
import classes

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
fps = 30

black = (0, 0, 0)
yellow = (255, 255, 0)
grey = (150, 150, 150)

car = classes.Car([218, 350], 5, "car_game/car.png", 10)
roads = []
for i in range(8):
    if i == 0:
        pos = [240, 0]
    else:
        pos = [240, i * 70]
    roads.append(classes.Road(pos))

isRunning = True
while isRunning:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False
    screen.fill(grey)
    for road in roads:
        road.update(screen)
    car.update(screen)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

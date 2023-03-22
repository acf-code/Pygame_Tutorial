import pygame, sys
from pygame.locals import QUIT
from pygame.math import Vector2
import math

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
fps = 30
clock = pygame.time.Clock()


class Player:

    def __init__(self, color, pos, size):
        self.color = color
        self.pos = Vector2(pos)
        self.velocity = Vector2(0, 0)
        self.size = size
        self.rect = pygame.Rect(self.pos, self.size)
        self.speed = 3

    def render(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.rect = pygame.Rect(self.pos, self.size)

    def move(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.velocity[0] = -self.speed
                if event.key == pygame.K_RIGHT:
                    self.velocity[0] = self.speed
                if event.key == pygame.K_UP:
                    self.velocity[1] = -self.speed
                if event.key == pygame.K_DOWN:
                    self.velocity[1] = self.speed
        if self.pos[0] + self.size[0] > 400:
            self.pos[0] = 400 - self.size[0]
            self.velocity[0] = -self.velocity[0]
        if self.pos[0] < 0:
            self.pos[0] =  self.size[0]
            self.velocity[0] = -self.velocity[0]
        if self.pos[1] + self.size[1] > 400:
            self.pos[1] = 400 + self.size[1]
            self.velocity[1] = -self.velocity[1]
        if self.pos[1] <  0:
            self.pos[1] =  self.size[1]
            self.velocity[1] = -self.velocity[1]
             


        magnitude = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
        if magnitude > 3:
            normal = Vector2(self.velocity[0] / magnitude,
                             self.velocity[1] / magnitude)
            self.velocity = normal * self.speed
        self.pos += self.velocity


#object = Class(parameters)
player = Player((255, 255, 255), [200, 200], [20, 20])
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 255, 0))
    player.render()
    player.move(events)
    print(player.pos)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()

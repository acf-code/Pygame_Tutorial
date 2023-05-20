import pygame
import random
import objects

# Constants
SCREEN_WIDTH = objects.Tools.SCREEN_WIDTH
SCREEN_HEIGHT = objects.Tools.SCREEN_HEIGHT
STAR_MIN_RADIUS = 1
STAR_MAX_RADIUS = 5
STAR_MOVEMENT_SPEED = 150

class Star:
    def __init__(self, pos, min_radius, max_radius):
        self.position = pos
        self.distance = SCREEN_WIDTH + random.randint(1000, 10000)
        self.radius = STAR_MIN_RADIUS
        self.min_radius = min_radius
        self.max_radius = max_radius
        self.x = SCREEN_WIDTH / 2 + self.position[0] * SCREEN_WIDTH / self.distance
        self.y = SCREEN_HEIGHT / 2 + self.position[1] * SCREEN_HEIGHT / self.distance

    def move(self):
        if self.distance > SCREEN_WIDTH:
            self.distance -= STAR_MOVEMENT_SPEED
            self.x = SCREEN_WIDTH / 2 + self.position[0] * SCREEN_WIDTH / self.distance
            self.y = SCREEN_HEIGHT / 2 + self.position[1] * SCREEN_HEIGHT / self.distance
            self.radius = min(self.radius + 0.05, self.max_radius)
        else:
            self.distance = SCREEN_WIDTH + random.randint(1000, 10000)
            self.position[0] = random.randint(-4000, 4000)
            self.position[1] = random.randint(-4000, 4000)
            self.radius = STAR_MIN_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, [255,255,255], [int(self.x), int(self.y)], int(self.radius))

    def update(self, screen):
        self.draw(screen)
        self.move()
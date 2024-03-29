import pygame
from random import randint


class Car:

    def __init__(self, pos, speed, image, health):
        self.pos = pos
        self.pos_center = [self.pos[0] + 32, self.pos[1] + 32]
        self.speed = speed
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [64, 64])
        self.health = health
        self.velocity = [0, 0]
        self.rect = self.image.get_bounding_rect()

    def render(self, screen):
        self.pos = [self.pos_center[0] - 32, self.pos_center[1] - 32]
        screen.blit(self.image, self.pos)
        self.rect.center = self.pos_center

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.velocity[0] = self.speed
        if keys[pygame.K_LEFT]:
            self.velocity[0] = -self.speed
        if keys[pygame.K_SPACE]:
            self.velocity[0] = 0

        if self.pos_center[0] < 0:
            self.velocity[0] = -self.velocity[0]
        if self.pos_center[0] > 500:
            self.velocity[0] = -self.velocity[0]

        self.pos_center[0] += self.velocity[0]
        self.pos_center[1] += self.velocity[1]

    def update(self, screen):
        self.move()
        self.render(screen)


class Road:

    def __init__(self, pos):
        self.pos = pos
        self.width = 10
        self.height = 50
        self.rect = pygame.Rect(self.pos, [self.width, self.height])
        self.color = (255, 255, 0)
        self.speed = 5

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0

    def update(self, screen):
        self.move()
        self.render(screen)


class Obstacle:

    def __init__(self, pos, speed, size, image):
        self.pos = pos
        self.speed = randint(1, speed)
        self.maxspeed = speed
        self.width = size[0]
        self.height = size[1]
        self.pos_center = [self.pos[0] + (self.width / 2), self.pos[1] + (self.height / 2)]
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,[self.width, self.height])
        self.rect = self.image.get_bounding_rect()

    def render(self, screen):
        #screen.blit(self.image, [self.pos_center[0] + self.width / 2, self.pos[1] + self.height / 2])
        self.pos = [self.pos_center[0] - self.width / 2, self.pos_center[1] - self.height / 2]
        screen.blit(self.image,self.pos)
        self.rect.center = self.pos_center
        print(self.pos)

    def move(self):
        self.pos_center[1] += self.speed
        if self.pos_center[1] > 500:
            self.pos_center[1] = 0
            self.speed = randint(1, self.maxspeed)
            self.pos_center[0] = randint(0, 500)

    def update(self, screen):
        self.render(screen)
        self.move()

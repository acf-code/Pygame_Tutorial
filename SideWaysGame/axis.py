import pygame
import numpy as np
from pygame.math import Vector2

# Constants
WIDTH, HEIGHT = 800, 600
CENTER = Vector2(WIDTH // 2, HEIGHT // 2)
AXIS_LENGTH = 200

class Axis:
    def __init__(self):
        self.length = AXIS_LENGTH
        self.basis_vectors = np.array([
            [1, 0, 0],  # x-axis
            [0, 1, 0],  # y-axis
            [0, 0, 1]   # z-axis
        ])
        self.vectors = self.basis_vectors

    def rotation_matrix(self, alpha, beta, gamma):
        alpha, beta, gamma = np.deg2rad([alpha, beta, gamma])  # Convert degrees to radians
        R_x = np.array([
            [1, 0, 0],
            [0, np.cos(alpha), -np.sin(alpha)],
            [0, np.sin(alpha), np.cos(alpha)]
        ])
        R_y = np.array([
            [np.cos(beta), 0, np.sin(beta)],
            [0, 1, 0],
            [-np.sin(beta), 0, np.cos(beta)]
        ])
        R_z = np.array([
            [np.cos(gamma), -np.sin(gamma), 0],
            [np.sin(gamma), np.cos(gamma), 0],
            [0, 0, 1]
        ])
        R = R_z @ R_y @ R_x
        return R

    def rotate(self, alpha, beta, gamma):
        rotated_vectors = self.rotation_matrix(alpha, beta, gamma) @ self.basis_vectors.T
        self.vectors = rotated_vectors.T

    def project(self, vector):
        # Orthographic projection: Ignore z-coordinate
        return CENTER + Vector2(vector[0], vector[1])

    def render(self, screen):
        def draw_triangle(v1, v2, v3, color):
            pygame.draw.polygon(screen, color, [self.project(v1), self.project(v2), self.project(v3)], 1)
        
        # Draw triangles for each face
        # Front face (origin to x, y, and z axis)
        draw_triangle([0, 0, 0], self.vectors[0] * self.length, self.vectors[1] * self.length, pygame.Color("red"))
        draw_triangle([0, 0, 0], self.vectors[0] * self.length, self.vectors[2] * self.length, pygame.Color("green"))
        draw_triangle([0, 0, 0], self.vectors[1] * self.length, self.vectors[2] * self.length, pygame.Color("blue"))

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
fps = 60

a = Axis()
alpha = 0
beta = 0
gamma = 0

while True:
    dt = clock.tick(fps) / 1000  # Time elapsed since last frame in seconds
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                alpha -= 10
            if event.key == pygame.K_d:
                alpha += 10
            if event.key == pygame.K_w:
                beta -= 10
            if event.key == pygame.K_s:
                beta += 10
            if event.key == pygame.K_q:
                gamma -= 10
            if event.key == pygame.K_e:
                gamma += 10

    screen.fill([0, 0, 0])
    #alpha += 10
    a.rotate(alpha, beta, gamma)
    a.render(screen)
    pygame.display.update()

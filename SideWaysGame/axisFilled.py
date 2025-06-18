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
        return R_z @ R_y @ R_x

    def rotate(self, alpha, beta, gamma):
        rotated_vectors = self.rotation_matrix(alpha, beta, gamma) @ self.basis_vectors.T
        self.vectors = rotated_vectors.T

    def project(self, vector):
        # Orthographic projection: Ignore z-coordinate
        return CENTER + Vector2(vector[0], vector[1])

    def calculate_depth(self, triangle):
        # Compute the average z-depth of the triangle vertices
        return np.mean([v[2] for v in triangle])

    def draw_filled_triangle(self, screen, v1, v2, v3, color):
        pygame.draw.polygon(screen, color, [self.project(v1), self.project(v2), self.project(v3)])

    def render(self, screen):
        triangles = []

        # Front face triangles
        triangles.append(([0, 0, 0], self.vectors[0] * self.length, self.vectors[1] * self.length, pygame.Color("red")))
        triangles.append(([0, 0, 0], self.vectors[0] * self.length, self.vectors[2] * self.length, pygame.Color("green")))
        triangles.append(([0, 0, 0], self.vectors[1] * self.length, self.vectors[2] * self.length, pygame.Color("blue")))

        # Back face triangles (offset by -length to simulate depth)
        back_offset = -self.length
        back_vectors = np.copy(self.vectors)
        back_vectors[:, 2] += back_offset
        
        triangles.append(([0, 0, back_offset], back_vectors[0], back_vectors[1], pygame.Color("darkred")))
        triangles.append(([0, 0, back_offset], back_vectors[0], back_vectors[2], pygame.Color("darkgreen")))
        triangles.append(([0, 0, back_offset], back_vectors[1], back_vectors[2], pygame.Color("darkblue")))

        # Side faces connecting front to back
        triangles.append((self.vectors[0] * self.length, self.vectors[1] * self.length, back_vectors[1], pygame.Color("purple")))
        triangles.append((self.vectors[0] * self.length, self.vectors[2] * self.length, back_vectors[2], pygame.Color("cyan")))
        triangles.append((self.vectors[1] * self.length, self.vectors[2] * self.length, back_vectors[2], pygame.Color("magenta")))

        # Sort triangles based on their average depth
        triangles.sort(key=lambda tri: self.calculate_depth(tri[:3]))

        # Draw the sorted triangles
        for v1, v2, v3, color in triangles:
            self.draw_filled_triangle(screen, v1, v2, v3, color)

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update rotation angles
    alpha += 0.5  # Rotate around the x-axis
    beta += 0.5   # Rotate around the y-axis
    gamma += 0.5  # Rotate around the z-axis

    # Reset angles to keep them within 0-360 degrees
    alpha %= 360
    beta %= 360
    gamma %= 360

    # Rotate the axis and render
    a.rotate(alpha, beta, gamma)
    screen.fill([0, 0, 0])
    a.render(screen)
    pygame.display.update()

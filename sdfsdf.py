import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Square")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Square properties
center_x, center_y = WIDTH // 2, HEIGHT // 2
large_square_size = 200
small_square_size = 50
angle = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Rotate the small square around the center of the large square
    angle += -10  # You can adjust the rotation speed by changing this value
    radian_angle = math.radians(angle)
    small_square_x = center_x + int(math.cos(radian_angle) * (large_square_size / 2 - small_square_size / 2))
    small_square_y = center_y - int(math.sin(radian_angle) * (large_square_size / 2 - small_square_size / 2))

    # Draw the large square
    pygame.draw.rect(screen, RED, (center_x - large_square_size // 2, center_y - large_square_size // 2,
                                   large_square_size, large_square_size),width=2)

    # Draw the rotating small square
    pygame.draw.rect(screen, RED, (small_square_x - small_square_size // 2, small_square_y - small_square_size // 2,
                                   small_square_size, small_square_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()

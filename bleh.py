import pygame
import math
from pygame.math import Vector2
from random import randint

pygame.init()

# Setup
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TikZ-style Hexagonal Fractal")
clock = pygame.time.Clock()
FPS = 60

# Colors
BG_COLOR = (10, 10, 25)
COLORS = [
    (255, 50, 50),
    (50, 255, 50),
    (50, 50, 255),
    (255, 255, 50),
    (255, 50, 255),
    (50, 255, 255)
]

def draw_hexagon(pos, size, depth, max_depth):
    if depth > max_depth:
        return
    
    # Calculate hexagon vertices
    points = []
    for i in range(6):
        angle_deg = 60 * i - 30
        angle_rad = math.radians(angle_deg)
        x = pos.x + size * math.cos(angle_rad)
        y = pos.y + size * math.sin(angle_rad)
        points.append(Vector2(x, y))
    
    # Draw the hexagon
    color = COLORS[depth % len(COLORS)]
    pygame.draw.polygon(screen, color, points, 1)
    
    # Recursively draw smaller hexagons
    if depth < max_depth:
        new_size = size * 0.4  # Scaling factor
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = math.radians(angle_deg)
            dx = size * 0.6 * math.cos(angle_rad)
            dy = size * 0.6 * math.sin(angle_rad)
            new_pos = Vector2(pos.x + dx, pos.y + dy)
            draw_hexagon(new_pos, new_size, depth + 1, max_depth)

def main():
    running = True
    max_depth = 5  # Controls recursion depth
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    max_depth = min(8, max_depth + 1)
                elif event.key == pygame.K_DOWN:
                    max_depth = max(1, max_depth - 1)
        
        screen.fill(BG_COLOR)
        
        # Draw the fractal
        center = Vector2(WIDTH // 2, HEIGHT // 2)
        initial_size = 300
        draw_hexagon(center, initial_size, 0, max_depth)
        
        # Display instructions
        font = pygame.font.SysFont('Arial', 20)
        text = font.render(f"Recursion Depth: {max_depth} (UP/DOWN to change)", True, (255, 255, 255))
        screen.blit(text, (20, 20))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
import pygame
import sys
import random
import math
from pygame import gfxdraw

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Convex 8-Sided Polygon")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

def generate_convex_polygon(num_vertices, center, max_radius):
    """Generate a convex polygon with the given number of vertices"""
    # Generate random angles and sort them
    angles = sorted([random.uniform(0, 2 * math.pi) for _ in range(num_vertices)])
    
    # Generate random radii (ensuring they don't create concavities)
    min_radius = max_radius * 0.4
    radii = [random.uniform(min_radius, max_radius) for _ in range(num_vertices)]
    
    # Smooth the radii to ensure convexity
    for i in range(num_vertices):
        prev_radius = radii[i-1]
        next_radius = radii[(i+1)%num_vertices]
        # Ensure the current radius isn't too small compared to neighbors
        radii[i] = max(radii[i], min(prev_radius, next_radius) * 0.9)
    
    # Convert polar to Cartesian coordinates
    points = []
    for angle, radius in zip(angles, radii):
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))
    
    return points

def is_convex(polygon):
    """Check if a polygon is convex"""
    if len(polygon) < 3:
        return False
    
    sign = 0
    n = len(polygon)
    
    for i in range(n):
        dx1 = polygon[(i+1)%n][0] - polygon[i][0]
        dy1 = polygon[(i+1)%n][1] - polygon[i][1]
        dx2 = polygon[(i+2)%n][0] - polygon[(i+1)%n][0]
        dy2 = polygon[(i+2)%n][1] - polygon[(i+1)%n][1]
        
        cross = dx1 * dy2 - dy1 * dx2
        
        if cross != 0:
            if sign == 0:
                sign = 1 if cross > 0 else -1
            else:
                if (sign == 1 and cross < 0) or (sign == -1 and cross > 0):
                    return False
    return True

def main():
    clock = pygame.time.Clock()
    center = (WIDTH // 2, HEIGHT // 2)
    max_radius = min(WIDTH, HEIGHT) * 0.4
    
    # Generate initial convex polygon
    while True:
        polygon = generate_convex_polygon(8, center, max_radius)
        if is_convex(polygon):
            break
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Generate a new convex polygon when space is pressed
                    while True:
                        polygon = generate_convex_polygon(8, center, max_radius)
                        if is_convex(polygon):
                            break
        
        # Clear screen
        screen.fill(WHITE)
        
        # Draw polygon
        if len(polygon) > 2:
            pygame.draw.polygon(screen, BLUE, polygon, 0)  # Filled
            pygame.draw.polygon(screen, BLACK, polygon, 2)  # Outline
        
        # Draw vertices
        for point in polygon:
            pygame.draw.circle(screen, RED, (int(point[0]), int(point[1])), 5)
        
        # Draw center
        pygame.draw.circle(screen, GREEN, center, 5)
        
        # Display instructions
        font = pygame.font.SysFont(None, 36)
        text = font.render("Press SPACE to generate a new convex polygon", True, BLACK)
        screen.blit(text, (20, 20))
        
        # Display convexity check
        status = "Convex" if is_convex(polygon) else "Not Convex"
        status_text = font.render(f"Status: {status}", True, BLACK)
        screen.blit(status_text, (20, 60))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
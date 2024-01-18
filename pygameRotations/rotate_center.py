import pygame
from pygame.math import Vector2
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
BLACK, BLUE, GREEN = (0, 0, 0), (0, 0, 255), (0, 255, 0)

class Player:
    # Constants for initial player properties
    INITIAL_ANGLE = 270
    ANGULAR_SPEED = 3
    SPEED = 5
    RECT_SIZE = 50

    def __init__(self, x, y):
        # Initialize player attributes
        self.x = x
        self.y = y
        self.angle = self.INITIAL_ANGLE
        self.angularspeed = self.ANGULAR_SPEED
        self.speed = self.SPEED
        self.rect = pygame.Rect(x, y, self.RECT_SIZE, self.RECT_SIZE)
        # Load and scale the player's image
        self.image = pygame.transform.scale(pygame.image.load("pygameRotations/spaceship.png"), (self.RECT_SIZE, self.RECT_SIZE))
        self.direction = Vector2.from_polar([self.RECT_SIZE / 2, self.angle])

    def move(self, keys):
        # Store the current angle for later comparison
        old_angle = self.angle
        vel = Vector2(0)
        # Handle rotation based on user input
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.angle += self.angularspeed
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.angle -= self.angularspeed
        # Update direction vector based on the new angle
        self.direction = Vector2.from_polar([self.RECT_SIZE / 2, self.angle])
        d = self.direction.normalize()
        # Handle forward and backward movement based on user input
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            vel[1] = d[1]
            vel[0] = d[0]
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            vel[1] = -d[1]
            vel[0] = -d[0]
        # Normalize and scale velocity based on speed
        if vel != Vector2(0):
            vel = vel.normalize()
            vel[0] *= self.speed
            vel[1] *= self.speed
        # Print information if the angle has changed
        if old_angle != self.angle:
            print(d)
            print(self.angle)
            old_angle = self.angle
        # Update player position based on velocity
        self.x += vel[0]
        self.y += vel[1]

    def render(self, screen):
        # Render the player on the screen
        self.rect.center = [self.x, self.y]
        up = Vector2(0, -1)
        angleFromUp = up.angle_to(self.direction)
        # Rotate the player's image based on its direction
        image_rot = pygame.transform.rotate(self.image, -angleFromUp)
        image_rect = image_rot.get_rect(center=[self.x, self.y])
        # Draw the player's image and rectangle on the screen
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, image_rect)
        pygame.draw.rect(screen, GREEN, self.rect)
        screen.blit(image_rot, image_rect)
        # Draw a line indicating the player's direction
        pygame.draw.line(screen, GREEN, [self.x, self.y], [self.x + self.direction[0], self.y + self.direction[1]])

    def update(self, screen, keys, dt):
        # Update the player's position and render on the screen
        self.move(keys)
        self.render(screen)

# Initialize player with starting position
player = Player(WIDTH / 2, HEIGHT / 2)


# Initialize game clock and frames per second
clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode([WIDTH,HEIGHT])

# Main game loop
while True:
    # Get mouse position and handle events
    mPos = pygame.mouse.get_pos()
    events = pygame.event.get()
    dt = clock.get_time()
    for event in events:
        if event.type == pygame.QUIT:
            # Quit the game if the window is closed
            pygame.quit()
            sys.exit()
    # Get keyboard input
    keys = pygame.key.get_pressed()
    # Update and render the player
    player.update(screen, keys, dt)
    # Update the display
    pygame.display.update()
    # Control the frames per second
    clock.tick(fps)

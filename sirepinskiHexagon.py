import pygame
from pygame.math import Vector2,Vector3
from random import randint,choice


pygame.init()

WIDTH,HEIGHT = 800,800
screen = pygame.display.set_mode([WIDTH,HEIGHT])
clock = pygame.time.Clock()
fps = 60

dt = 0

hexagonPoints = []
center = Vector2(WIDTH/2,HEIGHT/2)
length = 350
direction = Vector2(-1,0)
for i in range(6):
    direction.rotate_ip(60)
    point = center + direction * length
    hexagonPoints.append(point)
    



def drawHexagon(screen,points,color):
    for p in points:
        pygame.draw.circle(screen,color,p,3)

def generateSirpinskiPoints(numOfPoints, hexagonPoints):
    startPoint = center
    points = []
    for i in range(numOfPoints):
        target = choice(hexagonPoints)
        # Skip if startPoint equals target to avoid zero vector
        if startPoint == target:
            continue
        direction = (target - startPoint).normalize()
        randomPoint = startPoint + (target - startPoint) * 0.5  # Midpoint
        points.append(randomPoint)
        startPoint = randomPoint
        # Ensure we generate exactly numOfPoints by counting the skipped points
        if len(points) >= numOfPoints:
            break
    return points
sirpinskiPoints = generateSirpinskiPoints(10000,hexagonPoints)

def drawSirpinskiPoints(screen,points,startColor,endColor):
    for p in points:
        if p != center:
            distFromCenter = Vector2(p - center).length()
        else:
            distFromCenter = 0
        color = Vector3(startColor).lerp(endColor,min(distFromCenter/length,1))
        pygame.draw.circle(screen,color,p,1)

        
speed = 5

isRunning = True
while isRunning:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(1)
    
    screen.fill("black")
    # drawHexagon(screen,hexagonPoints,"white")
    drawSirpinskiPoints(screen,sirpinskiPoints,[255,0,0],[0,0,255])
    for point in sirpinskiPoints:
        point.x += speed
        if point.x > 800:
            point.x = 0
            #speed = -speed
        if point.x < 0:
            point.x = 800
            #speed = -speed
    pygame.display.update()
    dt = clock.tick(fps)/1000
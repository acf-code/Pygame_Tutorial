import pygame
from pygame.math import Vector2
from pygame.gfxdraw import textured_polygon
from random import randint



def createHexagon(size,texture):
    image = pygame.Surface(size)
    textureImage = pygame.image.load(texture)
    center = Vector2(size[0]/2,size[1]/2)
    hexagonPoints = []
    length = size[0]/2 * .8
    direction = Vector2(-1,0)
    for i in range(12):
        direction.rotate_ip(randint(20,30))
        point = center + direction * randint(int(length - length*.25),int(length))
        hexagonPoints.append(point)
    t_x = randint(0,textureImage.get_rect().w - size[0])
    t_y = randint(0,textureImage.get_rect().h - size[1])
    textured_polygon(image,hexagonPoints,textureImage,t_x,t_y)
    return image,hexagonPoints

def createAsteroidSurface(size,texture):
    image = pygame.Surface(size)
    textureImage = pygame.image.load(texture)
    center = Vector2(size[0]/2,size[1]/2)
    hexagonPoints = []
    length = size[0]/2 * .8
    direction = Vector2(-1,0)
    for i in range(12):
        direction.rotate_ip(randint(20,30))
        point = center + direction * randint(int(length - length*.25),int(length))
        hexagonPoints.append(point)
    t_x = randint(0,textureImage.get_rect().w - size[0])
    t_y = randint(0,textureImage.get_rect().h - size[1])
    textured_polygon(image,hexagonPoints,textureImage,t_x,t_y)
    return image







if __name__ == "__main__":
    pygame.init()

    WIDTH,HEIGHT = 800,600
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    clock = pygame.time.Clock()
    fps = 60

    testAsteroid,p = createHexagon([256,256],"space_game_z/asteroidTexture.jpg")

    isRunning = True
    while isRunning:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill("black")
        screen.blit(testAsteroid,testAsteroid.get_rect(center = [WIDTH/2,HEIGHT/2]))
        clock.tick(fps)
        pygame.display.update()
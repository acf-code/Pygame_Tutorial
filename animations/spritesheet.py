import pygame

class SpriteSheet():
    def __init__(self,image):
        self.sheet = pygame.image.load(image)

    def get_sprite(self,frame ,width, height, scale, color):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet,(0,0),((frame*width),0,width,height))
        image = pygame.transform.smoothscale(image,(width*scale,height*scale))
        image.set_colorkey(color)

        return image
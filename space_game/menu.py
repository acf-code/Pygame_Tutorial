import pygame
from pygame.math import Vector2
from random import randint
import objects, tools

def gameloop():
    pygame.init()
    pygame.font.init()

    size = [500, 500]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = tools.fps

    start_text = tools.font.render('Start', True, tools.white)
    start_rect = start_text.get_rect()
    start_rect.center = [size[0]/2,size[1]/2]

    exit_text = tools.font.render('Exit', True, tools.white)
    exit_rect = exit_text.get_rect()
    exit_rect.center = [size[0]/2,size[1]/2 + 100]


    isRunning = True

    background=pygame.image.load("space_game/images/background.png")

    pygame.display.set_caption("Space Game")

    while isRunning == True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    return "level1"
                if exit_rect.collidepoint(event.pos):
                    isRunning = False
        screen.fill(tools.white)
        pygame.draw.rect(screen,tools.black,start_rect)
        pygame.draw.rect(screen,tools.black,exit_rect)
        screen.blit(start_text,start_rect)
        screen.blit(exit_text,exit_rect)
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    gameloop()
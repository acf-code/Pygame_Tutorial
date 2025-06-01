import pygame
from player import Player
from enemyManager import EnemyManager
from obstacle import Obstacle
from scene import MainScene, StartScene

pygame.init()

class Game:
    SWIDTH,SHEIGHT = 500,500
    def __init__(self):
        self.screen = pygame.display.set_mode([Game.SWIDTH,Game.SHEIGHT])
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.mainScene = MainScene(self.screen,self.clock,self.fps)
        self.startScene = StartScene(self.screen,self.clock,self.fps)
        self.state = "start"

    def update(self):
        if self.state == "main":
            self.mainScene.update(self)
        elif self.state == "start":
            self.startScene.update(self)

    def draw(self):
        if self.state == "main":
            self.mainScene.draw()
        elif self.state == "start":
            self.startScene.draw()

    def main(self):
        while True:
            self.update()
            self.draw()
            pygame.display.update()


game = Game()
game.main()

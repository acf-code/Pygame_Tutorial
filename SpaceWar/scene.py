import pygame
from player import Player
from enemyManager import EnemyManager
from obstacle import Obstacle

class MainScene:
    def __init__(self,screen,clock,fps):
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.dt = 0
        self.onEnter()
        

    def onEnter(self):
        SWIDTH = self.screen.get_width()
        SHEIGHT = self.screen.get_height()
        self.ship = Player([SWIDTH/2,SHEIGHT - 30])
        self.enemies = EnemyManager(SWIDTH,SHEIGHT)
        self.obstacles = [Obstacle([SWIDTH/5,SHEIGHT-75]),Obstacle([SWIDTH/2,SHEIGHT-75]),Obstacle([SWIDTH*4/5,SHEIGHT-75])]

    def getObjects(self):
        objects = []
        objects.append(self.ship)
        objects.extend(self.enemies.getCurrentEnemies()["enemyObjects"])
        objects.extend(self.obstacles)
        return objects
    
    def update(self,game):
        self.dt = self.clock.tick(self.fps)/1000
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
        objects = self.getObjects()
        self.ship.update(objects)
        self.enemies.update(self.dt,objects)
        for obstactle in self.obstacles:
            obstactle.update()

    def draw(self):
        self.screen.fill("black")
        self.enemies.draw(self.screen)
        self.ship.draw(self.screen)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)


class StartScene:
    def __init__(self,screen,clock,fps):
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.titleFont = pygame.font.SysFont(None,64)
        self.buttonFont = pygame.font.SysFont(None,48)
        self.titleText = self.titleFont.render("SPACE INVADERS",True,"white")
        self.buttonText = self.buttonFont.render("START", True, "white")
        self.buttonSurface = pygame.Surface([128,32])
        self.buttonSurface.fill("green")
        self.buttonPos = [self.screen.get_width()/2, self.screen.get_height()*2/3]
        self.buttonRect = self.buttonSurface.get_rect(center = self.buttonPos)
        self.titlePos = [self.screen.get_width()/2,self.screen.get_height()/3]

    def update(self,game):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if self.buttonRect.collidepoint(event.pos):
                    game.mainScene.onEnter()
                    game.state = "main"

    def draw(self):
        self.screen.fill("black")
        self.screen.blit(self.titleText,self.titleText.get_rect(center = self.titlePos))
        self.screen.blit(self.buttonSurface,self.buttonRect)
        self.screen.blit(self.buttonText,self.buttonText.get_rect(center = self.buttonPos))


class GameOverScene:
    def __init__(self,screen,clock,fps):
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.titleFont = pygame.font.SysFont(None,64)
        self.buttonFont = pygame.font.SysFont(None,48)
        self.titleText = self.titleFont.render("GAME OVER!", True, "white")
        self.restartText = self.buttonFont.render("RESTART", True, "white")
        self.quitText = self.buttonFont.render("QUIT", True, "white")
        self.restartSurface = pygame.Surface([128,32])
        self.restartSurface.fill("green")
        self.quitSurface = pygame.Surface([128,32])
        self.quitSurface.fill("red")
        self.restartPos = [self.screen.get_width()/2,self.screen.get_height()*3/5]
        

        
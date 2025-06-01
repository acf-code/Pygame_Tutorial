import pygame
from pygame.math import Vector2
from enemy import Enemy

class EnemyManager:
    def __init__(self,swidth,sheight):
        self.screenWidth = swidth
        self.screenHeight = sheight
        self.gridSize = 50
        self.enemySize = 32
        self.rows = int(sheight/self.gridSize)
        self.cols = int(swidth/self.gridSize)
        self.grids = self.generateGrids()
        self.generateEnemies(2,0,self.cols-2,self.rows-4,self.grids)
        self.state = "moveRight"
        self.moveTimer = 0
        self.moveCooldown = 15
        self.bullets = []

    def generateGrids(self):
        grids = []
        for x in range(self.cols):
            for y in range(self.rows):
                rect = pygame.Rect(x*self.gridSize,y*self.gridSize,self.gridSize,self.gridSize)
                g = {
                    "rect" : rect,
                    "enemy" : None,
                    "x" : x,
                    "y" : y
                }
                grids.append(g)

        return grids
    
    def generateEnemies(self,startNumCols,startNumRows,endNumCols,endNumRows,grids):
        for x in range(startNumCols,endNumCols):
            for y in range(startNumRows,endNumRows):
                grid = None
                for g in grids:
                    if g["x"] == x and g["y"] == y:
                        grid = g
                        enemy = Enemy(grid["rect"].center, 32)
                        grid["enemy"] = enemy

        

    def draw(self,screen):
        #self.drawGrids(screen)
        self.drawEnemies(screen)
        for bullet in self.bullets:
            bullet.draw(screen)

    def drawGrids(self,screen):
        for grid in self.grids:
            pygame.draw.rect(screen,"yellow",grid["rect"],1)

    def drawEnemies(self,screen):
        for grid in self.grids:
            if grid["enemy"] != None:
                grid["enemy"].draw(screen)

    def update(self,dt,objects):
        if self.state == "moveRight":
            self.moveRightUpdate(dt)
        elif self.state == "moveDown":
            self.moveDownUpdate(dt)
        elif self.state == "moveLeft":
            self.moveLeftUpdate(dt)
        enemyObjects = self.getCurrentEnemies()["enemyObjects"]
        for enemy in enemyObjects:
            enemy.update(dt,objects,self.bullets)
        for bullet in self.bullets:
            bullet.update(objects)
            if bullet.destroyed:
                self.bullets.remove(bullet)

    def getCurrentEnemies(self):
        enemies = []
        for grid in self.grids:
            if grid["enemy"] != None:
                enemies.append(grid)
        enemyObjects = []
        for enemy in enemies:
            enemyObjects.append(enemy["enemy"])
        startX = enemies[0]["x"]
        startY = enemies[0]["y"]
        endX = enemies[-1]["x"]
        endY = enemies[-1]["y"]
        for enemy in enemies:
            if enemy["x"] < startX:
                startX = enemy["x"]
            if enemy["y"] < startY:
                startY = enemy["y"]
            if enemy["x"] > endX:
                endX = enemy["x"]
            if enemy["y"] > endY:
                endY = enemy["y"]
        enemiesDict = {
            "enemies" : enemies,
            "startX" : startX,
            "startY" : startY,
            "endX" : endX,
            "endY" : endY,
            "enemyObjects" : enemyObjects
        }
        return enemiesDict


    def moveRightUpdate(self,dt):
        if self.moveTimer >= self.moveCooldown:
            enemiesDict = self.getCurrentEnemies()
            if enemiesDict["endX"] >= self.cols - 1:
                self.state = "moveDown"
                self.moveTimer = 0
            else:
                newGrids = self.generateGrids()
                for enemy in enemiesDict["enemies"]:
                    for grid in newGrids:
                        if enemy["x"] + 1 == grid["x"] and enemy["y"] == grid["y"]:
                            grid["enemy"] = Enemy(grid["rect"].center, 32,destroyed=enemy["enemy"].destroyed,health=enemy["enemy"].health)
                self.grids = newGrids
                self.moveTimer = 0
        else:
            self.moveTimer += dt

    def moveDownUpdate(self,dt):
        if self.moveTimer >= self.moveCooldown:
            enemiesDict = self.getCurrentEnemies()
            if enemiesDict["endY"] >= self.rows - 3:
                self.state = "end"
                self.moveTimer = 0
            else:
                newGrids = self.generateGrids()
                for enemy in enemiesDict["enemies"]:
                    for grid in newGrids:
                        if enemy["x"] == grid["x"] and enemy["y"] + 1 == grid["y"]:
                            grid["enemy"] = Enemy(grid["rect"].center, 32,destroyed=enemy["enemy"].destroyed,health=enemy["enemy"].health)
                self.grids = newGrids
                self.moveTimer = 0
                if enemiesDict["endX"] >= self.cols - 1:
                    self.state = "moveLeft"
                else:
                    self.state = "moveRight"
        else:
            self.moveTimer += dt

    def moveLeftUpdate(self,dt):
        if self.moveTimer >= self.moveCooldown:
            enemiesDict = self.getCurrentEnemies()
            if enemiesDict["startX"] <= 0:
                self.state = "moveDown"
                self.moveTimer = 0
            else:
                newGrids = self.generateGrids()
                for enemy in enemiesDict["enemies"]:
                    for grid in newGrids:
                        if enemy["x"] - 1 == grid["x"] and enemy["y"] == grid["y"]:
                            grid["enemy"] = Enemy(grid["rect"].center, 32,destroyed=enemy["enemy"].destroyed,health=enemy["enemy"].health)
                self.grids = newGrids
                self.moveTimer = 0
        else:
            self.moveTimer += dt
            
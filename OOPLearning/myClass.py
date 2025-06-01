import pygame
from pygame.math import Vector2
from math import dist
from projectile import Projectile
from random import randint

#Datatypes
#1. String - it is a value surronded by quotations, text to be read by humans
#   ex. "Chloe", "56", "false"
#2. Integer - it is a whole number, no floating point values (decimals)
#   ex. 56, 767, -444
#3. Float - it is a number with a floating point value, it has decimals
#   ex. 7.25, -.34, 500.00
#4. Boolean - True or False
#   ex. True, False

#OOP stands for object oriented programming
#it is a way organize code into separate objects to make organization and code logic easier to handle

#in the past we used dictionaries(holds information with key value pairs),we had a file called player in that
#file we had function called makePlayer() which returned a dictionar with all the values that are relevant to the
#player

#we had other functions go use this dictionary to change specific values in the dictionary, like updating
#the position, the health, and being able to add bullets to the bullet list in the player dictionary

#Object Oriented Programming, is split up into two parts. The class and the object. The class defines
#what a object is and actions the object can perform. Objects are instances of a specific class

#What is the class for these objects:
#1. 56 ~ integer
#2. "hi" ~ string
#3. false ~ boolean

# to make a class do the following:
#class NameOfClass:

class Player:
    #next we are going to make a constructor method
    #the constructor method sets the instance variables of the class
    #an instance variable describes what a object is
    #for example: 
    #if I had a class called Dog
    #some istance variables would be like : size, furColor, breed
    #to make a constructor method for player type the following

    #What is a Vector2?
    #a Vector2 is a special list that can only hold two values
    #the first value is a value in the x direction (left to right)
    #the second value is a value in the y direction (up to down)

    def __init__(self):
        #to make an instance variable follow this format
        #self.nameOfVariable = value
        #self.image = pygame.Surface([50,50])
        self.upImage = pygame.image.load("OOPLearning/player/playerup.png")
        self.rightImage = pygame.image.load("OOPLearning/player/playerright.png")
        self.leftImage = pygame.image.load("OOPLearning/player/playerleft.png")
        self.downImage = pygame.image.load("OOPLearning/player/playerdown.png")
        self.image = self.upImage
        #the self is used to tell python that the specific variable/functions is part of the class/object
        self.pos = Vector2(250,250)
        self.color = "red"
        self.rect = self.image.get_rect(center = self.pos)
        self.boundRect = self.image.get_bounding_rect()
        self.hitBox = self.boundRect
        self.speed = 5
        self.vel = Vector2(0,0) #self.vel[0] is how fast we are moving in the x direction, and self.vel[1] is how fast we are moving in the y direction
        self.sword = Sword()
        self.attack = False
        self.facing = "up"
        self.maxHealth = 20
        self.health = self.maxHealth
        self.mPos = None
        self.destroyed = False
        self.isHurt = False
        self.isHurtCooldown = 7
        self.isHurtTimer = self.isHurtCooldown
        self.isHurtSpeed = 3



    #methods describe what an object does
    #fore example in the class Dog, a dog might bark, run, or play

    def draw(self,screen):
        if self.facing == "up":
            self.image = self.upImage
        elif self.facing == "right":
            self.image = self.rightImage
        elif self.facing == "left":
            self.image = self.leftImage
        elif self.facing == "down":
            self.image = self.downImage
        self.boundRect.center = self.rect.center
        self.hitBox.center = self.rect.center
        # pygame.draw.rect(screen,"red",self.boundRect)
        screen.blit(self.image,self.rect)
        if self.attack:
            self.sword.draw(screen)

    def move(self):
        self.vel = Vector2(0,0)#reseting the velocity
        keys = pygame.key.get_pressed()#this gets a list of all the keys on your keyboard that are being pressed down
        if keys[pygame.K_LEFT]:#if the left arrow key gets pressed
            self.facing = "left"
            self.vel[0] = -self.speed#setting the x velocity to be negative speed
        if keys[pygame.K_RIGHT]:
            self.facing = "right"
            self.vel[0] = self.speed
        if keys[pygame.K_DOWN]:
            self.facing = "down"
            self.vel[1] = self.speed
        if keys[pygame.K_UP]:
            self.facing = "up"
            self.vel[1] = -self.speed
        if self.vel != Vector2(0,0):
            self.vel.clamp_magnitude_ip(self.speed)#making sure it stays the same speed for all directions
        self.pos += self.vel#adding the velocity to the pos
        self.rect.center = self.pos#setting the center of the rect to be the pos



    def mainUpdate(self,enemies):#this method will be called every frame of our game
        self.move()
        #check if the mouse button is being pressed down, if so attack 
        self.getInputs()#this function will see if any inputs have been give to do an action
        #print(self.attack)
        if self.attack:
            self.sword.updatePos(self,self.mPos)
            for enemy in enemies:
                if self.sword.collide(enemy):
                    enemy.gotHit(self.sword.damage)
                    self.attack = False
        pygame.display.set_caption("Health: " + str(self.health))
        if self.health < 0:
            self.destroyed = True

    def update(self,enemies,screen):
        if not self.isHurt:
            self.mainUpdate(enemies)
        elif self.isHurt:
            self.hurtUpdate()
        self.boundary(screen)

    def hurtUpdate(self):
        if self.isHurt:
            self.pos += self.vel
            self.rect.center = self.pos
            if self.isHurtTimer >= 0:
                self.isHurtTimer -= 1
            else:
                self.isHurt = False
                self.isHurtTimer = self.isHurtCooldown
        else:
            self.vel = Vector2(0)

    def boundary(self,screen):
        #get the screen width and height
        width = screen.get_width()
        height = screen.get_height()
        if self.pos.x < 0:
            self.pos.x = width
            self.rect.center = self.pos
        elif self.pos.x > width:
            self.pos.x = 0
            self.rect.center = self.pos
        if self.pos.y < 0:
            self.pos.y = height
            self.rect.center = self.pos
        elif self.pos.y > height:
            self.pos.y = 0
            self.rect.center = self.pos
        


    def getInputs(self):
        self.attack = pygame.mouse.get_pressed()[0]
        if self.attack:
            self.mPos = pygame.mouse.get_pos()

    def gotHit(self,object):
        if not self.isHurt:
            self.health -= object.damage
            self.isHurt = True
            self.vel = object.direction * self.isHurtSpeed

class Sword:
    def __init__(self):
        #self.image = pygame.image.load("OOPLearning/sword.png")
        self.upImage = pygame.image.load("OOPLearning/sword.png")
        self.downImage = pygame.transform.flip(self.upImage,False,True)
        self.rightImage = pygame.transform.rotate(self.upImage,-90)
        self.leftImage = pygame.transform.rotate(self.upImage,90)
        self.image = self.upImage
        self.facing = "up"
        #Can you make other instance variables 
        self.pos = Vector2(0,0)
        self.rect = self.image.get_rect()
        self.damage = 2
        self.offset = 5 #this is the offset between the player and the sword

    def draw(self,screen):#draw the sword on the screen
        if self.facing == "up":
            self.image = self.upImage
        elif self.facing == "down":
            self.image = self.downImage
        elif self.facing == "left":
            self.image = self.leftImage
        elif self.facing == "right":
            self.image = self.rightImage
        pygame.draw.rect(screen,"blue",self.rect)
        screen.blit(self.image,self.rect)

    #next we need to make a method that updates the position of the sword based on the player
    def updatePos(self,player,facing):
        self.facing = self.getFacing(facing,player)
        self.rect = self.image.get_rect()
        if self.facing == "up":
            # self.rect = self.image.get_rect()
            #will have the sword appear at the tope of the player
            topPos = Vector2(player.boundRect.midtop)
            #will set the bottom of the sword to be at the top of the player plus some offset
            self.rect.midbottom = topPos
            self.rect.bottom -= self.offset
            self.pos = self.rect.center
        elif self.facing == "down":
            # self.rect = self.image.get_rect()
            downPos = Vector2(player.boundRect.midbottom)
            self.rect.midtop = downPos
            self.rect.top += self.offset
            self.pos = self.rect.center
        elif self.facing == "right":
            # self.rect = self.image.get_rect()
            rightPos = Vector2(player.boundRect.midright)
            self.rect.midleft = rightPos
            self.rect.left += self.offset
            self.pos = self.rect.center
        elif self.facing == "left":
            # self.rect = self.image.get_rect()
            leftPos = Vector2(player.boundRect.midleft)
            self.rect.midright = leftPos
            self.rect.right -= self.offset
            self.pos = self.rect.center

    def collide(self,object):
        if self.rect.colliderect(object.rect):
            return True
        else:
            return False
        
    def getFacing(self,facing,player):
        xChange = facing[0] - player.pos[0]
        yChange = facing[1] - player.pos[1]
        if abs(xChange) > abs(yChange):
            if xChange < 0:
                return "left"
            else:
                return "right"
        elif abs(xChange) < abs(yChange):
            if yChange < 0:
                return "up"
            else:
                return "down"
        else:
            return player.facing



class Enemy:
    def __init__(self,startPos):
        self.size = 50
        self.image = pygame.image.load("OOPLearning/enemy.png")
        self.image = pygame.transform.scale(self.image,[self.size,self.size])
        self.pos = Vector2(startPos)
        self.rect = self.image.get_rect(center = startPos)
        self.color = "green"
        self.state = "idle"
        self.followDistance = 200
        self.attackDistance = 100
        self.speed = 2
        self.direction = Vector2(0)
        self.health = 5
        self.damage = 2
        self.destroyed = False
        self.attackStartSize = Vector2(16,16)
        self.attackEndSize = Vector2(96,96)
        self.attackTimer = 0
        self.attackCooldown = 30
        self.attackDirection = Vector2(0)
        self.attackStartPos = Vector2(0)
        self.projectiles = []
        self.shootTimer = 0
        self.shootCooldown = 45
        self.healthPacks = None
        
    def draw(self,screen):
        for projectile in self.projectiles:
            projectile.draw((screen))
        if self.state == "idle":
            self.color = "green"
        elif self.state == "follow":
            self.color = "red"
        elif self.state == "attack":
            self.color = "yellow"
            self.attackDraw(screen)
        screen.blit(self.image,self.rect)

    def attackDraw(self,screen):
        t = min(1,(self.attackTimer/self.attackCooldown))
        attackSize = self.attackStartSize.lerp(self.attackEndSize,t)
        attackSurface = pygame.Surface(attackSize)
        attackSurface.fill("yellow")
        screen.blit(attackSurface,attackSurface.get_rect(center = self.attackStartPos))

    def update(self,player,enemies,healthPacks):
        if self.state == "idle":
            self.idleUpdate(player)
        elif self.state == "follow":
            self.followUpdate(player)
        elif self.state == "attack":
            self.attackUpdate(player)
        self.adjustPosEnemy(enemies)
        self.rect.center = self.pos
        for projectile in self.projectiles:
            projectile.update(player)
            if projectile.destroyed:
                self.projectiles.remove(projectile)
        if self.shootTimer < self.shootCooldown:
            self.shootTimer += 1
        self.healthPacks = healthPacks

    def idleUpdate(self,player):
        distance = dist(self.pos,player.pos)
        if distance < self.followDistance:
            self.state = "follow"

    def followUpdate(self,player):
        distance = dist(self.pos,player.pos)
        if distance > self.followDistance:
            self.state = "idle"
        if distance < self.attackDistance:
            self.attackDirection = Vector2(player.pos) - Vector2(self.pos)
            self.attackDirection.normalize_ip()
            self.state = "attack"
        self.direction = player.pos - self.pos
        self.pos += self.direction.normalize()*self.speed

    def attackUpdate(self,player):
        #DO ATTACK CODE HERE
        if self.shootTimer >= self.shootCooldown:
            self.shoot(player)
            self.shootTimer = 0
        distance = dist(self.pos,player.pos)
        if distance > self.attackDistance:
            self.state = "follow"


    def shoot(self,player):
        speed = 7
        direction = player.pos - self.pos
        self.projectiles.append(Projectile(self.pos,direction,speed))

    def adjustPosEnemy(self,enemies):
        otherEnemies = []
        for enemy in enemies:
            if enemy != self:
                otherEnemies.append(enemy)
        if len(otherEnemies) > 0:
            closestEnemy = otherEnemies[0]
            for enemy in otherEnemies:
                distance = dist(self.pos,enemy.pos)
                if distance < dist(self.pos,closestEnemy.pos):
                    closestEnemy = enemy
            if dist(self.pos,closestEnemy.pos) < self.size:
                direction = closestEnemy.pos - self.pos
                self.pos -= direction.normalize()*self.speed

    def gotHit(self,damage):
        self.health -= damage
        if self.health <= 0:
            value = randint(1,5)
            if value == 1:
                self.healthPacks.append(HealthPack(self.pos))
            self.destroyed = True

class HealthPack:
    def __init__(self,pos):
        self.pos = pos
        self.image = pygame.Surface([32,32])
        self.image.fill("green")
        self.rect = self.image.get_rect(center = self.pos)
        self.healAmount = 10
        self.destroyed = False

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def update(self,player):
        self.rect.center = self.pos
        if self.rect.colliderect(player.rect):
            healthToAdd = player.health + self.healAmount
            if healthToAdd > player.maxHealth:
                player.health = player.maxHealth
            else:
                player.health = healthToAdd
            self.destroyed = True

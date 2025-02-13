import pygame
from pygame.math import Vector2

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
        self.image = pygame.Surface([50,50])
        #the self is used to tell python that the specific variable/functions is part of the class/object
        self.pos = Vector2(250,250)
        self.color = "red"
        self.rect = self.image.get_rect(center = self.pos)
        self.speed = 2
        self.vel = Vector2(0,0) #self.vel[0] is how fast we are moving in the x direction, and self.vel[1] is how fast we are moving in the y direction

    #methods describe what an object does
    #fore example in the class Dog, a dog might bark, run, or play

    def draw(self,screen):
        self.image.fill(self.color)
        screen.blit(self.image,self.rect)

    def move(self):
        self.vel = Vector2(0,0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel[0] = -self.speed
        if keys[pygame.K_RIGHT]:
            self.vel[0] = self.speed
        if keys[pygame.K_DOWN]:
            self.vel[1] = self.speed
        if keys[pygame.K_UP]:
            self.vel[1] = -self.speed
        if self.vel != Vector2(0,0):
            self.vel.clamp_magnitude_ip(self.speed)
        self.pos += self.vel
        self.rect.center = self.pos

class Sword:
    def __init__(self):
        self.image = pygame.image.load("sword.png")
        #Can you make other instance variables 




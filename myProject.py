import pygame

#set up code

pygame.init()
#setting up the pygame screen
WIDTH = 800
HEIGHT = 640
screen = pygame.display.set_mode([WIDTH,HEIGHT])

#set game title
pygame.display.set_caption("My Game Title")

#set up the pygame clock
clock = pygame.time.Clock()
fps = 60

#set up colors
white = [255,255,255]
black = [0,0,0]
yellow = [255,255,0]

#set up functions for game objects
#each game object should have 3 functions
#1. first function is the create function
#this should create a dictionary that defines the game object
#2. second function is the set function
#this should set the keys in the game object dictionary to values
#3. the third function is the update function
#This should tell pygame what the game object does each frame

#this is the player object
def createPlayer():
    player = {
        "x" : 0,
        "y" : 0,
        "width" : 0,
        "height" : 0,
        "rect" : pygame.Rect(0,0,0,0),
        "color" : yellow
    }
    return player

def setPlayer(player):
    player["x"] = WIDTH/2
    player["y"] = HEIGHT/2
    player["width"] = 50
    player["height"] = 50
    player["rect"].center = [player["x"],player["y"]]
    player["rect"].width = player["width"]
    player["rect"].height = player["height"]

def updatePlayer(player):
    player["rect"].center = [player["x"],player["y"]]
    pygame.draw.rect(screen,player["color"],player["rect"])

#creating player object from the player functions
player = createPlayer()
setPlayer(player)

#GameLoop
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill("white")
    pygame.display.update()
    clock.tick(fps)
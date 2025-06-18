import pygame
from random import randint
import math

pygame.init()

SWIDTH,SHEIGHT = 500,500
screen = pygame.display.set_mode((SWIDTH,SHEIGHT),vsync=1)
clock = pygame.time.Clock()
fps = 60

playerPos = [SWIDTH/2,SHEIGHT/2]
playerVel = [0,0] #velocity is the speed of the player and direction 
#playerSize = 15
jumpVel = 7

playerImage = pygame.image.load("flappyBird/player.png")
playerRect = playerImage.get_rect(center = playerPos)

gravity = 10
dt = 0 #dt stands for deltaTime

pillarSpeed = 250

score = 0

state = "start"

def movePlayer():
    playerVel[1] += gravity * dt
    playerPos[0] += playerVel[0]
    playerPos[1] += playerVel[1]
    playerRect.center = playerPos
    if playerPos[1] + playerRect.height/2 > SHEIGHT:
        playerPos[1] = SHEIGHT - playerRect.height/2
        playerVel[1] = 0
    if playerPos[1] - playerRect.height/2 < 0:
        playerPos[1] = playerRect.height/2
        playerVel[1]= 0


def createPillar(startPos):
    gapSize = 200
    minSize = 20
    pillarWidth = 50
    topPillarHeight = randint(minSize, SHEIGHT - (minSize + gapSize))
    bottomPillarHeight = SHEIGHT - (gapSize + topPillarHeight)
    topPillar = pygame.Rect(startPos,0,pillarWidth,topPillarHeight)
    bottomPillar = pygame.Rect(startPos,SHEIGHT-bottomPillarHeight,pillarWidth,bottomPillarHeight)
    canAddScore = True
    return [topPillar,bottomPillar,canAddScore]

pillar = createPillar(425)

def drawPillar(pillar):
    for p in pillar:
        if isinstance(p,pygame.Rect):
            body = pygame.Surface([p.width,p.height])
            top = pygame.Surface([p.width + 25,25])
            body.fill("green")
            top.fill("dark green")
            screen.blit(body,p)
            if p.y <= 0:
                screen.blit(top,top.get_rect(midbottom = p.midbottom))
            else:
                screen.blit(top,top.get_rect(midtop = p.midtop))

def movePillar(pillar,dt):
    for p in pillar:
        if isinstance(p,pygame.Rect):
            speed = math.floor(pillarSpeed*dt)
            p.x -= speed
        

def checkPillar(pillar):
    if pillar[0].right <= 0:
        return True
    else:
        return False
    
def addScore():
    global score
    if pillar[0].x < playerPos[0] and pillar[2] == True:
        score += 1
        pillar[2] = False

def pillarCollide(pillar,playerRect):
    global state
    for p in pillar:
        if isinstance(p,pygame.Rect):
            if p.colliderect(playerRect):
                state = "gameOver"

    
def playLoop(events):
    global isRunning,pillar,dt
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playerVel[1] = -jumpVel
    movePlayer()
    movePillar(pillar,dt)
    pillarCollide(pillar,playerRect)
    screen.fill("black")
    drawPillar(pillar)
    if checkPillar(pillar):
        pillar = createPillar(SWIDTH)
    addScore()
    #pygame.draw.circle(screen,"red",playerPos,playerSize)
    screen.blit(playerImage,playerRect)
    dt = clock.tick(fps)/1000
    pygame.display.update()

def gameOverLoop(events):
    global isRunning, state, score, pillar, playerPos
    font = pygame.font.SysFont(None,64)
    buttonFont = pygame.font.SysFont(None,46)
    gameOverText = font.render("GAME OVER", True, "black")
    scoreText = font.render("FINAL SCORE: " + str(score),True,"black")
    playText = buttonFont.render("RESTART", True, "black")
    playRect = pygame.Rect(0,0,150,75)
    playRect.midleft = [75,SHEIGHT * .75]
    quitText = buttonFont.render("QUIT", True, "black")
    quitRect = pygame.Rect(0,0,150,75)
    quitRect.midright = [SWIDTH - 75, SHEIGHT *.75]
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            if quitRect.collidepoint(event.pos):
                pygame.quit()
            if playRect.collidepoint(event.pos):
                score = 0
                pillar = createPillar(SWIDTH)
                playerPos = [SWIDTH/2,SHEIGHT/2]
                state = "play"
    screen.fill("red")
    screen.blit(gameOverText,gameOverText.get_rect(midtop = [SWIDTH/2, 25]))
    screen.blit(scoreText,scoreText.get_rect(midtop = [SWIDTH/2, 100]))
    pygame.draw.rect(screen, "green", playRect)
    pygame.draw.rect(screen, "dark red", quitRect)
    screen.blit(playText,playText.get_rect(center = playRect.center))
    screen.blit(quitText,quitText.get_rect(center = quitRect.center))
    clock.tick(fps)
    pygame.display.update()

def startLoop(events):
    global isRunning,state
    font = pygame.font.SysFont(None,64)
    bRect = pygame.Rect(0,0,150,75)
    bRect.center = [SWIDTH/2,SHEIGHT/2]
    startText = font.render("FLAPPY BIRD", True, "black")
    buttonText = font.render("play",True,"black")
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            if bRect.collidepoint(event.pos):
                state = "play"
    screen.fill("white")
    screen.blit(startText, startText.get_rect(midtop = [SWIDTH/2,25]))
    pygame.draw.rect(screen,"green",bRect)
    screen.blit(buttonText,buttonText.get_rect(center = bRect.center))
    clock.tick(fps)
    pygame.display.update()




isRunning = True

while isRunning:
    pygame.display.set_caption("Score: " + str(score))
    events = pygame.event.get()
    if state == "play":
        playLoop(events)
    elif state == "gameOver":
        gameOverLoop(events)
    elif state == "start":
        startLoop(events)
    
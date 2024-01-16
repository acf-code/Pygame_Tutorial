import pygame
import random
from pygame.math import Vector2

pygame.init()

#set up projectile - projectile means a flying object
def createProjectile(x,y):
    projectile ={
        "width" : 10,
        "height" : 30,
        "x" : x,
        "y" : y,
        "rect" : pygame.Rect(0,0,0,0),
        "speed" : -15,
        "velocity" : Vector2(0),
        "destroyed" : False
    }
    return projectile

#function to update the projectile up the screen
def updateProjectile(projectile,screen):
    #projectile["velocity"][0] = projectile["speed"]
    projectile["velocity"][1] = projectile["speed"]
    projectile["y"] += projectile["velocity"][1]
    projectile["x"] += projectile["velocity"][0]
    projectile["rect"].center = [projectile["x"],projectile["y"]]
    projectile["rect"].width = projectile["width"]
    projectile["rect"].height = projectile["height"]
    pygame.draw.rect(screen,[255,0,0],projectile["rect"])
    #destroy projectile if it out of screen
    if projectile["rect"].bottom < 0:
        projectile["destroyed"] = True

#funtion to detect if projectile hits enemy
def collideProjectile(projectile,enemies):
    global score
    for e in enemies:
        if projectile["rect"].colliderect(e["rect"]):
            score += 1
            projectile["destroyed"] = True
            e["destroyed"] = True

#set up enemy
def createEnemy():
    enemy = {
        "width" : 50,
        "height" : 50,
        "x" : 0,
        "y" : 0,
        "rect" : pygame.Rect(0,0,0,0),
        "speed" : 3,
        "velocity" : Vector2(0),
        "image" : random.choice([pygame.image.load("enemy.png"),pygame.image.load("enemy2.png")]),
        "destroyed" : False
    }
    return enemy

#function to set up our enemies
def enemysetup(enemy):
    enemy["x"] = random.randint(0,WIDTH - enemy["width"])
    enemy["y"] = 0
    enemy["rect"].x = enemy["x"]
    enemy["rect"].y = enemy["y"]
    enemy["rect"].height = enemy["height"]
    enemy["rect"].width = enemy["width"]
    enemy["velocity"][1] = enemy["speed"]
    enemy["image"] = pygame.transform.scale(enemy["image"],[enemy["width"],enemy["height"]])

#funtion to update our enemy in the game loop
def enemyupdate(enemy,screen):
    enemy["rect"].centery += enemy["velocity"][1]
    screen.blit(enemy["image"],enemy["rect"])
    if enemy["rect"].top > HEIGHT:
        enemysetup(enemy)

#funtion that detects if enemy collides with player
def enemycollide(enemy,player):
    if enemy["rect"].colliderect(player):
        return True
    else:
        return False
    
def updateEnemyList():
    global player_destroyed
    global enemies
    for e in enemies:
        enemyupdate(e,screen)
        if e["destroyed"]:
            enemies.remove(e)
        player_destroyed = enemycollide(e,player)
        if player_destroyed:
            break

WIDTH = 800
HEIGHT = 640
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
fps = 60

#Setting up background image
background_img = pygame.image.load("background.png")
background_img = pygame.transform.scale(background_img,[WIDTH,HEIGHT])

white = [255, 255, 255]
black = [0, 0, 0]

# set up player
player_img = pygame.image.load("player.png")
p_width = 50
p_height = 50
player = pygame.Rect(0, 0, p_width, p_height)  # x,y,w,h
player.center = [WIDTH / 2, HEIGHT / 2]
player_img = pygame.transform.scale(player_img,[p_width,p_height])
player_destroyed_img = pygame.image.load("player_destroyed.png")
player_destroyed_img = pygame.transform.scale(player_destroyed_img,[p_width,p_height])
player_destroyed = False
p_projectiles = []

#set up score system
score = 0
scoreFont = pygame.font.SysFont("Arial",48)


#list to hold all enemy dictionaries
enemies = []
numberofenemies = 3
wave = 1
for i in range(numberofenemies):
    enemies.append(createEnemy())

#setting up each enemy in enemy list with the enemy setup function
for e in enemies:
    enemysetup(e)


#Velocity as a Zero Vector = [v_x = 0, v_y = 0]
v = Vector2(0) #v = [0,0]
speed = 3

while True:
    m = v.magnitude()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:  # setting our velocity
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                v[0] = speed
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                v[0] = -speed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                v[1] = -speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                v[1] = speed
        if event.type == pygame.KEYUP:  # setting Velocity to be zero
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                v[0] = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                v[0] = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                v[1] = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                v[1] = 0
            if event.key == pygame.K_SPACE:
                p_projectiles.append(createProjectile(player.centerx,player.centery))

    #to stop at screen edges
    if player.left < 0:
        v[0] = 0
        player.left = 0
    if player.right > WIDTH:
        v[0] = 0
        player.right = WIDTH
    if player.top < 0:
        v[1] = 0
        player.top = 0
    if player.bottom > HEIGHT:
        v[1] = 0
        player.bottom = HEIGHT
    
    if v != Vector2(0):
        v = v.normalize()
        v = v*speed

    if m != v.magnitude():
        print(v.magnitude()) #how long my velocity vector is
        m = v.magnitude()

    # add our velocity to our centerx and centery
    if player_destroyed: #if player was destroyed turn off movement
        v = Vector2(0)
    player.centerx += v[0]
    player.centery += v[1]
    # set the background color to be white
    screen.fill(white)
    # display the background image
    screen.blit(background_img,[0,0])

    #display our score
    scoreText = scoreFont.render("Score: " + str(score),True,[255,0,0])
    screen.blit(scoreText,[0,0])

    #update our player projectiles
    if len(p_projectiles) > 0 and not player_destroyed:
        for p in p_projectiles:
            updateProjectile(p,screen)
            collideProjectile(p,enemies)
            if p["destroyed"]:
                p_projectiles.remove(p)

    #update our enemy every frame
    if player_destroyed == False:
        updateEnemyList()
        if len(enemies) == 0: #all enemies are dead(the length of the enemy list is zero)
            numberofenemies += wave
            for i in range(numberofenemies):
                enemies.append(createEnemy())
            for e in enemies:
                enemysetup(e)
            wave += 1
        

    #pygame.draw.rect(screen, black, player)
    #if player was hit show the destroyed image instead of the player image
    if player_destroyed:
        screen.blit(player_destroyed_img,player)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player.center = [WIDTH/2,HEIGHT/2]
                    for e in enemies:
                        enemysetup(e)
                    player_destroyed = False
    else:
        screen.blit(player_img,player)
    # move on and update to the next frame
    pygame.display.update()
    clock.tick(fps)
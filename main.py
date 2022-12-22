#setup
import pygame
from pygame.math import Vector2
from random import randint

pygame.init()

size = [500, 500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

#color = (r,g,b)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
orange = (255, 150, 30)
isRunning = True
#rectanglename = pygame.Rect(x,y,width,height)
r_x = 225
r_y = 200
#t_x = 0
#t_y = 0
#target = pygame.Rect([t_x, t_y], [50, 50])
x_change = 0
y_change = 0
projectiles = []
p_speed = 7
background=pygame.image.load("background.png")
gameover=pygame.image.load("gameover.png")

#class is like a blueprint
#ex. class Name:
class Player:

    def __init__(self, pos, health, speed, image):
        self.pos = Vector2(pos)
        self.health = health
        self.max_health = health
        self.speed = speed
        self.image_raw = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image_raw, [64, 64])
        self.rect = self.image.get_bounding_rect()
        self.health_rect = pygame.Rect([10,465],[self.health,25])
        self.damage_rect = pygame.Rect([10,465],[self.max_health,25])
        self.vel = Vector2(0)
        self.invincibility = 60

    def move(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.vel[0] = self.speed
                if event.key == pygame.K_LEFT:
                    self.vel[0] = -self.speed
                if event.key == pygame.K_UP:
                    self.vel[1] = -self.speed
                if event.key == pygame.K_DOWN:
                    self.vel[1] = self.speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.vel[0] = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.vel[1] = 0
        if self.vel.magnitude() > self.speed:
            self.vel.scale_to_length(self.speed)
        if self.pos[0] <= 0:
            self.pos[0] = 0
        if self.pos[0] >= 436:
            self.pos[0] = 436
        if self.pos[1] <= 0:
            self.pos[1] = 0
        if self.pos[1] >= 436:
            self.pos[1] = 436
        self.pos += self.vel
        
        

    def render(self):
        screen.blit(self.image, self.pos)
        self.rect.center = [self.pos[0] + 32, self.pos[1] + 32]
        pygame.draw.rect(screen,red,self.damage_rect)
        pygame.draw.rect(screen,green,self.health_rect)
        #pygame.draw.rect(screen, white, self.rect)

    def update(self, events):
        self.move(events)
        self.render()
        if self.invincibility<60:
            self.invincibility+=1
        
    def damage(self):
        if self.invincibility>=60:
            self.health -= 10
            self.health_rect = pygame.Rect([10,465],[self.health,25])  
            self.invincibility = 0

class Enemy:
    #method is a funtion inside the class
    #the first method for any class is called the constructor method
    def __init__(self, pos, health, size, color):
        #instance variables from these parameters
        self.pos = pos
        self.health = health
        self.size = size
        self.area = self.size[0] * self.size[1]
        self.color = color
        self.save_color = color
        self.max_speed = 5 - (self.area / 1500)
        self.velocity = Vector2(randint(1, 7), randint(1, 7))
        self.rect = pygame.Rect(self.pos, self.size)
        self.hit_timer = fps

    def move(self):
        if self.velocity.magnitude() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)
        if self.pos[0] < 0:
            self.pos[0] = 0
            self.velocity[0] = -self.velocity[0]
        if self.pos[0] > 500:
            self.pos[0] = 500
            self.velocity[0] = -self.velocity[0]
        if self.pos[1] < 0:
            self.pos[1] = 0
            self.velocity[1] = -self.velocity[1]
        if self.pos[1] > 500:
            self.pos[1] = 500
            self.velocity[1] = -self.velocity[1]
        self.pos += self.velocity
        self.rect.topleft = self.pos

    def render(self):
        if self.hit_timer < fps:
            self.color = red
            self.hit_timer += 1
        else:
            self.color = self.save_color
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        self.move()
        self.render()

    def attack(self):
        pass

    def damage(self):
        self.health -= 1
        self.hit_timer = 0


#to create an object follow this syntax
#object_name = Class_name(paramters)
bob = Enemy([250, 250], 3, [50, 50], (0, 0, 255))
joe = Enemy([0, 0], 5, [70, 70], (255, 0, 255))
enemies = [bob, joe]
player = Player([r_x, r_y], 100, 3, "spaceship.png")
waves=3
#game loop(updates each frame of the game)
while isRunning == True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projectiles.append(
                    pygame.Rect([player.pos[0] + 5, player.pos[1]], [10, 10]))
    #cannonTip.topleft = [rect_pos[0] - 2.5, rect_pos[1]]
    #target.topleft = [t_x, t_y]
    if player.health<=0:
        for i in range(fps*5):
            screen.blit(gameover,[0,0])
            pygame.display.flip()
        isRunning = False
        pygame.quit()
    screen.blit(background,[0,0])
    player.update(events)
    #pygame.draw.rect(screen, red, target)
    if len(enemies) > 0:
        for enemy in enemies:
            enemy.update()
            for projectile in projectiles:
                if projectile.colliderect(enemy.rect):
                    enemy.damage()
                    projectiles.remove(projectile)
            if enemy.health <= 0:
                enemies.remove(enemy)
            if enemy.rect.colliderect(player.rect):
                player.damage()
    if len(enemies) == 0:
        for i in range(waves):            
            random_color=(randint(0,255),randint(0,255),randint(0,255))
            enemies.append(Enemy([randint(0,400), randint(0,400)], 3, [randint(50,100), randint(50,100)], random_color))
        waves+=1
    print(bob.pos)
    if len(projectiles) > 0:
        for projectile in projectiles:
            pygame.draw.rect(screen, orange, projectile)
            projectile.y -= p_speed
            if projectile.y < 0:
                projectiles.remove(projectile)
    clock.tick(fps)
    pygame.display.update()

pygame.quit()

#Homework:
#Can you make the player take damage if it is hit by the enemy rect
#Challenge:
#Can you make images for the enemy as well

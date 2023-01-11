#setup
import pygame
from pygame.math import Vector2
from random import randint
import objects, tools,level1,menu

scene = "menu"

if scene == "menu":
    scene = menu.gameloop()
if scene == "level1":
    level1.gameloop()


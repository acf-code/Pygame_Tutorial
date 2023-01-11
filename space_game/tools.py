import pygame
from pygame.math import Vector2
from random import randint

fps = 60
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
orange = (255, 150, 30)


def increase_time(time,start_frame,fps):
    t = time
    s_f = start_frame
    if start_frame >= fps:
        t += 1
        s_f = 0
    else:
        s_f += 1
    return t,s_f


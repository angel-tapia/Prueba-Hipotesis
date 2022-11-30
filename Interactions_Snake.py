import pygame
from Constants_Snake import *

def parsingKey(key, direction):
    if key[pygame.K_DOWN]:
        return "Down"
    if key[pygame.K_UP]:
        return "Up"
    if key[pygame.K_RIGHT]:
        return "Right"
    if key[pygame.K_LEFT]:
        return "Left"
    return direction

def isPause(key, pause):
    if key[pygame.K_p]:
        pause = not pause
    return pause
        

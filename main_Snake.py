import pygame
import random
from Constants_Snake import *
from Class_Snake import *
from Interactions_Snake import *
from Snake_Game import *

def runSnake():
    game = Game()
    while game.running :
        game.simulate()
        game.draw()
    while game.end:
        game.over()

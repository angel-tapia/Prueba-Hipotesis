import pygame
import random
from Constants_Breakout import *
from Class_Breakout import *
from Interactions_Breakout import *
from Breakout_Game import *

def runBreakout():
    game = Game()
    while game.running :
        game.simulate()
        game.draw()
    while game.end:
        game.over()

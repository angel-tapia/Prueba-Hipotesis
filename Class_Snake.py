import pygame
import random
from Constants_Snake import *

class Snake:

    def __init__ (self):
        initPos = screenSize/2
        self.body = [ (initPos, initPos) ]
        self.direction = "Left"

    def move(self):
        (x, y) = self.body[0]
        (dx, dy) = movMap[self.direction]
        newHead = (x+dx, y+dy)
        self.body.insert(0, newHead)

    def valid(self):
        (x, y) = self.body[0]
        if x < 0 or x > screenSize-pixelSize or y < 0 or y > screenSize-pixelSize:
            return False
        head = self.body[0]
        if self.body.count(head) > 1:
            return False
        return True

    def setDirection(self, direction):
        if len(self.body) is 1:
            self.direction = direction
            return
        indexDir = directions.index(self.direction)
        indexNewDir = directions.index(direction)
        if (indexDir+2)%4 is not indexNewDir:
            self.direction = direction

    def pop(self):
        self.body.pop()

class Food:
    def generateCoords(self):
        return (random.randint(1, lim)*pixelSize, random.randint(1, lim)*pixelSize)

    def appearFood(self, snake):
         #while the new food is in the body of the snake appear a new food
        while self.pos in snake.body:
            self.pos = self.generateCoords()

    def __init__ (self):
        self.pos = self.generateCoords()

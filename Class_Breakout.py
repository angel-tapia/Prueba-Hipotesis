import pygame
import random
from Constants_Breakout import *

class Ball(pygame.sprite.Sprite):

    def __init__ (self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((widthBall, heightBall))
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((0, 0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.directionX = -1
        self.directionY = -1
        self.randomSpeed = 0

    def flipDirectionX (self):
        self.directionX *= -1

    def flipDirectionY (self):
        self.directionY *= -1
    
    def move(self):
        self.rect.x += speedBall * self.directionX
        self.rect.y += (speedBall + self.randomSpeed) * self.directionY

    def valid(self):
        if self.rect.x <= 0 or self.rect.x >= screenWidth-widthBall:
            self.flipDirectionX()
        if self.rect.y <= 0:
            self.flipDirectionY()
        if self.rect.y > screenHeight:
            return False
        else :
            return True


class Brick(pygame.sprite.Sprite):

    def __init__ (self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((widthBrick, heightBrick))
        self.image.fill((200, 100, 200))
        self.image.set_colorkey((0, 0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Paddle(pygame.sprite.Sprite):

    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((widthPaddle, heightPaddle))
        self.image.fill((146, 168, 209))
        self.image.set_colorkey((0, 0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (screenWidth//2, screenHeight-100)

    def move(self):
        if self.direction is "Left":
            self.rect.x -= speed
        if self.direction is "Right":
            self.rect.x += speed
        self.isValid()
        
    def isValid(self):
        if self.rect.x + widthPaddle > screenWidth:
            self.rect.x = screenWidth-widthPaddle
        if self.rect.x < 0:
            self.rect.x = 0

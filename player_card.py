from pygame.rect import Rect
import pygame
import random
from main import screen
from enum import Enum


class Color(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3


class card:
    image: pygame.Surface
    hitbox: Rect
    color: Color
    def __init__ (self):
        self.color = random.choice(list(Color))
        self.isAlive = True
    def draw(self):
        if self.isAlive == True:
            pygame.draw.rect(screen, (100, 50, 100), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))
    def use(self):
        self.isAlive = False
    def updatePos(self, x, y):
        self.hitbox.update(x, y, self.hitbox.width, self.hitbox.height)

class plaincard(card):
    def __init__ (self):
        super().__init__()
        self.number = random.randrange(0, 10)
        


class plustwo(card):
    pass
    #opponets_cards.append (something like that I think idk rlly just lmk what ur thinking)
class skipcard(card):
    pass

class reversecard(card):
    pass

class plusfour(card):
    pass
        
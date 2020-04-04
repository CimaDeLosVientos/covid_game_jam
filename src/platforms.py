from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *

class Platform():
    def __init__(self, position):
        super(Platform, self).__init__()
        self.x = position[0]
        self.y = position[1]
        
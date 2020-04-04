from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *

class Platform(sprite.Sprite):
    def __init__(self, position, image):
        sprite.Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        self.image = load_image("assets/images/sprites/{}.png".format(image))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self, time, player):
        displacement = player.get_displacement(time)
        self.move(displacement)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def move(self, displacement):
        self.x += displacement[0]
        self.y += displacement[1]
        
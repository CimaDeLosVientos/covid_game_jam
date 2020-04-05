from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *

class Platform(sprite.Sprite):
    def __init__(self, position, image):
        sprite.Sprite.__init__(self)
        self.x = self.initial_x = position[0]
        self.y = self.initial_y = position[1]
        self.image = load_image("assets/images/sprites/{}.png".format(image))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self, displacement, player):
        self.move(displacement)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


    def move(self, displacement):
        self.x += displacement[0]
        self.y += displacement[1]
        

    def restart(self):
        self.x = self.initial_x
        self.y = self.initial_y + RESET_DISTANCE




class FloatPlatform(Platform):
    def __init__(self, position, distance, image):
        super(FloatPlatform, self).__init__(position, image)
        self.distance = distance
        self.current = 0
        self.orientation = 1


class FloatPlatformHorizontal(FloatPlatform):
    def __init__(self, position, distance, image):
        super(FloatPlatformHorizontal, self).__init__(position, distance, image)

    def move(self, displacement):
        super(FloatPlatformHorizontal, self).move(displacement)
        self.x += 1 * self.orientation
        self.current += 1
        if self.current == self.distance:
            self.orientation *= -1
            self.current = 0

class FloatPlatformHorizontalInverted(FloatPlatform): # Distance is negative
    def __init__(self, position, distance, image):
        super(FloatPlatformHorizontalInverted, self).__init__(position, distance, image)

    def move(self, displacement):
        super(FloatPlatformHorizontalInverted, self).move(displacement)
        self.x += -1 * self.orientation
        self.current -= 1
        if self.current == self.distance:
            self.orientation *= -1
            self.current = 0


class FloatPlatformVertical(FloatPlatform):
    def __init__(self, position, distance, image):
        super(FloatPlatformVertical, self).__init__(position, distance, image)


    def move(self, displacement):
        super(FloatPlatformVertical, self).move(displacement)
        self.y += 1 * self.orientation
        self.current += 1
        if self.current == self.distance:
            self.orientation *= -1
            self.current = 0
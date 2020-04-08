from pygame import sprite, transform
from math import ceil
from pygame.locals import *
from .helpers import *
from .parameters import *
import random

class Platform(sprite.Sprite):
    def __init__(self, position, image):
        sprite.Sprite.__init__(self)
        self.x = self.initial_x = position[0]
        self.y = self.initial_y = position[1]
        self.image = load_image("assets/images/sprites/{}.png".format(image))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self, displacement):
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
        self.distance = int(distance / 2)
        self.current = 0
        self.orientation = 1

    def restart(self):
        super(FloatPlatform, self).restart()
        self.current = 0
        self.orientation = 1


class FloatPlatformHorizontal(FloatPlatform):
    def __init__(self, position, distance, image):
        super(FloatPlatformHorizontal, self).__init__(position, distance, image)

    def move(self, displacement):
        super(FloatPlatformHorizontal, self).move(displacement)
        self.x += 2 * self.orientation
        self.current += 1
        if self.current == self.distance:
            self.orientation *= -1
            self.current = 0

class FloatPlatformHorizontalInverted(FloatPlatform): # Distance is negative
    def __init__(self, position, distance, image):
        super(FloatPlatformHorizontalInverted, self).__init__(position, distance, image)

    def move(self, displacement):
        super(FloatPlatformHorizontalInverted, self).move(displacement)
        self.x += -2 * self.orientation
        self.current -= 1
        if self.current == self.distance:
            self.orientation *= -1
            self.current = 0


class FloatPlatformVertical(FloatPlatform):
    def __init__(self, position, distance, image):
        super(FloatPlatformVertical, self).__init__(position, distance, image)


    def move(self, displacement):
        super(FloatPlatformVertical, self).move(displacement)
        self.y += 2 * self.orientation
        self.current += 1
        if self.current == self.distance:
            self.orientation *= -1
            self.current = 0


class FloatPlatformVerticalInverted(FloatPlatform): # Distance is negative
    def __init__(self, position, distance, image):
        super(FloatPlatformVerticalInverted, self).__init__(position, distance, image)

    def move(self, displacement):
        super(FloatPlatformVerticalInverted, self).move(displacement)
        self.y += -2 * self.orientation
        self.current -= 1
        if self.current == self.distance:
            self.orientation *= -1
            self.current = 0



class Cloud(Platform):
    def __init__(self, position):
        super(Cloud, self).__init__(position, "final_cloud")
        self.thunder = True
        self.image_1 = self.image
        self.image_2 = load_image("assets/images/sprites/{}.png".format("final_cloud_2"))
        self.image_3 = load_image("assets/images/sprites/{}.png".format("final_cloud_3"))
        self.collision = Rect((self.rect.left,
                                self.rect.top / 2,
                                self.rect.width,
                                10))
        self.current_image = 0
        self.sound = load_sound("assets/music/thunder.wav")

    def fix(self):
        return (-2, -3)

    def storm(self):
        self.image = self.image_2 if self.current_image < STORM_INTERVAL else self.image_3
        self.current_image = (self.current_image+1) % (STORM_INTERVAL * 2)
        if self.thunder:
            self.sound.play()
            self.thunder = False

    def restart(self):
        super(Cloud, self).restart()
        self.thunder = True
        self.image = self.image_1
        self.current_image = 0



# Decoration
def generate_clouds(coordenate_left_top, coordenate_right_bottom, clouds_amounts):
    clouds = []
    for clouds_index in range(len(clouds_amounts)):
        for ii in range(clouds_amounts[clouds_index]):
            x = random.randrange(coordenate_left_top[0], coordenate_right_bottom[0])
            y = random.randrange(coordenate_left_top[1], coordenate_right_bottom[1])
            clouds.append(Platform((x, y), "cloud_{}".format(clouds_index + 1)))
            print(x,y)
    return clouds

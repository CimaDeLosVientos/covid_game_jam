import pygame, os, random, time as tim
from src.parameters import *
from pygame.locals import *
from src.helpers import *
from src.platforms import *

class GameScene():
    def __init__(self):
        self.next = None


    def load(self, data):
        pass



    def on_event(self, time, event):
        pass


    def on_update(self, time):
        pass


    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 200))


    def finish(self, data):
        pass
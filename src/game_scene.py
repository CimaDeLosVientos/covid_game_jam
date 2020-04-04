import pygame, os, random, time as tim
from src.parameters import *
from pygame.locals import *
from src.helpers import *
from src.platform import *
from src.player import *

class GameScene():
    def __init__(self):
        self.next = None

        # Platforms
        self.platforms = pygame.sprite.Group()
        self.platforms.add(Platform((200, 500), "platform_1"))
        self.platforms.add(Platform((400, 500), "platform_2"))
        self.platforms.add(Platform((600, 500), "platform_3"))

        # Player
        self.player = Player("keyboard", int(WIDTH / 2), int(HEIGHT / 2))


    def load(self, data):
        pass



    def on_event(self, time, event):
        keys = pygame.key.get_pressed()

        # players controls
        self.player.action_keyboard(keys)


    def on_update(self, time):
        self.platforms.update(time, self.player)


    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 200))

        screen.blit(self.player.image, self.player.rect) 
        
        for platform in self.platforms:
            screen.blit(platform.image, platform.rect)


    def finish(self, data):
        pass
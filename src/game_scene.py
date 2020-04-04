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
        

        pl = []
        pl.append(Platform((500, 645), "mar"))
        pl.append(Platform((pl[-1].x + 725, pl[-1].y - 25), "playa"))
        #Escena 2 (Playa)
        pl.append(Platform((pl[-1].x + 300, pl[-1].y - 125), "platform_2"))
        pl.append(Platform((pl[-1].x + 187, pl[-1].y - 50), "platform_3"))
        self.platforms.add(pl)




        #self.platforms.add(Platform((200, 500), "platform_1"))
        #self.platforms.add(Platform((700, 500), "platform_2"))
        #self.platforms.add(Platform((900, 500), "platform_3"))

        self.origen_point_x = 250
        self.origen_point_y = 400
        self.die = False

        # Player
        self.player = Player("keyboard", int(WIDTH / 2), 520)

    def load(self, data):
        pass



    def on_event(self, time, event):
        keys = pygame.key.get_pressed()

        # players controls
        self.player.action_keyboard(keys)


    def on_update(self, time):
        displacement = self.player.get_displacement(time, self.platforms)
        self.player.update(self.platforms)
        self.platforms.update(displacement, self.player)
        if self.player.jump_time < FALL_TIME_OVER and self.platforms.sprites()[0].y < self.origen_point_y:
            for platform in self.platforms:
                platform.restart()


    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 200))

        screen.blit(self.player.image, self.player.rect) 
        
        for platform in self.platforms:
            screen.blit(platform.image, platform.rect)


    def finish(self, data):
        pass
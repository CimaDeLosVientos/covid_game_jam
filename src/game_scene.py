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
        pl.append(Platform((pl[-1].x + 262, pl[-1].y - 100), "platform_2"))
        pl.append(Platform((pl[-1].x + 337, pl[-1].y - 0), "platform_3"))
        pl.append(Platform((pl[-1].x + 299, pl[-1].y - 100), "platform_3"))
        #Escena 3 (Playa)
        pl.append(Platform((pl[-1].x + 262, pl[-1].y - 100), "platform_2"))
        pl.append(Platform((pl[-1].x + 112, pl[-1].y + 100), "platform_1"))
        pl.append(Platform((pl[-1].x + 324, pl[-1].y + 100), "platform_3"))
        pl.append(Platform((pl[-1].x - 12, pl[-1].y - 200), "platform_1"))
        pl.append(Platform((pl[-1].x + 307, pl[-1].y - 50), "platform_2"))
        pl.append(Platform((pl[-1].x + 237, pl[-1].y - 50), "platform_3"))
        #Escena 4 (Campo)
        pl.append(Platform((pl[-1].x + 362, pl[-1].y - 50), "platform_2"))
        pl.append(Platform((pl[-1].x + 300, pl[-1].y - 50), "platform_2"))
        pl.append(Platform((pl[-1].x + 300, pl[-1].y - 50), "platform_2"))
        pl.append(Platform((pl[-1].x + 300, pl[-1].y - 50), "platform_2"))
        #Escena 5 (Campo)
        pl.append(Platform((pl[-1].x + 287, pl[-1].y - 100), "platform_3"))
        pl.append(Platform((pl[-1].x + 324, pl[-1].y - 100), "platform_1"))
        pl.append(Platform((pl[-1].x + 87, pl[-1].y - 200), "platform_2"))
        pl.append(Platform((pl[-1].x + 162, pl[-1].y - 200), "platform_3"))
        #Plataforma que se mueve de arriba abajo
        pl.append(FloatPlatformVertical((pl[-1].x + 337, pl[-1].y + 225), 200, "platform_2"))
        #Escena 6 (Bosque)
        pl.append(Platform((pl[-1].x + 150, pl[-1].y + 400), "platform_2"))
        pl.append(Platform((pl[-1].x + 350, pl[-1].y - 0), "platform_2"))
        pl.append(Platform((pl[-1].x + 112, pl[-1].y - 50), "platform_1"))
        pl.append(Platform((pl[-1].x + 137, pl[-1].y - 200), "platform_2"))
        pl.append(Platform((pl[-1].x + 212, pl[-1].y - 150), "platform_1"))
        pl.append(Platform((pl[-1].x + 374, pl[-1].y - 0), "platform_3"))
        #Escena 7 (Bosque)
        pl.append(Platform((pl[-1].x + 224, pl[-1].y + 50), "platform_1"))
        pl.append(Platform((pl[-1].x + 237, pl[-1].y + 50), "platform_2"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y + 100), "platform_1"))
        pl.append(Platform((pl[-1].x + 149, pl[-1].y + 50), "platform_1"))
        #Platafoma que sube y baja
        pl.append(FloatPlatformVertical((pl[-1].x + 237, pl[-1].y - 300), 175, "platform_2"))
        pl.append(Platform((pl[-1].x + 137, pl[-1].y - 200), "platform_3"))
        #Escena 8 (Monte)
        pl.append(Platform((pl[-1].x + 249, pl[-1].y - 100), "platform_3"))
        pl.append(Platform((pl[-1].x + 187, pl[-1].y - 100), "platform_2"))
        pl.append(Platform((pl[-1].x + 150, pl[-1].y - 100), "platform_2"))
        pl.append(Platform((pl[-1].x - 75, pl[-1].y - 200), "platform_1"))
        pl.append(Platform((pl[-1].x + 187, pl[-1].y - 100), "platform_2"))
        pl.append(Platform((pl[-1].x + 337, pl[-1].y + 100), "platform_3"))
        #Escena 9 (Monte)
        pl.append(Platform((pl[-1].x + 337, pl[-1].y - 0), "platform_2"))
        pl.append(Platform((pl[-1].x + 237, pl[-1].y - 0), "platform_1"))
        pl.append(FloatPlatformVertical((pl[-1].x + 224, pl[-1].y - 0), 150, "platform_1"))
        pl.append(Platform((pl[-1].x + 199, pl[-1].y - 0), "platform_1"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y - 0), "platform_2"))
        pl.append(Platform((pl[-1].x + 237, pl[-1].y - 50), "platform_3"))
        #Escena 10 (Montaña)
        pl.append(Platform((pl[-1].x + 374, pl[-1].y + 50), "platform_1"))
        pl.append(Platform((pl[-1].x + 112, pl[-1].y - 200), "platform_3"))
        pl.append(Platform((pl[-1].x + 349, pl[-1].y - 0), "platform_3"))
        #Escena 11 (Montaña)
        pl.append(FloatPlatformVertical((pl[-1].x + 312, pl[-1].y - 250), 500, "platform_2"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y + 250), "platform_1"))
        pl.append(FloatPlatformVertical((pl[-1].x + 262, pl[-1].y - 250), 500, "platform_2"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y + 250), "platform_1"))
        pl.append(FloatPlatformVertical((pl[-1].x + 262, pl[-1].y - 250), 500, "platform_2"))
        # Escena 12 (Nieve)
        pl.append(FloatPlatformHorizontalInverted((pl[-1].x + 537, pl[-1].y + 250), -250, "platform_3"))
        pl.append(Platform((pl[-1].x + 302, pl[-1].y + 200), "platform_2"))
        pl.append(Platform((pl[-1].x + 387, pl[-1].y + 150), "platform_3"))
        # Escena 13 (Nieve)
        pl.append(FloatPlatformHorizontal((pl[-1].x + 299, pl[-1].y + 0), 375, "platform_3"))
        pl.append(Platform((pl[-1].x + 637, pl[-1].y + 0), "platform_2"))
        pl.append(FloatPlatformHorizontal((pl[-1].x + 287, pl[-1].y + 0), 400, "platform_3"))
        # Escena 14 (Nieve)
        pl.append(Platform((pl[-1].x + 687, pl[-1].y + 0), "platform_2"))
        pl.append(Platform((pl[-1].x + 225, pl[-1].y - 150), "platform_2"))
        pl.append(Platform((pl[-1].x + 187, pl[-1].y - 150), "platform_1"))
        pl.append(Platform((pl[-1].x + 187, pl[-1].y - 150), "platform_2"))
        pl.append(Platform((pl[-1].x + 225, pl[-1].y - 150), "platform_2"))
        # Escena 15 (Final)
        pl.append(FloatPlatformHorizontal((pl[-1].x + 187, pl[-1].y + 0), 225, "platform_3"))
        pl.append(FloatPlatformHorizontal((pl[-1].x + 224, pl[-1].y + 0), 225, "platform_3"))


        self.platforms.add(pl)


        self.origen_point_x = 250
        self.origen_point_y = 400
        self.die = False

        # Player
        self.player = Player("keyboard", int(WIDTH / 2), 400)

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

        caca = pygame.Surface((self.player.collision_rect_left.width, self.player.collision_rect_left.height))
        caca.fill((255,0,0))
        screen.blit(caca, self.player.collision_rect_left)

        caca = pygame.Surface((self.player.collision_rect_right.width, self.player.collision_rect_right.height))
        caca.fill((255,255,0))
        screen.blit(caca, self.player.collision_rect_right) 

        caca = pygame.Surface((self.player.collision_rect_down.width, self.player.collision_rect_down.height))
        caca.fill((255,0,255))
        screen.blit(caca, self.player.collision_rect_down)

        caca = pygame.Surface((self.player.collision_rect_top.width, self.player.collision_rect_top.height))
        caca.fill((0,255,255))
        screen.blit(caca, self.player.collision_rect_top)


        for platform in self.platforms:
            screen.blit(platform.image, platform.rect)


    def finish(self, data):
        pass
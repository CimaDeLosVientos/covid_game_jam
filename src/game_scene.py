import pygame, os, random, time as tim
from src.parameters import *
from pygame.locals import *
from src.helpers import *
from src.platform import *
from src.player import *

class GameScene():
    def __init__(self):
        self.next = None

        self.background = load_image("assets/images/scenes/background.png")


        # Platforms
        self.platforms = pygame.sprite.Group()
        

        pl = []
        pl.append(Platform((375, 945), "sea"))
        pl.append(Platform((pl[-1].x + 600, pl[-1].y - 25), "beach"))
        #Escena 2 (Playa = beach)
        pl.append(Platform((pl[-1].x + 300, pl[-1].y - 225), "platform_2_beach"))
        pl.append(Platform((pl[-1].x + 187, pl[-1].y - 50), "platform_3_beach"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y - 100), "platform_2_beach"))
        pl.append(Platform((pl[-1].x + 337, pl[-1].y - 0), "platform_3_beach"))
        pl.append(Platform((pl[-1].x + 299, pl[-1].y - 100), "platform_3_beach"))
        #Escena 3 (Playa)
        pl.append(Platform((pl[-1].x + 262, pl[-1].y - 100), "platform_2_beach"))
        pl.append(Platform((pl[-1].x + 112, pl[-1].y + 100), "platform_1_beach"))
        pl.append(Platform((pl[-1].x + 324, pl[-1].y + 100), "platform_3_beach"))
        pl.append(Platform((pl[-1].x - 12, pl[-1].y - 200), "platform_1_beach"))
        pl.append(Platform((pl[-1].x + 307, pl[-1].y - 50), "platform_2_beach"))
        pl.append(Platform((pl[-1].x + 237, pl[-1].y - 50), "platform_3_beach"))
        #Escena 4 (Campo = grass)
        pl.append(Platform((pl[-1].x + 362, pl[-1].y - 50), "platform_2_grass"))
        pl.append(Platform((pl[-1].x + 300, pl[-1].y - 50), "platform_2_grass"))
        pl.append(Platform((pl[-1].x + 300, pl[-1].y - 50), "platform_2_grass"))
        pl.append(Platform((pl[-1].x + 300, pl[-1].y - 50), "platform_2_grass"))
        #Escena 5 (Campo)
        pl.append(Platform((pl[-1].x + 287, pl[-1].y - 100), "platform_3_grass"))
        pl.append(Platform((pl[-1].x + 324, pl[-1].y - 100), "platform_1_grass"))
        pl.append(Platform((pl[-1].x + 87, pl[-1].y - 150), "platform_2_grass"))
        pl.append(Platform((pl[-1].x + 162, pl[-1].y - 150), "platform_3_grass"))
        #Plataforma que se mueve de arriba abajo
        pl.append(FloatPlatformVertical((pl[-1].x + 337, pl[-1].y + 225), 200, "platform_2_grass"))
        #Escena 6 (Bosque = forest)
        pl.append(Platform((pl[-1].x + 150, pl[-1].y + 400), "platform_2_forest"))
        pl.append(Platform((pl[-1].x + 350, pl[-1].y - 0), "platform_2_forest"))
        pl.append(Platform((pl[-1].x + 112, pl[-1].y - 50), "platform_1_forest"))
        pl.append(Platform((pl[-1].x + 137, pl[-1].y - 150), "platform_2_forest"))
        pl.append(Platform((pl[-1].x + 212, pl[-1].y - 150), "platform_1_forest"))
        pl.append(Platform((pl[-1].x + 374, pl[-1].y - 0), "platform_3_forest"))
        #Escena 7 (Bosque)
        pl.append(Platform((pl[-1].x + 224, pl[-1].y + 50), "platform_1_forest"))
        pl.append(Platform((pl[-1].x + 237, pl[-1].y + 50), "platform_2_forest"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y + 100), "platform_1_forest"))
        pl.append(Platform((pl[-1].x + 149, pl[-1].y + 50), "platform_1_forest"))
        #Platafoma que sube y baja
        pl.append(FloatPlatformVertical((pl[-1].x + 237, pl[-1].y - 300), 175, "platform_2_forest"))
        pl.append(Platform((pl[-1].x + 137, pl[-1].y - 100), "platform_3_forest"))
        #Escena 8 (Monte = dirt)
        pl.append(Platform((pl[-1].x + 249, pl[-1].y - 100), "platform_3_dirt"))
        pl.append(Platform((pl[-1].x + 187, pl[-1].y - 100), "platform_2_dirt"))
        pl.append(Platform((pl[-1].x + 150, pl[-1].y - 100), "platform_2_dirt"))
        pl.append(Platform((pl[-1].x - 175, pl[-1].y - 150), "platform_1_dirt"))
        pl.append(Platform((pl[-1].x + 290, pl[-1].y - 100), "platform_2_dirt"))
        pl.append(Platform((pl[-1].x + 337, pl[-1].y + 100), "platform_3_dirt"))
        #Escena 9 (Monte)
        pl.append(Platform((pl[-1].x + 337, pl[-1].y - 0), "platform_2_dirt"))
        pl.append(Platform((pl[-1].x + 237, pl[-1].y - 0), "platform_1_dirt"))
        pl.append(FloatPlatformVertical((pl[-1].x + 224, pl[-1].y - 0), 150, "platform_1_dirt"))
        pl.append(Platform((pl[-1].x + 199, pl[-1].y - 0), "platform_1_dirt"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y - 0), "platform_2_dirt"))
        pl.append(Platform((pl[-1].x + 237, pl[-1].y - 50), "platform_3_dirt"))
        #Escena 10 (Montaña = stone)
        pl.append(Platform((pl[-1].x + 374, pl[-1].y + 50), "platform_1_stone"))
        pl.append(Platform((pl[-1].x + 112, pl[-1].y - 150), "platform_3_stone"))
        pl.append(Platform((pl[-1].x + 349, pl[-1].y - 0), "platform_3_stone"))
        #Escena 11 (Montaña)
        pl.append(FloatPlatformVertical((pl[-1].x + 312, pl[-1].y - 250), 500, "platform_2_stone"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y + 250), "platform_1_stone"))
        pl.append(FloatPlatformVertical((pl[-1].x + 262, pl[-1].y - 250), 500, "platform_2_stone"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y + 250), "platform_1_stone"))
        pl.append(FloatPlatformVertical((pl[-1].x + 262, pl[-1].y - 250), 500, "platform_2_stone"))
        # Escena 12 (Nieve = snow)
        pl.append(FloatPlatformHorizontalInverted((pl[-1].x + 537, pl[-1].y + 250), -250, "platform_3_snow"))
        pl.append(Platform((pl[-1].x + 302, pl[-1].y + 200), "platform_2_snow"))
        pl.append(Platform((pl[-1].x + 387, pl[-1].y + 150), "platform_3_snow"))
        # Escena 13 (Nieve)
        pl.append(FloatPlatformHorizontal((pl[-1].x + 299, pl[-1].y + 0), 375, "platform_3_snow"))
        pl.append(Platform((pl[-1].x + 637, pl[-1].y + 0), "platform_2_snow"))
        pl.append(FloatPlatformHorizontal((pl[-1].x + 287, pl[-1].y + 0), 400, "platform_3_snow"))
        # Escena 14 (Nieve)
        pl.append(Platform((pl[-1].x + 687, pl[-1].y + 0), "platform_2_snow"))
        pl.append(Platform((pl[-1].x + 225, pl[-1].y - 150), "platform_2_snow"))
        pl.append(Platform((pl[-1].x + 187, pl[-1].y - 150), "platform_1_snow"))
        pl.append(Platform((pl[-1].x + 187, pl[-1].y - 150), "platform_2_snow"))
        pl.append(Platform((pl[-1].x + 225, pl[-1].y - 150), "platform_2_snow"))
        # Escena 15 (Final)
        #pl.append(FloatPlatformHorizontal((pl[-1].x + 313, pl[-1].y + 0), 225, "platform_3"))
        #pl.append(FloatPlatformHorizontal((pl[-1].x + 224, pl[-1].y + 0), 225, "platform_3"))
        self.cloud = Cloud((pl[-1].x + 413, pl[-1].y + 50))
        self.cloud = Cloud((-400, 1000))

        self.platforms.add(pl)
        self.platforms.add(self.cloud)

        self.end = False
        self.end_time = 0

        self.origen_point_x = 250
        self.origen_point_y = 400
        self.die = False

        # Player
        self.player = Player("keyboard", int(WIDTH / 2), int(HEIGHT / 2))

    def load(self, data):
        pass


    def on_event(self, time, event):
        keys = pygame.key.get_pressed()

        # players controls
        self.player.action_keyboard(keys)


    def on_update(self, time):
        if sprite.collide_rect(self.cloud, self.player):
            self.end = True
        if self.end:
            if self.end_time < FIX_TIME:
                self.platforms.update((0, -3))
            if self.end_time < FLY_TIME:
                self.player.on_air = False
                self.platforms.update((-3, 0))
                self.cloud.update((3, 0))
                self.player.update(self.platforms)
                self.end_time += 1
                return
            elif self.end_time < STORM_TIME:
                self.cloud.storm()
                self.player.update(self.platforms)
                self.end_time += 1
                return
            else:
                self.cloud.storm()
                self.player.on_air = True
                self.end = False
                self.end_time += 1
                self.platforms.update((0, -3))
                return
        displacement = self.player.get_displacement(time, self.platforms)
        self.player.update(self.platforms)
        self.platforms.update(displacement)
        if self.player.velocity < FALL_VELOCITY_OVER and self.platforms.sprites()[0].y < self.origen_point_y:
            for platform in self.platforms:
                platform.restart()
                self.player.dead = True
                self.player.current_frame = 0
                self.player.current_sprite = 3
                self.end_time = 0


    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 200))

        screen.blit(self.background, self.background.get_rect())

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
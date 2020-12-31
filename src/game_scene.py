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

        self.current_track = "None"

        # Platforms and clouds
        self.platforms = pygame.sprite.Group()
        pl = []
        self.clouds = pygame.sprite.Group()
        ca = []
        self.ca = ca
        # generate_clouds(coordenate_left_top, coordenate_right_bottom, amount)
        #ca.append(CloudArea((200, 400), (1000, 700), (2, 3, 1)))
        
        pl.append(Platform((-525, 945), "sea2_inv"))
        pl.append(Platform((525, 945), "sea"))
        pl.append(Platform((pl[-1].x + 600, pl[-1].y - 25), "beach"))
        #Nubes
        ca.append(CloudArea((pl[-1].x + 725, pl[-1].y - 950), (pl[-1].x + 2200, pl[-1].y - 600), (4, 0, 0, 0)))
        ca.append(CloudArea((ca[-1].x + 1475, ca[-1].y - 250), (ca[-1].x + 2500, ca[-1].y + 250), (4, 0, 0, 0)))
        ca.append(CloudArea((ca[-1].x + 1025, ca[-1].y - 300), (ca[-1].x + 1500, ca[-1].y + 200), (2, 1, 0, 0)))
        ca.append(CloudArea((ca[-1].x + 675, ca[-1].y - 300), (ca[-1].x + 1150, ca[-1].y + 300), (2, 1, 0, 0)))
        ca.append(CloudArea((ca[-1].x + 475, ca[-1].y - 50), (ca[-1].x + 1200, ca[-1].y + 350), (1, 1, 0, 0)))
        ca.append(CloudArea((ca[-1].x + 725, ca[-1].y + 0), (ca[-1].x + 1450, ca[-1].y + 850), (1, 1, 0, 0)))
        ca.append(CloudArea((ca[-1].x + 725, ca[-1].y + 100), (ca[-1].x + 2150, ca[-1].y + 600), (1, 2, 1, 0)))
        ca.append(CloudArea((ca[-1].x + 1425, ca[-1].y - 300), (ca[-1].x + 2125, ca[-1].y + 500), (1, 1, 1, 0)))
        ca.append(CloudArea((ca[-1].x + 700, ca[-1].y - 300), (ca[-1].x + 3200, ca[-1].y + 300), (0, 4, 2, 0)))
        ca.append(CloudArea((ca[-1].x + 2500, ca[-1].y - 350), (ca[-1].x + 4550, ca[-1].y + 350), (2, 5, 2, 0)))
        ca.append(CloudArea((ca[-1].x + 2050, ca[-1].y + 300), (ca[-1].x + 2950, ca[-1].y + 800), (0, 2, 2, 0)))
        ca.append(CloudArea((ca[-1].x + 900, ca[-1].y + 300), (ca[-1].x + 2700, ca[-1].y + 1100), (0, 2, 2, 2)))
        ca.append(CloudArea((ca[-1].x + 1800, ca[-1].y - 300), (ca[-1].x + 2500, ca[-1].y + 1000), (0, 0, 2, 2)))
        ca.append(CloudArea((ca[-1].x + 700, ca[-1].y - 400), (ca[-1].x + 1250, ca[-1].y + 700), (0, 0, 1, 2)))
        ca.append(CloudArea((ca[-1].x + 650, ca[-1].y - 100), (ca[-1].x + 1450, ca[-1].y + 300), (0, 0, 2, 1)))


        #Escena 2 (Playa = beach)
        pl.append(Platform((pl[-1].x + 300, pl[-1].y - 225), "platform_2_beach"))
        
        pl.append(Platform((pl[-1].x + 187, pl[-1].y - 50), "platform_3_beach"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y - 100), "platform_2_beach"))
        pl.append(Platform((pl[-1].x + 337, pl[-1].y - 0), "platform_3_beach"))
        pl.append(Platform((pl[-1].x + 299, pl[-1].y - 100), "platform_3_beach"))
        #Escena 3 (Playa)
        pl.append(Platform((pl[-1].x + 262, pl[-1].y - 100), "platform_2_beach"))
        pl.append(Platform((pl[-1].x + 137, pl[-1].y + 100), "platform_2_beach"))
        #pl.append(Platform((pl[-1].x + 324, pl[-1].y + 100), "platform_3_beach"))
        pl.append(Platform((pl[-1].x + 274, pl[-1].y - 100), "platform_1_beach"))
        pl.append(Platform((pl[-1].x + 282, pl[-1].y - 50), "platform_2_beach"))
        pl.append(Platform((pl[-1].x + 237, pl[-1].y - 50), "platform_3_beach"))
        #Escena 4 (Campo = grass)
        pl.append(Platform((pl[-1].x + 362, pl[-1].y - 50), "platform_2_grass"))
        pl.append(Platform((pl[-1].x + 300, pl[-1].y - 50), "platform_1_grass"))
        pl.append(Platform((pl[-1].x + 263, pl[-1].y - 50), "platform_2_grass"))
        pl.append(Platform((pl[-1].x + 300, pl[-1].y - 50), "platform_1_grass"))
        #Escena 5 (Campo)
        pl.append(Platform((pl[-1].x + 250, pl[-1].y - 100), "platform_3_grass"))
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
        pl.append(Platform((pl[-1].x + 364, pl[-1].y - 0), "platform_3_forest"))
        #Escena 7 (Bosque)
        pl.append(Platform((pl[-1].x + 224, pl[-1].y + 50), "platform_1_forest"))
        pl.append(Platform((pl[-1].x + 237, pl[-1].y + 50), "platform_2_forest"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y + 100), "platform_1_forest"))
        pl.append(Platform((pl[-1].x + 149, pl[-1].y + 50), "platform_1_forest"))
        #Platafoma que sube y baja
        pl.append(FloatPlatformVertical((pl[-1].x + 237, pl[-1].y - 250), 150, "platform_2_forest"))
        pl.append(Platform((pl[-1].x + 137, pl[-1].y - 150), "platform_3_forest"))
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
        pl.append(Platform((pl[-1].x + 162, pl[-1].y - 150), "platform_3_stone"))
        pl.append(Platform((pl[-1].x + 349, pl[-1].y - 0), "platform_3_stone"))
        #Escena 11 (Montaña)
        pl.append(FloatPlatformVertical((pl[-1].x + 312, pl[-1].y - 150), 300, "platform_2_stone"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y + 150), "platform_1_stone"))
        pl.append(FloatPlatformVerticalInverted((pl[-1].x + 262, pl[-1].y + 150), -300, "platform_2_stone"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y - 150), "platform_1_stone"))
        pl.append(FloatPlatformVertical((pl[-1].x + 262, pl[-1].y - 150), 300, "platform_2_stone"))
        # Escena 12 (Nieve = snow)
        pl.append(FloatPlatformHorizontalInverted((pl[-1].x + 537, pl[-1].y + 250), -250, "platform_3_snow"))
        pl.append(Platform((pl[-1].x + 302, pl[-1].y + 200), "platform_2_snow"))
        pl.append(Platform((pl[-1].x + 387, pl[-1].y + 150), "platform_3_snow"))
        # Escena 13 (Nieve)
        pl.append(FloatPlatformHorizontal((pl[-1].x + 300, pl[-1].y + 0), 374, "platform_3_snow"))
        pl.append(Platform((pl[-1].x + 637, pl[-1].y + 0), "platform_2_snow"))
        pl.append(FloatPlatformHorizontal((pl[-1].x + 262, pl[-1].y + 0), 374, "platform_1_snow"))
        # Escena 14 (Nieve)
        pl.append(Platform((pl[-1].x + 549, pl[-1].y - 150), "platform_1_snow"))
        pl.append(Platform((pl[-1].x + 262, pl[-1].y - 150), "platform_2_snow"))
        pl.append(Platform((pl[-1].x + 225, pl[-1].y - 150), "platform_2_snow"))
        pl.append(Platform((pl[-1].x + 187, pl[-1].y - 150), "platform_1_snow"))
        pl.append(Platform((pl[-1].x + 187, pl[-1].y - 150), "platform_2_snow"))
        pl.append(Platform((pl[-1].x + 225, pl[-1].y - 150), "platform_2_snow"))
        # Escena 15 (Final)
        #pl.append(FloatPlatformHorizontal((pl[-1].x + 313, pl[-1].y + 0), 225, "platform_3"))
        #pl.append(FloatPlatformHorizontal((pl[-1].x + 224, pl[-1].y + 0), 225, "platform_3"))
        self.cloud = Cloud((pl[-1].x + 375, pl[-1].y + 200))

        pl.append(self.cloud)
        self.platforms.add(pl)

        self.clouds.add(ca)
        for area in ca:
            self.clouds.add(area.generate_clouds())

        self.end = False
        self.end_time = 0

        self.origen_point_x = 250
        self.origen_point_y = 400
        self.die = False

        # Player
        self.player = Player("keyboard", int(WIDTH / 2), int(HEIGHT / 2) -50)

    def load(self, data):
        pass

    def play_music(self):
        for track in TRACK_LIST:
            if self.cloud.x > track[0]:
                correct_track = track[1]
                break
        if correct_track != self.current_track:
            if correct_track == "None":
                pygame.mixer.music.stop()
            load_music("assets/music/{}".format(correct_track))
            self.current_track = correct_track
            pygame.mixer.music.play(-1)



    def on_event(self, time, event):
        keys = pygame.key.get_pressed()

        # players controls
        self.player.action_keyboard(keys)


    def on_update(self, time):
        self.play_music()
        if sprite.collide_rect(self.cloud, self.player):
            self.end = True
        if self.end:
            if self.end_time < FIX_TIME:
                self.platforms.update((0, -3))
                self.clouds.update((0, -3))
            if self.end_time < FLY_TIME:
                self.player.on_air = False
                self.platforms.update((-3, 0))
                self.clouds.update((-3, 0))
                self.cloud.update((3, 0))
                self.player.update((-3, 0), self.platforms)
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
                self.clouds.update((0, -3))
                return
        displacement = self.player.get_displacement(time, self.platforms)
        self.player.update(displacement, self.platforms)
        self.platforms.update(displacement)
        self.clouds.update(displacement)
        if self.player.velocity < FALL_VELOCITY_OVER and self.platforms.sprites()[0].y < self.origen_point_y:
            for platform in self.platforms:
                platform.restart()
                self.player.dead = True
                self.player.state = "idle"
                self.player.current_frame = 0
                self.player.current_sprite = 0
                self.end_time = 0
            for cloud in self.clouds:
                cloud.restart()
            for area in self.ca:
                area.restart()


    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 200))

        screen.blit(self.background, self.background.get_rect())

        
        screen.blit(self.player.image, self.player.rect)

        # caca = pygame.Surface((self.player.collision_rect_left.width, self.player.collision_rect_left.height))
        # caca.fill((255,0,0))
        # screen.blit(caca, self.player.collision_rect_left)

        # caca = pygame.Surface((self.player.collision_rect_right.width, self.player.collision_rect_right.height))
        # caca.fill((255,255,0))
        # screen.blit(caca, self.player.collision_rect_right) 

        # caca = pygame.Surface((self.player.collision_rect_down.width, self.player.collision_rect_down.height))
        # caca.fill((255,0,255))
        # screen.blit(caca, self.player.collision_rect_down)

        # caca = pygame.Surface((self.player.collision_rect_top.width, self.player.collision_rect_top.height))
        # caca.fill((0,255,255))
        # screen.blit(caca, self.player.collision_rect_top)


        for platform in self.platforms:
            screen.blit(platform.image, platform.rect)

        for cloud in self.clouds:
            screen.blit(cloud.image, cloud.rect)




    def finish(self, data):
        pass
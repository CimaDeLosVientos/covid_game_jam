from pygame import sprite, transform, Rect
from pygame.locals import *
from .helpers import *
from .parameters import *

class Player(sprite.Sprite):
    def __init__(self, device, pos_x, pos_y):
        sprite.Sprite.__init__(self)
        self.device = device
        self.sprites = self.load_sprites()
        self.image = self.sprites["normal"]
        self.x = pos_x         #X inicial
        self.y = pos_y         #Y inicial   
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.keyMap = {}
        self.current_frame = -1

        self.jump_time = 0
        self.on_air = False
        self.state = "idle"

        self.collision_rect_left = Rect((self.rect.left,
                                        self.rect.top,
                                        MARGIN_COLLISION_RECT,
                                        self.rect.height - MARGIN_COLLISION_RECT))
        self.collision_rect_right = Rect((self.rect.right - MARGIN_COLLISION_RECT,
                                        self.rect.top,
                                        MARGIN_COLLISION_RECT,
                                        self.rect.height - MARGIN_COLLISION_RECT))
        self.collision_rect_down = Rect((self.rect.left + MARGIN_COLLISION_RECT,
                                        self.rect.bottom - MARGIN_COLLISION_RECT,
                                        self.rect.width - MARGIN_COLLISION_RECT,
                                        MARGIN_COLLISION_RECT))

        self.setPlayer(device)
        self.restart()

    def restart(self):
        self.state = "idle"
        self.image = self.sprites["normal"]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


    def on_floor(self, platforms):
        for platform in platforms:
            if self.collision_rect_down.colliderect(platform.rect):
                self.on_air = False
                self.jump_time = 0  
                return True
        self.on_air = True


    def in_touch_on_right(self, platforms):
        for platform in platforms:
            if self.collision_rect_right.colliderect(platform.rect):
                return True
        return False


    def in_touch_on_left(self, platforms):
        for platform in platforms:
            if self.collision_rect_left.colliderect(platform.rect):
                return True
        return False


    def setPlayer(self, device):
        return
        if device == "keyboard":
            self.keyMap["left"] = K_a
            self.keyMap["right"] = K_d
        #elif device == "pad":
        #    self.keyMap["up"] = (0,1)
        #    self.keyMap["down"] = (0,-1)
        #    self.keyMap["left"] = (-1,0)
        #    self.keyMap["right"] = (0,1)
        #    self.keyMap["weakAttack"] = 2       #Number of the button (X on Xbox controller)
        #    self.keyMap["strongAttack"] = 3     #Number of the button (Y on Xbox controller)

    def load_sprites(self):
        ficha = {
            "normal" : load_image("assets/images/sprites/player.png"),
        }
        return ficha
        


    def action_keyboard(self, keys):
        if keys[K_a] or keys[K_LEFT]:
            if self.state != "left":
                self.current_frame = 0
                self.state = "left"
        elif keys[K_d] or keys[K_RIGHT]:
            if self.state != "right":
                self.current_frame = FRAME_PER_SPRITE
                self.state = "right"
        else:
            self.state = "idle"
        if keys[K_UP] and not self.on_air:
            self.jump_time = JUMP_DURATION
            self.on_air = True
            


    def getFrame(self):
        return self.sprites["normal"]
        if self.current_frame == -1:
            return self.sprites["normal"]
        if self.state == "idle":
            return self.sprites["front"]

        self.current_frame += 1
        if self.current_frame == FRAME_PER_SPRITE * 2 + 1:
            self.current_frame = 0
        if self.current_frame <= FRAME_PER_SPRITE:
            return self.sprites["left"]
        else:
            return self.sprites["right"]

    def update(self, platforms):
        self.on_floor(platforms)
        self.image = self.getFrame()
        #self.rect = self.image.get_rect()
        #self.rect.center = (self.x, self.y)

    def get_displacement(self, time, platforms):
        # e = 1/2 * a * t² + Vo * t + Eo
        x = 0
        y = 0
        if self.state == "left" and not self.in_touch_on_left(platforms):
            x += time * HORIZONTAL_VELOCITY
        if self.state == "right"  and not self.in_touch_on_right(platforms):
            x -= time * HORIZONTAL_VELOCITY
        if self.jump_time > 0:
            y += JUMP_POWER
            self.jump_time -= 1
        else:
            if self.on_air:
                y -= JUMP_POWER
                self.jump_time -= 1

        #if self.jump_time <= 0:
        #    self.state = "idle"


        #if self.jump_velocity > 0:
        #    y += (0.5 * GRAVITY * time * time) + self.jump_velocity * time
        #    self.jump_velocity += GRAVITY * time
        #else:
        #    self.jump_velocity = 0
        return (x, y)




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

        self.velocity = 0
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
                                        self.rect.width - MARGIN_COLLISION_RECT*2,
                                        MARGIN_COLLISION_RECT))
        self.collision_rect_top = Rect((self.rect.left + MARGIN_COLLISION_RECT,
                                        self.rect.top - MARGIN_COLLISION_RECT,
                                        self.rect.width - MARGIN_COLLISION_RECT*2,
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
                return self.collision_rect_down.bottom - platform.rect.top
        return False


    def in_touch_on_right(self, platforms):
        for platform in platforms:
            if self.collision_rect_right.colliderect(platform.rect):
                return self.collision_rect_right.right - platform.rect.left
        return False


    def in_touch_on_left(self, platforms):
        for platform in platforms:
            if self.collision_rect_left.colliderect(platform.rect):
                return platform.rect.right - self.collision_rect_left.left
        return False


    def in_touch_on_top(self, platforms):
        for platform in platforms:
            if self.collision_rect_top.colliderect(platform.rect):
                return platform.rect.bottom - self.collision_rect_top.top
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
        #elif keys[K_w] or keys[K_UP]:
        #    if self.state != "up":
        #        self.current_frame = FRAME_PER_SPRITE
        #        self.state = "up"
        #elif keys[K_s] or keys[K_DOWN]:
        #    if self.state != "down":
        #        self.current_frame = FRAME_PER_SPRITE
        #        self.state = "down"
        else:
            self.state = "idle"
        if keys[K_UP] and not self.on_air:
            self.on_air = True
            self.velocity = INITIAL_VELOCITY
            


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
        if self.state == "left":
            contact = self.in_touch_on_left(platforms)
            if not contact:
                x += time * HORIZONTAL_VELOCITY
            else: 
                x -= (contact - 1) # Hold contact
        if self.state == "right":
            contact = self.in_touch_on_right(platforms)
            if not contact:
                x -= time * HORIZONTAL_VELOCITY
            else:
                x += (contact - 1) # Hold contact
        if self.velocity > 0:
            y += self.velocity + GRAVITY * 0.5
            self.velocity += GRAVITY
        else:
            contact = self.on_floor(platforms)
            if contact:
                y += (contact - 1)
                self.on_air = False
                self.velocity = 0
            else:
                y += self.velocity + GRAVITY * 0.5
                self.velocity += GRAVITY
                self.on_air = True

        contact = self.in_touch_on_top(platforms)
        if contact:
            y += (contact - 1)
            self.velocity = 0
            self.on_air = True

        return (x, y)

# Free controls
        #x = 0
        #y = 0
        #if self.state == "left":
        #    x += time * HORIZONTAL_VELOCITY
        #if self.state == "right":
        #    x -= time * HORIZONTAL_VELOCITY
        #if self.state == "up":
        #    y += time * HORIZONTAL_VELOCITY
        #if self.state == "down":
        #    y -= time * HORIZONTAL_VELOCITY
        #
        #return (x, y)
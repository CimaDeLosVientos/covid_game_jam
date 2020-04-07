from pygame import sprite, transform, Rect
from pygame.locals import *
from .helpers import *
from .parameters import *

class Player(sprite.Sprite):
    def __init__(self, device, pos_x, pos_y):
        sprite.Sprite.__init__(self)
        self.device = device
        self.sprites = self.load_sprites()
        self.image = self.sprites["go_right"][0]
        self.x = pos_x         #X inicial
        self.y = pos_y         #Y inicial   
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.keyMap = {}
        self.current_frame = 0
        self.current_sprite = 0
        self.dead = False
        self.orientation = "right"

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

        self.restart()

    def restart(self):
        self.state = "idle"
        self.image = self.sprites["go_right"][0]
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


    def load_sprites(self):
        width = 80
        height = 100
        sheet = {}
        sprite_sheet_dead_right = load_image("assets/images/sprites/floppy_dead_right.png")
        sprite_sheet_go_right = load_image("assets/images/sprites/floppy_go_right.png")
        sprite_sheet_jump_right = load_image("assets/images/sprites/floppy_jump_right.png")
        sprite_sheet_dead_left = load_image("assets/images/sprites/floppy_dead_left.png")
        sprite_sheet_go_left = load_image("assets/images/sprites/floppy_go_left.png")
        sprite_sheet_jump_left = load_image("assets/images/sprites/floppy_jump_left.png")
        sheet["dead_right"] = []
        sheet["go_right"] = []
        sheet["jump_right"] = []
        sheet["dead_left"] = []
        sheet["go_left"] = []
        sheet["jump_left"] = []
        for i in range(4):
            sheet["dead_right"].append(sprite_sheet_dead_right.subsurface((i*width, 0*height, width, height)))
            sheet["go_right"].append(sprite_sheet_go_right.subsurface((i*width, 0*height, width, height)))
            sheet["dead_left"].append(sprite_sheet_dead_left.subsurface((i*width, 0*height, width, height)))
            sheet["go_left"].append(sprite_sheet_go_left.subsurface((i*width, 0*height, width, height)))
        for i in range(9):
            sheet["jump_right"].append(sprite_sheet_jump_right.subsurface((i*width, 0*height, width, height)))
            sheet["jump_left"].append(sprite_sheet_jump_left.subsurface((i*width, 0*height, width, height)))
        return sheet
        


    def action_keyboard(self, keys):
        if self.dead:
            return
        if keys[K_a] or keys[K_LEFT]:
            if self.state != "left":
                self.state = "left"
                self.orientation = "left"
                if not self.on_air:
                    self.current_frame = 0
                    self.current_sprite = 0
        elif keys[K_d] or keys[K_RIGHT]:
            if self.state != "right":
                self.state = "right"
                self.orientation = "right"
                if not self.on_air:
                    self.current_frame = 0
                    self.current_sprite = 0
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
        if (keys[K_UP] or keys[K_SPACE]) and not self.on_air:
            self.on_air = True
            self.velocity = INITIAL_VELOCITY


    def getFrame(self):
        frame = None
        if self.dead and not self.on_air:
            frame_dead = FRAME_PER_SPRITE / 3
            if self.current_frame <= frame_dead or frame_dead * 14 < self.current_frame:
                self.current_sprite = 0
            elif self.current_frame <= frame_dead * 2 or frame_dead * 12 < self.current_frame:
                self.current_sprite = 1
            elif self.current_frame <= frame_dead * 3 or frame_dead * 10 < self.current_frame:
                self.current_sprite = 2
            elif self.current_frame <= frame_dead * 4 or frame_dead * 8 < self.current_frame:
                self.current_sprite = 3
            if self.current_frame == frame_dead * 16:
                self.dead = False
            if self.orientation == "right":
                frame = self.sprites["dead_right"][self.current_sprite]
            else:
                frame = self.sprites["dead_left"][self.current_sprite]
            self.current_frame += 1
            return frame

        if self.on_air:
            if self.orientation == "right":
                frame = self.sprites["jump_right"][self.current_sprite % 9]
            else:
                frame = self.sprites["jump_left"][self.current_sprite % 9]
        else:
            if self.orientation == "right":
                frame = self.sprites["go_right"][self.current_sprite % 4]
            else:
                frame = self.sprites["go_left"][self.current_sprite % 4]

        self.current_frame += 1
        if self.current_frame == FRAME_PER_SPRITE:
            self.current_sprite += 1
            self.current_frame = 0

        return frame

    def update(self, platforms):
        self.on_floor(platforms)
        self.image = self.getFrame()


    def get_displacement(self, time, platforms):
        # e = 1/2 * a * t² + Vo * t + Eo; t = 1
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
                if self.on_air:
                    self.on_air = False
                    self.velocity = 0
                    self.current_frame = 0
                    self.current_sprite = 0
            else:
                y += self.velocity + GRAVITY * 0.5
                self.velocity += GRAVITY
                self.on_air = True

        contact = self.in_touch_on_top(platforms)
        if contact:
            y -= (contact - 1)
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
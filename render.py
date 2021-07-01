"""
* Classes:
- Texture
- Sprites?

- Triangle?
- Model

- Shader (how???)
"""

import pygame
from PIL import Image

def rgb(string: str) -> tuple[int, int, int]:
    return (int(string[0:2], 16), int(string[2:4], 16), int(string[4:6], 16))

def string_number(color: tuple[int, int, int]) -> str:
    return hex(color[0])[2:].zfill(2) + hex(color[1])[2:].zfill(2) + hex(color[2])[2:].zfill(2)

def vector2_subtract(a: list[int], b: list[int]) -> list[int]:
    return [a[0] - b[0],
            a[1] - b[1]]

def vector2_add(a: list[int], b: list[int]) -> list[int]:
    return [a[0] + b[0],
            a[1] + b[1]]

def anchor_to_vector2(anchor: str, width: int, height: int) -> list[int]:
    if anchor == "top left":       return [0       , height   ]
    elif anchor == "top right":    return [width   , height   ]
    elif anchor == "bottom left":  return [0       , 0        ]
    elif anchor == "bottom right": return [width   , 0        ]
    elif anchor == "top":          return [width//2, height   ]
    elif anchor == "bottom":       return [width//2, 0        ]
    elif anchor == "left":         return [0       , height//2]
    elif anchor == "right":        return [width   , height//2]
    elif anchor == "center":       return [width//2, height//2]

def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

background = rgb("ffffff")
base_anchors = ["top left", "top right", "bottom left", "bottom right"]
font_file_name = "assets/fonts/JetBrainsMono-Medium.ttf"

class Button:
    def on_push(self):
        pass

    def on_hover(self):
        pass

    def on_lift(self):
        pass

    def __init__(self, text: str, text_color: tuple[int, int, int], text_alignment: str, text_size: int, on_push = None, on_hover = None, on_lift = None):
        self.text = text
        self.text_color = text_color
        self.text_alignment = text_alignment
        self.text_size = text_size

        self.on = False
        if on_push != None:
            self.on_push = on_push
        if on_hover != None:
            self.on_hover = on_hover
        if on_lift != None:
            self.on_lift = on_lift

    def check(self, mouse, click, x: int, y: int, w: int, h: int):
        if (mouse[0] > x & mouse[0] < x + w) & (mouse[1] > y & mouse[1] < y + h): # self.on_hover()
            # mouse is on top of button/texture
            self.on_hover()
            self.on = True

            if click[0]: # self.on_push()
                self.on_push()

        else: # self.on_lift()
            if self.on == True: # last frame was on, but not anymore
                self.on_lift()
                self.on = False

    def draw(self, screen, x: int, y: int, w: int, h: int):
        font = pygame.font.Font(font_file_name, self.text_size)
        text_surf, text_rect = text_objects(self.text, font, self.text_color)
        text_rect.center = (x + w // 2, y + h // 2)
        screen.blit(text_surf, text_rect)

class Texture:
    def load(self, file_name: str):
        """
        Load the texture from a file
        """

        with Image.open(file_name) as image:
            self.realw = image.width
            self.realh = image.height

            self.cache(file_name)

    def cache(self, file_name: str):
        """
        Create a scaled version of the texture and store it
        """

        self.image = Image.open(file_name).resize((self.w, self.h))

    def generate_anchor_presets(self, width: int, height: int):
        x, y, w, h = self.x, self.y, self.w, self.h

        first = [[x, y + h], [x + w, y + h], [x, y], [x + w, y]]
        result = []

        for i, anchor in enumerate(first): result.append(vector2_subtract(anchor_to_vector2(self.anchors[i], width, height), anchor))

        self.anchor_presets = result

    def __init__(self, kind: str, x: int, y: int, w: int, h: int, z: int, file_name: str, anchors: list[str] = ["center", "center", "center", "center"], button: Button = None):
        """
        kind: "sprite" or "texture"
        x, y: position of the bottom left corner of the texture in the screen in pixels
        w, h: size of the texture when drawn to the screen in pixels
        z: used for rendering order
        file_name: name of the file to import the image from
        anchors(optional): [top_left top_right bottom_left bottom_right] individual anchor can be top bottom right left or center (or combination of bottom/top and left/right)
        button(optional): an optional button that can be appended to the texture to function as a button to press
        """
        
        self.kind = kind
        self.x = x; self.y = y
        self.w = w; self.h = h
        self.z = z

        if kind == "sprite":
            self.sw = w
            self.sh = h

        self.anchor_presets = [[], [], [], []]
        self.presets_generated = False
        self.anchors = anchors

        self.button = button

        self.file_name = file_name
        self.load(file_name) # import & cache

sprites : list[Texture] = []
canvas  : list[Texture] = []

def resize(screen):
    width, height = screen.get_width(), screen.get_height()

    for texture in canvas:
        if texture.presets_generated == False:
            texture.generate_anchor_presets(width, height)
            texture.presets_generated = True

        texture.x, texture.y = vector2_subtract(anchor_to_vector2(texture.anchors[2], width, height), texture.anchor_presets[2])
        texture.w = vector2_subtract(anchor_to_vector2(texture.anchors[1], width, height), texture.anchor_presets[1])[0] - texture.x
        texture.h = vector2_subtract(anchor_to_vector2(texture.anchors[0], width, height), texture.anchor_presets[0])[1] - texture.y

        texture.cache(texture.file_name)

    unit = 0
    if width > height: # horizontal
        unit = width // 10
    else: # vertical
        unit = height // 10

    for sprite in sprites:
        sprite.w = sprite.sw * unit
        sprite.h = sprite.sh * unit

        sprite.cache(sprite.file_name)

def update(screen) -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: return False

        elif event.type == pygame.VIDEORESIZE or event.type == pygame.VIDEOEXPOSE:
            size = screen.get_size()
            pygame.display.set_mode(size, pygame.RESIZABLE)
            resize(screen)
    
    return True

def button_check(screen, mouse, click, texture: Texture, unit = 1, half_width=0, half_height=0):
    if texture.button == None: return # makes sure texture has button

    texture.button.check(mouse, click, half_width + texture.x * unit, half_height + texture.y * unit, texture.w, texture.h)
    texture.button.draw(screen, half_width + texture.x * unit, half_height + texture.y * unit, texture.w, texture.h)
        
def draw(screen): # TODO make functions in the classes to handle stuff in here easier
    screen.fill(background)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for texture in canvas:
        surface = pygame.image.fromstring(texture.image.tobytes(), texture.image.size, texture.image.mode).convert()

        screen.blit(surface, (texture.x, screen.get_height() - texture.y - texture.h))

        button_check(screen, mouse, click, texture)

    unit = 0
    if screen.get_width() > screen.get_height(): # horizontal
        unit = screen.get_width() // 10
    else: # vertical
        unit = screen.get_height() // 10
        
    for sprite in sprites:
        # draw sprite
        surface = pygame.image.fromstring(sprite.image.tobytes(), sprite.image.size, sprite.image.mode).convert()

        screen.blit(surface, (
                        screen.get_width() // 2 + sprite.x * unit - sprite.w // 2,
                        screen.get_height() // 2 - sprite.y * unit - sprite.h // 2
                    ))

        button_check(screen, mouse, click, sprite, unit, screen.get_width() // 2 - sprite.w // 2, screen.get_height() // 2 - sprite.h // 2)

    pygame.display.flip()

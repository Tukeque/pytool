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

background = rgb("ffffff")

class Texture:
    """
    Class that represents a 2D texture
    """

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


    def __init__(self, x: int, y: int, w: int, h: int, file_name: str):
        """
        x, y: position of the bottom left corner of the texture in the screen in pixels
        w, h: size of the texture when drawn to the screen in pixels
        file_name: name of the file to import the image from
        """

        self.x = x; self.y = y
        self.w = w; self.h = h

        self.load(file_name) # import & cache

textures: list[Texture] = []

def update() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: return False
    
    return True

def draw(screen):
    screen.fill(background)

    for texture in textures:
        surface = pygame.image.fromstring(texture.image.tobytes(), texture.image.size, texture.image.mode).convert()

        screen.blit(surface, (texture.x, screen.get_height() - texture.y - texture.h))

    pygame.display.flip()

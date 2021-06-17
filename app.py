from typing import final
from _thread import start_new_thread
import pygame, render

class App:
    name = ""
    font_name = "JetBrainsMono-Medium.ttf"

    def start(self):
        """
        Called before the first update
        """
        pass

    def update(self):
        """
        Called before every frame
        """
        pass

    def __init__(self, name: str):
        self.name = name

    #//@final
    #//def update_loop(self):
    #//    while self.run:
    #//        self.update()

    @final
    def render_loop(self):
        while self.run:
            self.clock.tick(self.ideal_fps)
            self.fps = self.clock.get_fps()

            self.update() #//
            render.draw(self.screen)

    @final
    def alive_loop(self):
        while self.run:
            self.run = render.update()

    @final
    def main(self):
        """
        Called to start running the application
        """

        #* pygame
        pygame.init()
        info   = pygame.display.Info()
        width  = (info.current_w - 10) // 2
        height = (info.current_h - 50) // 2
        self.screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)
        pygame.display.set_caption(self.name)

        #* self variables
        self.font  = pygame.font.Font(self.font_name, 18)
        self.clock = pygame.time.Clock()
        self.run   = True
        self.fps   = 0
        self.t     = 0
        self.ideal_fps  = 30
        self.fullscreen = False

        #* start
        self.start()

        start_new_thread(self.render_loop)
        self.alive_loop()

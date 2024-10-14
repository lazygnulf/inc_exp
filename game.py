import sys, time
import pygame as pg
from pygame.locals import *
import constants as c
from debug import debug

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(c.DISPLAY_SIZE)
        pg.display.set_caption(c.WINDOW_TITLE)
        self.clock = pg.time.Clock()
        self.dt = 0.0

         
    def run(self):
        prev_time = time.time()
        
        while True:
            # tick clock and compute delta time
            self.clock.tick(c.FPS)
            self.dt = time.time() - prev_time
            prev_time = time.time()

            # handle events
            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.quit()


            # update
            # todo update game objects

            # render state
            self.screen.fill(c.BG_COLOR)
            debug(f"Delta t: {self.dt}")
            # todo update game objects
            pg.display.update()

    def quit(self):
        pg.quit()
        sys.exit()


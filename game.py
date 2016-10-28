import pygame
from player import Player
from asteroid import Asteroid
from menu import Menu

class Game(object):
    def __init__(self):
        self.player = Player()
        self.asteroid = Asteroid()
        self.menu = Menu()

    def update(self):
        if self.menu != None:
            if self.menu.update(pygame.key.get_pressed()) == True:
                self.menu = None
            else:
                return

        self.player.update()
        self.asteroid.update()
        if self.asteroid.check_collision(self.player)==True:
            self.player.destroy()
            self.menu = Menu()

    def draw(self, screen):
        if self.menu is not None:
            self.menu.draw(screen)
            return

        screen.fill([0, 0, 0])
        self.player.draw(screen)
        self.asteroid.draw(screen)
        pygame.display.update()

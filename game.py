import pygame
from player import Player
from asteroid import Asteroid
from menu import Menu

class Game(object):
    def __init__(self):
        self.player = Player()
        self.asteroid = Asteroid()
        self.menu = Menu()
        self.score = 0
        self.TIMER_START = 60
        self.timer = self.TIMER_START
        self.start_ticks = pygame.time.get_ticks()
        self.cur_ticks = self.start_ticks
        self.previous_score = 0
        self.high_score = 0

    def reset(self):
        self.timer = self.TIMER_START
        self.menu = Menu()
        self.asteroid.reset()
        self.player.destroy()
        self.previous_score = self.score
        if self.previous_score > self.high_score:
            self.high_score = self.previous_score
        self.score = 0

    def update(self):
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.reset()

        ticks = pygame.time.get_ticks()
        if ticks - self.start_ticks > 1000:
            self.start_ticks = ticks
            self.timer -= 1
            if self.timer < 0:
                # reset game
                self.reset()
                return True

        if self.menu != None:
            if self.menu.update(pygame.key.get_pressed()) == True:
                self.menu = None
            else:
                return False

        self.player.update()
        self.asteroid.update()

        if self.asteroid.check_collision(self.player)==True:
            if self.asteroid.is_good_type():
                self.score += 1
                self.asteroid.reset()
            else:
                self.reset()

        return False


    def draw(self, screen):
        if self.menu is not None:
            self.menu.draw(screen, self.previous_score, self.high_score)
            return

        screen.fill([0, 0, 0])

        font = pygame.font.Font(None, 36)
        text = font.render("Score: {}".format(str(self.score)), 1, (255, 255, 0))
        textpos = text.get_rect()
        screen.blit(text, textpos)

        text = font.render("Timer: {}".format(str(self.timer)), 1, (255, 255, 0))
        textpos = text.get_rect()
        textpos.left = 200
        screen.blit(text, textpos)

        self.player.draw(screen)
        self.asteroid.draw(screen)
        pygame.display.update()

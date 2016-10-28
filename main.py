import pygame
from pygame.locals import KEYDOWN
from game import Game

Screen_Width = 600
Screen_Height = 480

def update(game):
    # Here we update the game to move elements
    game.update()

def draw(game, screen):
    # Here we draw each component to the screen
    game.draw(screen)

def run():
    quit = False
    game = Game()
    while quit == False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
            if event.type == pygame.QUIT:
                quit = True
        update(game)
        draw(game, screen)
        pygame.time.wait(20)
    pygame.quit()


if __name__=='__main__':
    # global player
    # global asteroid
    global screen

    pygame.init()

    screen = pygame.display.set_mode([Screen_Width, Screen_Height])
    # player = Player()
    # asteroid = Asteroid()

    run()

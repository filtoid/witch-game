import pygame
from player import Player
from asteroid import Asteroid
from pygame.locals import KEYDOWN


Screen_Width = 600
Screen_Height = 480


def update():
    # Here we update the game to move elements
    player.update()
    asteroid.update()
    if asteroid.check_collision(player)==True:
        player.destroy()

def draw(screen):
    # Here we draw each component to the screen
    screen.fill([255, 255, 255])
    player.draw(screen)
    asteroid.draw(screen)
    pygame.display.update()

def run():
    quit = False
    while quit == False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
            if event.type == pygame.QUIT:
                quit = True
        update()
        draw(screen)
        pygame.time.wait(20)
    pygame.quit()


if __name__=='__main__':
    global player
    global asteroid
    global screen

    pygame.init()

    screen = pygame.display.set_mode([Screen_Width, Screen_Height])
    player = Player()
    asteroid = Asteroid()

    run()

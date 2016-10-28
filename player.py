import pygame
from utils import Location

class Player(object):
    def __init__(self):
        self.location = Location(50,440)
        self.size = Location(40, 40)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("images/witch.png").convert()
        self.sprite.image = pygame.transform.scale(self.sprite.image, (50,50))
        self.sprite.rect = self.sprite.image.get_rect()
        self.travelling_left = True

    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            self.location.x -= 5
            self.travelling_left = True

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.location.x += 5
            self.travelling_left = False

        # Make sure we can't leave the screen
        if self.location.x > 560:
            self.location.x = 560

        if self.location.x < 0:
            self.location.x = 0

    def draw(self, screen):
        if self.travelling_left:
            screen.blit(self.sprite.image, self.location.get_loc())
        else:
            img = pygame.transform.flip(self.sprite.image, True, False)
            screen.blit(img, self.location.get_loc())

    def destroy(self):
        # Reset back to our location
        self.location.x = 50
        self.location.y = 440

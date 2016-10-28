import pygame
from utils import Location
import random

class Asteroid(object):
    def __init__(self):
        self.location = Location(100,0)
        self.size = Location(40,40)
        self.sprite = pygame.sprite.Sprite()
        self.get_rand_image()
        self.sprite.rect = self.sprite.image.get_rect()
	
    def get_rand_image(self):
        # picker = random.randint(1,7)
	picker = 5
        if picker == 1:
            self.sprite.image = pygame.image.load("eyeball.png").convert()
            self.sprite.image = pygame.transform.scale(self.sprite.image, (50,50))
        elif picker == 2:
            self.sprite.image = pygame.image.load("bat.png").convert()
            self.sprite.image = pygame.transform.scale(self.sprite.image, (50,50))
        elif picker == 3:
            self.sprite.image = pygame.image.load("small snake.png").convert()
            self.sprite.image = pygame.transform.scale(self.sprite.image, (32,64))
        elif picker == 4:
            self.sprite.image = pygame.image.load("jaws.png").convert()
            self.sprite.image = pygame.transform.scale(self.sprite.image, (50,50))
        elif picker == 5:
            self.sprite.image = pygame.image.load("colorful-1321413.png").convert()
	    self.sprite.image = pygame.transform.scale(self.sprite.image, (51,37))
        elif picker == 6:
            self.sprite.image = pygame.image.load("dog.png").convert()
	    self.sprite.image = pygame.transform.scale(self.sprite.image, (40,50))
        elif picker == 7:
            self.sprite.image = pygame.image.load("small flower.png").convert()
	    self.sprite.image = pygame.transform.scale(self.sprite.image, (54,50))
        #self.sprite.image = pygame.transform.scale(self.sprite.image, (50,50))

    def update(self):
        self.location.y += 5
        if self.location.y > 500:\
            self.reset()

    def reset(self):
        self.get_rand_image()
        self.location.y = 0
        self.location.x = random.randint(0, 560)

    def draw(self, screen):
        screen.blit(self.sprite.image, self.location.get_loc())

    def check_collision(self, obj):
        # Check if the two objects are touching
        diffx = self.location.x - obj.location.x
        diffy = obj.location.y - self.location.y
        if diffx < self.size.x and diffx > (self.size.x * -1):
            if diffy < self.size.y:
                return True
        return False

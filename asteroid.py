import pygame
from utils import Location
import random

class Asteroid(object):
    def __init__(self):
        self.location = Location(100,0)
        self.size = Location(40,40)
        #self.sprite = pygame.sprite.Sprite()
        #self.sprite.rect = self.sprite.image.get_rect()
        self.good_type = None
	self.cur_image = 0
	self.images = []
        for i in range(0,7):
            self.images.append(pygame.sprite.Sprite())
	self.images[0].image = pygame.image.load("images/eyeball.png").convert()
        self.images[0].image = pygame.transform.scale(self.images[0].image, (50,50))
       
       
        self.images[1].image = pygame.image.load("images/bat.png").convert()
        self.images[1].image = pygame.transform.scale(self.images[1].image, (50,50))

        self.images[2].image = pygame.image.load("images/small_snake.png").convert()
        self.images[2].image = pygame.transform.scale(self.images[2].image, (32,64))
        
        self.images[3].image = pygame.image.load("images/jaws.png").convert()
        self.images[3].image = pygame.transform.scale(self.images[3].image, (50,50))
 
        self.images[4].image = pygame.image.load("images/colorful-1321413.png").convert()
        self.images[4].image = pygame.transform.scale(self.images[4].image, (51,37))
  
        self.images[5].image = pygame.image.load("images/dog.png").convert()
        self.images[5].image = pygame.transform.scale(self.images[5].image, (40,50))
 
        self.images[6].image = pygame.image.load("images/small_flower.png").convert()
        self.images[6].image = pygame.transform.scale(self.images[6].image, (54,50))
       
        for i in range(0, len(self.images)):
            self.images[i].rect = self.images[i].image.get_rect()
 
        self.get_rand_image()
        

    def get_rand_image(self):
        picker = random.randint(1,7)
        # picker = 5
        self.good_type = True
        if picker == 1:
            self.cur_image = 0
        elif picker == 2:
            self.cur_image = 1    
        elif picker == 3:
            self.cur_image = 2
        elif picker == 4:
            self.cur_image = 3
        elif picker == 5:
           self.cur_image = 4
           self.good_type = False
        elif picker == 6:
           self.cur_image = 5
           self.good_type = False
        elif picker == 7:
          self.cur_images = 6
          self.good_type = False
            

    def update(self):
        self.location.y += 5
        if self.location.y > 500:
            self.reset()

    def reset(self):
        self.get_rand_image()
        self.location.y = 0
        self.location.x = random.randint(0, 560)

    def draw(self, screen):
        screen.blit(self.images[self.cur_image].image, self.location.get_loc())

    def is_good_type(self):
        return self.good_type

    def check_collision(self, obj):
        # Check if the two objects are touching
        diffx = self.location.x - obj.location.x
        diffy = obj.location.y - self.location.y
        if diffx < self.size.x and diffx > (self.size.x * -1):
            if diffy < self.size.y:
                return True
        return False

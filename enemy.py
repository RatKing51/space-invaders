from typing import Any
import pygame
from pygame import *
import random

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, img_path):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.img_path = img_path
        self.image = self.img_path
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.dir = random.randint(0, 1)
        self.kill_ = False
        self.speed = 0.75
        
    
    def draw(self, window):
        window.blit(self.image, self.rect)

    def update(self, other_rect, window):
        
    
        self.rect.move_ip(0, 1)
        

        
        if self.kill_:
            self.kill()
        
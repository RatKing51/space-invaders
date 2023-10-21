from typing import Any
import pygame
from pygame import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, img_path):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.img_path = img_path
        self.image = self.img_path
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.dir = 1
        self.kill_ = False
        
    
    def draw(self, window):
        window.blit(self.image, self.rect)

    def update(self, other_rect):
        
        
        if self.rect.centerx == 368:
           self.dir = 0
           self.rect.move_ip(0, 5)
        if self.rect.centerx == 32:
           self.dir = 1
           self.rect.move_ip(0, 5)

        if self.dir == 0:
            self.rect.move_ip(-1, 0)
        if self.dir == 1:
           self.rect.move_ip(1, 0)
        
        if self.kill_:
            self.kill()
        
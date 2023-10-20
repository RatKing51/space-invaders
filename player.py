import pygame
from pygame import *
import bullet
from bullet import *

class Player(pygame.sprite.Sprite):
     
    def __init__(self, x, y, color, img_path, size1, size2):
        self.x = int(x)
        self.y = int(y)
        self.color = color
        self.img_path = img_path
        self.size1 = size1
        self.size2 = size2
        self.img = pygame.image.load(self.img_path)
        self.img = pygame.transform.scale(self.img, (64, 64))
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.left_pressed = False
        self.right_pressed = False
        self.speed = 2
        self.last_shot = pygame.time.get_ticks()
        self.pew_group = pygame.sprite.Group()
        self.spaced_pressed = False
        
    def draw(self, win):
        win.blit(self.img, (self.rect))

    def update(self):
        if self.left_pressed and not self.right_pressed:
            self.rect.move_ip(-self.speed, 0)
        if self.right_pressed and not self.left_pressed:
            self.rect.move_ip(self.speed, 0)

        if self.rect.x == 0:
            self.rect.x = 0
            self.rect.move_ip(self.speed, 0)
        if self.rect.x == 336:
            self.rect.x = 336
            self.rect.move_ip(-self.speed, 0)

        cooldown = 100

        time_now = pygame.time.get_ticks()
        # shoot
        if self.spaced_pressed and time_now - self.last_shot > cooldown:
            pew = Bullet(self.rect.centerx, self.rect.top)
            self.pew_group.add(pew)
            self.last_shot = time_now

        
        
    
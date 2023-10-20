import pygame
from pygame import *
import enemy
from enemy import *

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (int(x), int(y))
        self.tell_kill = False

    def draw(self, win):
        win.blit(self.image, self.rect)

    def update(self, other_rect):
        self.rect.y -= 7
        collide = pygame.Rect.colliderect(self.rect, other_rect)

        if self.rect.bottom <= 0:
            self.kill()
        elif collide:
            self.tell_kill = True
            self.kill()

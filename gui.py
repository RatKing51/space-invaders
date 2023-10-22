import pygame
from pygame import *

class Button():

    def __init__(self, x, y, color, img_path, size1, size2, text):
        self.x = int(x)
        self.y = int(y)
        self.color = color
        self.img_path = img_path
        self.size1 = int(size1)
        self.size2 = int(size2)
        self.rect = Rect(self.x, self.y, size1, size2)
        self.font = pygame.font.SysFont('Georgia', 20)
        self.text = text
        self.text_ = self.font.render("Play", True, 'white')
        self.pressed = False
        self.hide = False

    def draw(self, window):
        self.button = pygame.draw.rect(window, self.color, self.rect, 0, 5)
        window.blit(self.text_, (self.x + 15, self.y + 20))

    def update(self):

        mousePos = pygame.mouse.get_pos()

        if self.button.collidepoint(mousePos):
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if not self.pressed:
                    self.pressed = True
                    self.hide = True

            else:
                self.pressed = False

class Text():

    def __init__(self, x, y, size, color, text):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.size = size
        self.color = color
        self.font = pygame.font.SysFont('Georgia', self.size)
        self.text = text
        self.message = self.font.render(self.text, True, self.color)

    def draw(self, window):
        window.blit(self.message, (self.x, self.y))

    def update(self, window, text):
        self.text = text
        window.blit(self.message, (self.x, self.y))


        
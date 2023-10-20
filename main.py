import pygame
from pygame import *
import gui
from gui import *
import player
from player import *
import bullet
from bullet import *
import enemy
from enemy import *


pygame.init()

# Game Vars
width = 400
height = 600
pygame.display.set_caption('space invaders')
screen = pygame.display.set_mode((width, height))


button1 = Button(164, 236, 'blue', False, 64, 64, "Play")

user = Player(200, 564, False, 'assets/player.png', 64, 64)

bullet_ = Bullet(400, 600)

enemy_ = Enemy(50, 50, 'assets/enemy.png')

game = False

shoot = False


enemy_group = pygame.sprite.Group()

enemy_group.add(enemy_)

#Images
bg = pygame.image.load('assets/background.png')

#game loop
run = True
while run:
    screen.fill('black')
    screen.blit(bg, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                user.left_pressed = True
            if event.key == K_d:
                user.right_pressed = True
            if event.key == K_SPACE:
                user.spaced_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == K_a:
                user.left_pressed = False
            if event.key == K_d:
                user.right_pressed = False
            if event.key == pygame.K_SPACE:
                user.spaced_pressed = False
    

    # Start Button
    if not button1.hide:
        button1.draw(screen)
    else:
        game = True
    button1.update()

    # main game
    if game:
        if pygame.sprite.groupcollide(enemy_group, user.pew_group, dokilla=True, dokillb=True):
            print("yes")
        user.draw(screen)
        user.update()
        user.pew_group.draw(screen)
        user.pew_group.update(enemy_.rect)
        enemy_.draw(screen)
        enemy_.update(bullet_.rect)
        
    
              



    pygame.display.update()
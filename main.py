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
import random
import time


pygame.init()

# Game Vars
width = 400
height = 600
pygame.display.set_caption('space invaders')
screen = pygame.display.set_mode((width, height))


button1 = Button(164, 236, 'blue', False, 64, 64, "Play")

user = Player(200, 564, False, 'assets/player.png', 64, 64)

bullet_ = Bullet(400, 600)

score_text = Text(0, 0, 20, 'white', "Score")

game = False

shoot = False

clock = pygame.time.Clock()




green_enemy1 = pygame.sprite.Group()
red_enemy1 = pygame.sprite.Group()

green1_x = []
red1_x = []
green1_y = []
red1_y = []

numOfgEnemy = 10
numOfrEnemy = 5





for i in range(numOfgEnemy):
    green1_x.append(random.randrange(32, 332))
    green1_y.append(random.randrange(0, 32))
    enemy_ = Enemy(green1_x[i], green1_y[i], pygame.image.load('assets/enemy.png'))
    green_enemy1.add(enemy_)

for i in range(numOfrEnemy):
    red1_x.append(random.randrange(32, 332))
    red1_y.append(random.randrange(0, 32))
    enemy_ = Enemy(red1_x[i], red1_y[i], pygame.image.load('assets/enemy1.png'))
    red_enemy1.add(enemy_)


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
        if pygame.sprite.groupcollide(green_enemy1, user.pew_group, dokilla=True, dokillb=True):
            enemy_.kill_ = True
        if pygame.sprite.groupcollide(red_enemy1, user.pew_group, dokilla=True, dokillb=True):
            enemy_.kill_ = True
        user.draw(screen)
        user.update()
        user.pew_group.draw(screen)
        user.pew_group.update(enemy_.rect)
        green_enemy1.draw(screen)
        green_enemy1.update(bullet_.rect, screen)
        red_enemy1.draw(screen)
        red_enemy1.update(bullet_.rect, screen)
        score_text.draw(screen)
        
    clock.tick(50)
    
              



    pygame.display.update()

if __name__ == "__main__":
    run = True
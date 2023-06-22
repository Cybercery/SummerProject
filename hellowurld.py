import pygame
import math

pygame.init()

screen_width = 1000
screen_height = 800
bg = pygame.image.load('assets/bg1.png')
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MyGame")
mc1 = pygame.image.load('assets/fullHealth.png')
mc_X = 470
mc_Y = 680
mc_changeX = 0
mc_changeY = 0

enemy1 = pygame.image.load('assets/monster1.png')
enemy_X = 470
enemy_Y = 50
enemy_changeX = 0
enemy_changeY = 0

font = pygame.font.Font('assets/freesansbold.ttf', 32)
text_X = 10
text_Y = 10

def player(x, y):
    screen.blit(mc1, (x, y))
def enemy(x, y):
    screen.blit(enemy1, (x, y))
def collision(mc_x, mc_y, enemy_x, enemy_y):
    dist = math.sqrt((math.pow(enemy_x - mc_x, 2)) + (math.pow(enemy_y - mc_y, 2)))
    if dist < 68:
        return True
    else:
        return False
def showtext(x, y):
    score = font.render("SCORE: ", True, (0, 0, 0))
    screen.blit(score, (x, y))


enemy1_status = True
run = True
while run:
    screen.fill((154, 205, 224))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mc_changeX = -4
            if event.key == pygame.K_RIGHT:
                mc_changeX = 4
            if event.key == pygame.K_UP:
                mc_changeY = -4
            if event.key == pygame.K_DOWN:
                mc_changeY = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mc_changeX = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                mc_changeY = 0
    mc_X += mc_changeX
    if mc_X <= 0:
        mc_X = 0
    elif mc_X >= 936:
        mc_X = 936
    elif mc_Y <= 0:
        mc_Y = 0
    elif mc_Y >= 736:
        mc_Y = 736
    mc_Y += mc_changeY
    enemy(enemy_X, enemy_Y)
    player(mc_X, mc_Y)
    coll = collision(mc_X, mc_Y, enemy_X, enemy_Y)
    if coll:
        if enemy1_status:
            print("HIT")
            enemy1_status = False
        else:
            print("Already HIT")
    showtext(text_X, text_Y)
    pygame.display.update()
pygame.quit()

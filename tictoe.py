import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 565))
pygame.display.set_caption("Enemy Battle: TicTacToe")
mc1 = pygame.image.load('fullHealth.png')
enemy1 = pygame.image.load('monster1.png')
font = pygame.font.Font('freesansbold.ttf', 38)
def player(x, y):
    screen.blit(mc1, (x, y))
def enemy(x, y):
    screen.blit(enemy1, (x, y))
def showtext1(x, y):
    score = font.render(": X", True, (0, 0, 0))
    screen.blit(score, (x, y))
def showtext2(x, y):
    score = font.render(": O", True, (0, 0, 0))
    screen.blit(score, (x, y))


run = True
while run:
    screen.fill((248, 240, 227))
    pygame.draw.line(screen, "Black", (166, 15), (166, 485), 2)
    pygame.draw.line(screen, "Black", (332, 15), (332, 485), 2)
    pygame.draw.line(screen, "Black", (15, 166), (485, 166), 2)
    pygame.draw.line(screen, "Black", (15, 332), (485, 332), 2)
    player(90, 495)
    showtext1(160, 510)
    enemy(290, 495)
    showtext2(360, 510)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

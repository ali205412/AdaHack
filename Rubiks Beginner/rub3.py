import pygame
from pygame.locals import *
import time

blue = 114, 187, 255
white = 230, 230, 255
yellow = 175, 232, 65
red = 178, 71, 61
orange = 255, 129, 66
green = 0, 203, 40

colors = [red, yellow, blue, white, green, orange]


# works
def initialize(screen, x, y):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 80, y, 40, 40), 3)

    pygame.draw.rect(screen, (255, 255, 255), (x, y + 40, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y + 40, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 80, y + 40, 40, 40), 3)

    pygame.draw.rect(screen, (255, 255, 255), (x, y + 80, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y + 80, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 80, y + 80, 40, 40), 3)


def color_side(color, x, y, z, screen):
    if z == 0 or z == 1 or z == 5:
        pygame.draw.rect(screen, colors[color[0]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[0]], (x + 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[0]], (x + 80, y, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[0]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[0]], (x + 40, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[0]], (x + 80, y + 40, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[0]], (x, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[0]], (x + 40, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[0]], (x + 80, y + 80, 34, 34), 0)
    elif z == 2:
        pygame.draw.rect(screen, colors[color[1]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x + 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x + 80, y, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[1]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x + 40, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x + 80, y + 40, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[1]], (x, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x + 40, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x + 80, y + 80, 34, 34), 0)
    elif z == 3:
        pygame.draw.rect(screen, colors[color[2]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 80, y, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[2]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 40, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 80, y + 40, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[2]], (x, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 40, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 80, y + 80, 34, 34), 0)
    elif z == 4:
        pygame.draw.rect(screen, colors[color[3]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[3]], (x + 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[3]], (x + 80, y, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[3]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[3]], (x + 40, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[3]], (x + 80, y + 40, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[3]], (x, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[3]], (x + 40, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[3]], (x + 80, y + 80, 34, 34), 0)


def color_update(matrix, screen):
    color_side(matrix[0], 163, 203, 0, screen)
    color_side(matrix[1], 163, 323, 1, screen)
    color_side(matrix[2], 283, 203, 2, screen)
    color_side(matrix[3], 163, 83, 3, screen)
    color_side(matrix[4], 43, 203, 4, screen)
    color_side(matrix[5], 163, 443, 5, screen)


scr = pygame.display.set_mode((440, 580))
scr.fill((155, 155, 155))


def paint(matrix):
    global scr
    initialize(scr, 160, 80)
    initialize(scr, 160, 200)
    initialize(scr, 160, 320)
    initialize(scr, 160, 440)
    initialize(scr, 280, 200)
    initialize(scr, 40, 200)
    color_update(matrix, scr)
    pygame.display.update()


running = True
while running:
    paint([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5, 5]])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

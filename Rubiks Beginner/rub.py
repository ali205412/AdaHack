import pygame
from pygame.locals import *

blue = 114, 187, 255
white = 230, 230, 255
yellow = 175, 232, 65
red = 178, 71, 61
orange = 255, 129, 66
green = 0, 203, 40

colors = [red, yellow, blue, white, green, orange]


def initialize(screen, x, y):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x, y + 40, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y + 40, 40, 40), 3)


def color_side(color, x, y, z, screen):
    if z == 0 or z == 1 or z == 5:
        pygame.draw.rect(screen, colors[color[0]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x + 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[3]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 40, y + 40, 34, 34), 0)
    elif z == 2:
        pygame.draw.rect(screen, colors[color[1]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[0]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[3]], (x + 40, y + 40, 34, 34), 0)
    elif z == 3:
        pygame.draw.rect(screen, colors[color[2]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[3]], (x + 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[0]], (x + 40, y + 40, 34, 34), 0)
    elif z == 4:
        pygame.draw.rect(screen, colors[color[3]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[0]], (x + 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x + 40, y + 40, 34, 34), 0)


def color_update(matrix, screen):
    color_side(matrix[0], 163, 163, 0, screen)
    color_side(matrix[1], 163, 243, 1, screen)
    color_side(matrix[2], 243, 163, 2, screen)
    color_side(matrix[3], 163, 83, 3, screen)
    color_side(matrix[4], 83, 163, 4, screen)
    color_side(matrix[5], 163, 323, 5, screen)


def paint(matrix):
    screen = pygame.display.set_mode((400, 480))
    screen.fill((155, 155, 155))
    initialize(screen, 160, 160)
    initialize(screen, 160, 240)
    initialize(screen, 240, 160)
    initialize(screen, 160, 80)
    initialize(screen, 80, 160)
    initialize(screen, 160, 320)
    color_update(matrix, screen)
    pygame.display.update()

def initialize(screen, x, y):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 40, 40), 90)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x, y + 40, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y + 40, 40, 40), 3)


while True:
    paint([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]])
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
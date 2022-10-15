import pygame
from pygame.locals import *
import time

scr = pygame.display.set_mode((550, 580))
scr.fill((155, 155, 155))

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


def color_side(color, x, y, screen):
    pygame.draw.rect(screen, color[0], (x, y, 34, 34), 0)
    pygame.draw.rect(screen, color[1], (x + 40, y, 34, 34), 0)
    pygame.draw.rect(screen, color[2], (x + 80, y, 34, 34), 0)

    pygame.draw.rect(screen, color[3], (x, y + 40, 34, 34), 0)
    pygame.draw.rect(screen, color[4], (x + 40, y + 40, 34, 34), 0)
    pygame.draw.rect(screen, color[5], (x + 80, y + 40, 34, 34), 0)

    pygame.draw.rect(screen, color[6], (x, y + 80, 34, 34), 0)
    pygame.draw.rect(screen, color[7], (x + 40, y + 80, 34, 34), 0)
    pygame.draw.rect(screen, color[8], (x + 80, y + 80, 34, 34), 0)


def color_update(matrix, screen):
    color_side(matrix[0], 163, 83, screen)
    color_side(matrix[1], 43, 203, screen)
    color_side(matrix[2], 163, 203, screen)
    color_side(matrix[3], 283, 203, screen)
    color_side(matrix[4], 403, 203, screen)
    color_side(matrix[5], 163, 323, screen)

def paint(matrix):
    global scr
    initialize(scr, 160, 80)
    initialize(scr, 160, 200)
    initialize(scr, 160, 320)
    initialize(scr, 400, 200)
    initialize(scr, 280, 200)
    initialize(scr, 40, 200)
    color_update(matrix, scr)
    pygame.display.update()


colorDict = {
    "r": red,
    "y": yellow,
    "b": blue,
    "w": white,
    "g": green,
    "o": orange
}

pattern = ""
while len(pattern) != 54:
    pattern = input("str: ").lower()

# rywwybyroyoboooobrrgyybrwbggyowrgwybgggwgbwgbbrrwwryoo
config = []
temp = ""
i = 1
for letter in pattern:
    temp += letter
    if i % 9 == 0:
        config.append(temp)
        temp = ""
    i += 1

config_color = []
for item in config:
    temp = []
    for letter in item:
        color = colorDict[letter]
        temp.append(color)
    config_color.append(temp)

running = True
while running:
    paint(config_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

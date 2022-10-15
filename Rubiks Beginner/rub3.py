import pygame

scr = pygame.display.set_mode((540, 580))
scr.fill((155, 155, 155))

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
        pygame.draw.rect(screen, colors[color[1]], (x + 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 80, y, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[3]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[4]], (x + 40, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[5]], (x + 80, y + 40, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[6]], (x, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[7]], (x + 40, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[8]], (x + 80, y + 80, 34, 34), 0)
    elif z == 2:
        pygame.draw.rect(screen, colors[color[0]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x + 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 80, y, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[3]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[4]], (x + 40, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[5]], (x + 80, y + 40, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[6]], (x, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[7]], (x + 40, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[8]], (x + 80, y + 80, 34, 34), 0)
    elif z == 3:
        pygame.draw.rect(screen, colors[color[0]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x + 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 80, y, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[3]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[4]], (x + 40, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[5]], (x + 80, y + 40, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[6]], (x, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[7]], (x + 40, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[8]], (x + 80, y + 80, 34, 34), 0)
    elif z == 4:
        pygame.draw.rect(screen, colors[color[0]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x + 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 80, y, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[3]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[4]], (x + 40, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[5]], (x + 80, y + 40, 34, 34), 0)

        pygame.draw.rect(screen, colors[color[6]], (x, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[7]], (x + 40, y + 80, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[8]], (x + 80, y + 80, 34, 34), 0)


def color_update(matrix, screen):
    color_side(matrix[0], 163, 83, 0, screen)
    color_side(matrix[1], 43, 203, 1, screen)
    color_side(matrix[2], 163, 203, 2, screen)
    color_side(matrix[3], 283, 203, 3, screen)
    color_side(matrix[4], 403, 203, 4, screen)
    color_side(matrix[5], 163, 323, 5, screen)


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
    "r": 0,
    "y": 1,
    "b": 2,
    "w": 3,
    "g": 4,
    "o": 5
}

pattern = ""
while len(pattern) != 54:
    pattern = input("str: ").lower()

# rywwybyroyoboooobrrgyybrwbggyowrgwybgggwgbwgbbrrwwryoo
config = []
pos = ""
i = 1
for letter in pattern:
    pos += letter
    if i % 9 == 0:
        config.append(pos)
        pos = ""
    i += 1

color_config = []
for item in config:
    temp = []
    for letter in item:
        color = colorDict[letter]
        temp.append(color)
    color_config.append(temp)

running = True
while running:
    paint(color_config)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

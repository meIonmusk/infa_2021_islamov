import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
point = 0


def new_ball():
    """
    создает новый шарик случайного радиуса случайного цвета в случайном месте

    :return: none
    """
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    """
    обрабатывает щелчок мыши: распознает словил ли пользователь шарик

    :param event: event
    :return: none
    """
    global point
    if abs(event.pos[0] - x) < r and abs(event.pos[1] - y):
        print('yeah!')
        point += 1


def point_version(point):
    """
    определят необходимый падеж слова очки

    :param point: количество очков
    :return: слово в нужном падеже
    """
    if point % 10 == 1 and point % 100 != 11:
        version = 'очко'
    elif point % 10 in (2, 3, 4) and point % 100 not in (12, 13, 14):
        version = 'очка'
    else:
        version = 'очков'
    return version


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print('вы набрали', point, point_version(point) + '!')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            click(event)
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

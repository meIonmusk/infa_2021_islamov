import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
WIDTH = 1200
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
RASPBERRY = (255, 0, 125)
MAGENTA = (255, 0, 255)
VIOLET = (125, 0, 255)
BLUE = (0, 0, 255)
OCEAN = (0, 125, 255)
CYAN = (0, 255, 255)
TURQUOISE = (0, 255, 125)
GREEN = (0, 255, 0)
SPRING = (125, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 125, 0)
BLACK = (0, 0, 0)
COLORS = [RED, RASPBERRY, MAGENTA, VIOLET, BLUE, OCEAN,
          CYAN, TURQUOISE, GREEN, SPRING, YELLOW, ORANGE]
point = 0
balls_number = 5

pool = []


def new_ball():
    """
    создает новый шарик случайного радиуса, случайной скорости и случайного цвета в случайном месте

    :return: none
    """
    global pool
    x = randint(WIDTH//10, WIDTH//2)
    y = randint(HEIGHT//10, HEIGHT//2)
    r = randint(30, 50)
    v_x = randint(-5, 5)
    v_y = randint(-5, 5)
    color = COLORS[randint(0, 11)]
    pool.append([x, y, r, v_x, v_y, color])


def draw_balls():
    """
    Функция рисует заданное количество шариков
    :return: none
    """
    global pool
    for t in range(balls_number):
        pool[t][0] += pool[t][3]
        pool[t][1] += pool[t][4]
        circle(screen, pool[t][5], (pool[t][0], pool[t][1]), pool[t][2])


def bump_border(ball):
    """
    Функция отталкивает шарик от стен в случае столкновения
    :param ball: шарик, столкновение котрого проверяет функция
    :return: none
    """
    if abs(ball[0] - WIDTH/2) > WIDTH/2-ball[2]:
        ball[3] = -ball[3]
        ball[0] += ball[3]
    if abs(ball[1] - HEIGHT/2) > HEIGHT/2-ball[2]:
        ball[4] = -ball[4]
        ball[1] += ball[4]


def bump_balls():
    """
    Функция отталкивает шарики в случае столкновения
    :return: none
    """
    for p in range(balls_number):
        ball_1 = pool[p]
        for n in range(balls_number):
            if n != p:
                ball_2 = pool[n]
                if ((ball_1[0]-ball_2[0])**2 + (ball_1[1]-ball_2[1])**2
                        <= (ball_1[2]+ball_2[2])**2):
                    ball_1[3], ball_2[3] = ball_2[3], ball_1[3]
                    ball_1[4], ball_2[4] = ball_2[4], ball_1[4]
                    ball_1[0] += ball_1[3]
                    ball_1[1] += ball_1[4]
                    ball_2[0] += ball_2[3]
                    ball_2[1] += ball_2[4]


def click(event_):
    """
    обрабатывает щелчок мыши: распознает словил ли пользователь шарик

    :param event_: event
    :return: none
    """
    global point, pool
    for j in range(balls_number):
        r = pool[j][2]
        if (event_.pos[0] - pool[j][0]) ** 2 + (event_.pos[1] - pool[j][1]) ** 2 <= r ** 2:
            print('yeah!')
            point += 1
            pool.pop(j)
            new_ball()


def point_version(point_):
    """
    определят необходимый падеж слова очки

    :param point_: количество очков
    :return: слово в нужном падеже
    """
    if point_ % 10 == 1 and point_ % 100 != 11:
        version = 'очко'
    elif point_ % 10 in (2, 3, 4) and point_ % 100 not in (12, 13, 14):
        version = 'очка'
    else:
        version = 'очков'
    return version


for i in range(balls_number):
    new_ball()

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
    draw_balls()
    for k in range(balls_number):
        bump_border(pool[k])
    bump_balls()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

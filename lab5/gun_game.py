import math
from random import choice
from random import randint
import pygame


FPS = 35

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.v = 0
        self.dvy = 2

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy -= self.dvy

        if self.x >= WIDTH or self.x <= 0:
            self.vx = -0.5 * self.vx
            self.x += self.vx
        if self.y >= HEIGHT or self.y <= 0:
            self.vy = -0.5 * self.vy
            self.y -= self.vy
        self.v = (self.vx**2 + self.vy**2) ** 0.5
        if self.v < 5:
            self.y = HEIGHT
            self.vy = 0

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x-obj.x)**2 + (self.y-obj.y)**2 <= (self.r+obj.r)**2:
            return True
        return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        new_ball.v = (new_ball.vy**2 + new_ball.vx**2) ** 0.5
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] != 20:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self, x=40, y=450):
        global screen
        a = 7
        pygame.draw.polygon(screen, self.color, [
            (x, y),
            (x + self.f2_power*math.cos(-self.an), y - self.f2_power*math.sin(-self.an)),
            (x + self.f2_power*math.cos(-self.an) - a*math.sin(-self.an),
             y - self.f2_power*math.sin(-self.an) - a*math.cos(-self.an)),
            (x-a*math.sin(-self.an), y-a*math.cos(-self.an))
        ])

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


RANGE_X = 400
RANGE_Y = 200


class Target:
    points = 0

    def __init__(self):
        self.live = 1
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.live = 1
        self.x = randint(RANGE_X+50, WIDTH-100)
        self.y = randint(RANGE_Y+50, HEIGHT-100)
        self.r = randint(2, 50)
        self.color = choice(GAME_COLORS)
        self.vx = randint(-5, 5)
        if self.vx == 0: self.vx = 1
        self.vy = randint(-5, 5)
        if self.vy == 0: self.vy = 1

    def hit(self, point=1):
        """Попадание шарика в цель."""
        Target.points += point
        self.live = 1

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def bump_borders(self):
        if self.x >= WIDTH-50-self.r or self.x <= RANGE_X+self.r:
            self.vx = -self.vx
            self.x += self.vx
        if self.y >= HEIGHT-50-self.r or self.y <= RANGE_Y+self.r:
            self.vy = -self.vy
            self.y += self.vy


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
font_size = 36
f = pygame.font.SysFont('Arial', font_size)

clock = pygame.time.Clock()
gun = Gun(screen)
target_numbers = 4
targets = []
for num in range(target_numbers):
    target = Target()
    targets.append(target)

for targ in targets:
    targ.new_target()

MOVE_TARGET = True
finished = False
while not finished:
    screen.fill(WHITE)
    gun.draw()
    for targ in targets:
        if MOVE_TARGET:
            targ.bump_borders()
            targ.move()
        targ.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    text = f.render('POINTS: ' + str(Target.points), False, BLACK)
    screen.blit(text, (40, 200))

    for b in balls:
        if b.v > 10:
            b.move()
        else:
            b.y = HEIGHT
        for targ in targets:
            if b.hittest(targ) and targ.live:
                targ.live = 0
                targ.hit()
                targ.new_target()
    k = 0
    for b in balls:
        if b.v < 10:
            balls.pop(k)
        k += 1
    gun.power_up()

print(Target.points)
pygame.quit()

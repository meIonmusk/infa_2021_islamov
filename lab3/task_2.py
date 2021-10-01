import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 700))
leaf = pygame.Surface((10, 70))
green = (50, 120, 65)
pi = math.pi

ellipse(leaf, green, (0, 0, 10, 70))
leaf_right = pygame.transform.rotate(leaf, 20).convert_alpha()

arc(screen, green, (435, 200, 200, 300), 2*pi/5, 7*pi/8, 3)
arc(screen, green, (435, 50, 600, 300), 3*pi/5, 8*pi/9, 3)

screen.blit(leaf_right, (530, 90))
for i in range(4):
    screen.blit(leaf_right, (560 + 20*i, 77 - 5*i))

screen.blit(leaf_right, (490, 220))
screen.blit(leaf_right, (520, 200))
screen.blit(leaf_right, (550, 210))

half_tree = pygame.transform.flip(screen, True, False)
half_tree = pygame.transform.scale(half_tree, (1000, 700))
rect(screen, green, (400, 400, 35, 100))
rect(screen, green, (400, 250, 35, 130))
polygon(screen, green, [(420, 240), (400, 236), (417, 151), (437, 155)])
polygon(screen, green, [(425, 145), (410, 142), (435, 17), (450, 20)])
screen.blit(half_tree, (-50, 50))
screen2 = pygame.transform.scale(screen, (800, 700))
screen.fill((255, 180, 130))
screen.blit(screen2, (0, 0))

screen.blit(pygame.transform.scale(screen2, (300, 500)), (100, 150))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

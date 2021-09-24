import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
brown = (125, 20, 0)
circle(screen, yellow, (200, 200), 100)
circle(screen, red, (160, 170), 20)
circle(screen, black, (160, 170), 8)
circle(screen, red, (240, 170), 15)
circle(screen, black, (240, 170), 8)
polygon(screen, brown, [(185, 170), (190, 165), (125, 100), (120, 105)])
polygon(screen, brown, [(215, 165), (212, 158), (290, 120), (293, 128)])
rect(screen, black, (130, 225, 140, 17))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

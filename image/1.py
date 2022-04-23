import pygame
from sys import exit

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (156, 39, 176)
INDIGO = (63, 81, 181)
BLUE = (33, 150, 243)
GREEN = (76, 175, 80)
YELLOW = (255, 235, 59)
ORANGE = (255, 152, 0)
GREY = (158, 158, 158)

display = pygame.display.set_mode( (800, 600) )

FPS = 60
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('����� �������')
            elif event.key == pygame.K_RIGHT:
                print('������ �������')
            elif event.key ==pygame.K_UP:
                print('������� �����')
            elif event.key ==pygame.K_DOWN:
                print('������� ����')

    pygame.display.update()

    clock.tick(FPS) 

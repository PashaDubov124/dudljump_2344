import pygame
import sys


pygame.init()



s_size = 480,700

bg_color = 254,254,254

screen = pygame.display.set_mode(s_size)


while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)
    pygame.display.update()
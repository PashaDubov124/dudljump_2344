import pygame
import sys


pygame.init()

class Main:
    def __init__(self):
        self.s_size = 480, 700
        self.screen = pygame.display.set_mode(self.s_size)
        self.bg_image = pygame.image.load("images/fon_dudljump.png")
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg_image, self.bg_image.get_rect())


main  = Main()







while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main.draw()
    pygame.display.update()
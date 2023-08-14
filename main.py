import pygame
import sys
import random
from platform import Platform


pygame.init()

class Main:
    def __init__(self):
        self.s_size = 480, 700
        self.screen = pygame.display.set_mode(self.s_size)
        self.bg_image = pygame.image.load("images/fon_dudljump.png")
        self.platforms = [Platform(self.s_size[0] / 2 - 45, self.s_size[1] - 30)]
        self.create_platform()
        self.clock = pygame.time.Clock()
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg_image, self.bg_image.get_rect())
        for platform in  self.platforms:
            platform.draw(self.screen)
    def create_platform(self):
        y_p = self.platforms[0].rect.y - 120
        for platf in range (5):
            self.platforms.append(Platform(random.randint(0, self.s_size[0] - 90), y_p))
            y_p = self.platforms[-1].rect.y - 120
    def update(self):
        for platform in self.platforms:
            platform.move()
        self.platform_logic()
    def platform_logic(self):
        for platform in self.platforms:
            if platform.rect.top >= self.s_size[1] + 50:
                self.platforms.remove(platform)
                y_p = self.platforms[-1].rect.y - 120
                self.platforms.append(Platform(random.randint(0, self.s_size[0] - 90), y_p))



main  = Main()







while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main.draw()
    main.update()
    pygame.display.update()
    main.clock.tick(60)
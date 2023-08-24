import pygame
import sys
import random
from platform import Platform
from back_ground import Back_ground
from dudlik import Dudlik

pygame.init()


class Main:
    def __init__(self):
        self.s_size = 480, 700
        self.screen = pygame.display.set_mode(self.s_size)
        self.platforms = [Platform(self.s_size[0] / 2 - 45, self.s_size[1] - 30)]
        self.create_platform()
        self.clock = pygame.time.Clock()
        self.fon = Back_ground(self.s_size)
        self.dudlik = Dudlik(self.s_size[0] / 2, self.s_size[1] - 70, self.s_size)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.fon.draw(self.screen)
        for platform in self.platforms:
            platform.draw(self.screen)
        self.dudlik.draw(self.screen)

    def create_platform(self):
        y_p = self.platforms[0].rect.y - 120
        for platf in range(6):
            self.platforms.append(Platform(random.randint(0, self.s_size[0] - 90), y_p))
            y_p = self.platforms[-1].rect.y - 120

    def update(self):
        for platform in self.platforms:
            platform.move()
        self.platform_logic()
        self.fon.move()
        self.fon.logic()
        self.dudlik.move()
        self.dudlik.logic()

    def platform_logic(self):
        for platform in self.platforms:
            if platform.rect.top >= self.s_size[1] + 50:
                self.platforms.remove(platform)
                y_p = self.platforms[-1].rect.y - 120
                self.platforms.append(Platform(random.randint(- 45, self.s_size[0] - 45), y_p))


main = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                main.dudlik.speed_x = -main.dudlik.speed
            if event.key == pygame.K_RIGHT:
                main.dudlik.speed_x = main.dudlik.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                main.dudlik.speed_x = 0
            if event.key == pygame.K_RIGHT:
                main.dudlik.speed_x = 0
    main.draw()
    main.update()
    pygame.display.update()
    main.clock.tick(60)

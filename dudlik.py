import pygame

class Dudlik:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = pygame.image.load('images/dudlik.png')
        self.rect = self.image.get_rect()
        self.rect.center = x, y
    def draw(self, screen):
        screen.blit(self.image, self.rect)
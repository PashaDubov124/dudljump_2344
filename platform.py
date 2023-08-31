import pygame


class Platform:
    def __init__(self, x, y):
        self.color = (0, 0, 0)
        self.size = 90, 10
        self.speed = 1
        self.rect = pygame.Rect(x, y, self.size[0], self.size[1])
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        self.rect.y += self.speed

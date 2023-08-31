import pygame


class Dudlik:
    def __init__(self, x, y, s_size):
        self.x, self.y = x, y
        self.image = pygame.image.load('images/666.png')
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.score = 0
        self.font = pygame.sysfont.SysFont("Arial", 20)
        self.speed_x = 0
        self.speed = 4
        self.s_size = s_size
        self.speed_y = 4

    def logic(self):
        if self.rect.left > self.s_size[0]:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = self.s_size[0]
    def draw(self, screen):
        text = self.font.render(f"Score: {self.score}", True, (0,0,0))
        text_rect = text.get_rect()
        screen.blit(text, text_rect)
        screen.blit(self.image, self.rect)

    def jump(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.rect.bottom in range(platform.rect.top,platform.rect.top + 6) :
                    self.speed_y -= 20
                    self.score += 1
                    if self.speed_y < -20:
                        self.speed_y = -20


    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.speed_y += 1
        if self.speed_y > 3:
            self.speed_y = 3

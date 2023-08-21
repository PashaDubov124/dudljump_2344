import pygame

class Back_ground:
    def __init__(self, s_size):
        self.s_size = s_size
        self.bg_image = pygame.image.load("images/fon_2.jpg")
        self.bg_image_2 = pygame.image.load("images/fon_2.jpg")
        self.bg_rect_1 = self.bg_image.get_rect()
        self.bg_rect_2 = self.bg_image_2.get_rect()
        self.bg_rect_1.bottomleft = 0, s_size[1]
        self.bg_rect_2.bottomleft = self.bg_rect_1.topleft
        self.speed = 1
        self.bg_s = [self.bg_rect_1, self.bg_rect_2]

    def logic(self):
        for bg in self.bg_s:
            if bg.top > self.s_size[1]:
                bg.bottom = self.bg_s[-1].top
                bg = self.bg_s.pop(0)
                self.bg_s.append(bg)




    def draw(self, screen):
        screen.blit(self.bg_image, self.bg_rect_1)
        screen.blit(self.bg_image_2, self.bg_rect_2)
    def move(self):
        self.bg_rect_1.y += 1
        self.bg_rect_2.y += 1
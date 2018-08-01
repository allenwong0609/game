import pygame
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768


class Bullet(object):

    def __init__(self, win, hero_x, hero_y, hero_w):
        self.img = pygame.image.load("res/hero_bullet_7.png")
        self.window = win

        self.rect = self.img.get_rect()
        self.rect[0] = hero_x + hero_w/2 - self.rect[2]/2
        self.rect[1] = hero_y - self.rect[3]

    def move(self):
        self.rect[1] -= 6

    def blited(self):
        self.window.blit(self.img, (self.rect[0], self.rect[1]))  # 设置飞机的位置和矩形对象的位置是一致的

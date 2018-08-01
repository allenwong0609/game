import pygame
import random
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768


class Enemy(object):

    def __init__(self, win):
        self.img = pygame.image.load("res/img-plane_%s.png" % random.randint(1, 7))
        self.window = win
        self.rect = self.img.get_rect()
        self.rect[0] = random.randint(0, WINDOW_WIDTH-self.rect[2])
        self.rect[1] = 0  # random.randint(-100, 30)
        self.speed = random.randint(30, 50) * 0.1

    def move(self):
        self.rect[1] += self.speed

        if self.rect[1] > WINDOW_HEIGHT:   # 敌机超出窗口的时候，需要重置一下这个敌机
            # self.rect[1] = 0
            self.reset()

    def blited(self):
        self.window.blit(self.img, (self.rect[0], self.rect[1]))  # 设置飞机的位置和矩形对象的位置是一致的

    def reset(self):
        self.img = pygame.image.load("res/img-plane_%s.png" % random.randint(1, 7))
        self.rect[0] = random.randint(0, WINDOW_WIDTH - self.rect[2])
        self.rect[1] = 0  # random.randint(-100, 30)
        self.speed = random.randint(30, 50) * 0.1

import pygame
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768


class Map(object):

    def __init__(self, win):
        self.img = pygame.image.load("res/img_bg_level_1.jpg")
        self.img2 = pygame.image.load("res/img_bg_level_1.jpg")
        self.window = win
        self.y = 0
        self.y2 = -WINDOW_HEIGHT

    def move(self):
        """地图移动的方法"""
        self.y += 3
        self.y2 += 3

        # 如果某个y的值大于窗口高度，就把它的这个y值重新设置回-窗口高度(拿回上面去)
        if self.y > WINDOW_HEIGHT:
            self.y = -WINDOW_HEIGHT
        if self.y2 > WINDOW_HEIGHT:
            self.y2 = -WINDOW_HEIGHT

    def blited(self):
        self.window.blit(self.img, (0, self.y))
        self.window.blit(self.img2, (0, self.y2))
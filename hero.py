import pygame
from bullet import Bullet
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768


class Hero(object):

    def __init__(self, win):
        self.img = pygame.image.load("res/hero.png")
        self.window = win

        # 获取图片的矩形对象
        # hero_rect = hero.get_rect()  # 获取图片的矩形对象（一个图片就会有一个矩形对象，通过这个.get_rect() 来获取矩形对象， 这个矩形对象的宽高和图片一样）
        # print(hero_rect)   # <rect(0, 0, 120, 78)>
        # print(hero_rect[2])   # 120   # hero_rect[2]获取到图片的宽度， hero_rect[3]获取到图片的高度
        # 得到矩形对象
        self.rect = self.img.get_rect()
        self.speed = 3  # 飞机的移动速度
        self.rect[0] = WINDOW_WIDTH/2-self.rect[2]/2   # 飞机矩形对象初始的x值
        self.rect[1] = 600  # 飞机矩形对象初始的y值

        self.bullets = []   # 用来存放子弹对象

    def move(self):
        # print(self.rect)
        # 长按控制飞机移动
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            if self.rect[1] > 0:            # 为了限制飞机的移动边界，下面这行代码（造成飞机的移动）在y>0的情况下才执行
                self.rect[1] -= self.speed  # 最终决定飞机位置的改变--移动，  往上移动
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            if self.rect[1] < WINDOW_HEIGHT - self.rect[3]:
                self.rect[1] += self.speed
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if self.rect[0] > 0:
                self.rect[0] -= self.speed
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            if self.rect[0] < WINDOW_WIDTH - self.rect[2]:  # x必须小于串口宽度-飞机图片宽度，才执行下面的代码
                self.rect[0] += self.speed

    def shot(self):
        self.bullets.append(Bullet(self.window, self.rect[0], self.rect[1], self.rect[2]))

    def blited(self):
        self.window.blit(self.img, (self.rect[0], self.rect[1]))  # 设置飞机的位置和矩形对象的位置是一致的
        # 显示子弹： [Bullet(),Bullet(),Bullet()]
        for i in self.bullets:   # i就是每一个子弹对象
            if i.rect[1] < 0:
                self.bullets.remove(i)
            else:
                i.blited()

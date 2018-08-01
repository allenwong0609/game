import pygame
import sys
from map import Map  # 从map模块导入Map这个类
from hero import Hero  # 从hero模块导入Hero这个类
from enemy import Enemy  # 从enemy模块导入Enemy这个类

WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768


class PlaneWar(object):

    def __init__(self):
        pygame.init()
        # 创建游戏窗口对象
        self.window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

        self.set_window()
        self.map = Map(self.window)
        self.hero = Hero(self.window)
        self.enemy = [Enemy(self.window) for _ in range(4)]
        self.score = 0

    @staticmethod
    def set_window():
        # 设置窗口标题
        pygame.display.set_caption("飞机大战2018正常版")

        # 设置窗口小图标--icon
        icon = pygame.image.load("res/app.ico")
        pygame.display.set_icon(icon)
        # 加载背景音乐
        pygame.mixer.music.load("./res/bg2.ogg")
        # 循环播放背景音乐
        pygame.mixer.music.play(-1)

    def events(self):
        """执行窗口事件"""
        # 窗口事件
        event_list = pygame.event.get()

        for event in event_list:
            # 1. 鼠标点击关闭窗口事件
            if event.type == pygame.QUIT:
                print("关闭了窗 口")
                sys.exit()

            # 2. 键盘按下事件
            if event.type == pygame.KEYDOWN:

                # 判断用户按下的键是否是空格键
                if event.key == pygame.K_SPACE:
                    print("按了空格 ")
                    self.hero.shot()   # 飞机发射子弹

    def move(self):
        """处理各个对象(飞机、子弹、敌机、地图)的移动"""
        self.map.move()
        self.hero.move()
        for i in self.hero.bullets:  # i就是每一个子弹
            i.move()

        for i in self.enemy:  # i是每一只敌机
            i.move()

    def blit(self):
        """绘制窗口中需要 显示 的所有的对象"""
        self.map.blited()
        self.hero.blited()
        for i in self.enemy:  # i是每一只敌机
            i.blited()

    def update(self):
        """更新界面"""
        pygame.display.update()

    def is_bullet_hit_enemy(self):
        # 判断两个矩形是否相交，相交返回True，否则返回False
        # flag = pygame.Rect.colliderect(rect1, rect2)
        # if flag:

        for i in self.enemy:
            for j in self.hero.bullets:
                if pygame.Rect.colliderect(i.rect, j.rect):
                    i.reset()
                    self.score += 20
                    # self.hero.bullets.remove(j)

    def is_hero_hit_enemy(self):
        for i in self.enemy:
            if pygame.Rect.colliderect(i.rect, self.hero.rect):
                return True  # 如果相交了就返回真
        else:
            return False

    def write(self, text, y, font_size):
        font = pygame.font.SysFont('SimHei', font_size)
        # render(text(文本内容), antialias(抗锯齿), color(RGB))，返回文字对象
        textobj = font.render(text, 1, (200, 200, 200))

        # 设置文字矩形对象位置
        textrect = textobj.get_rect()
        textrect.move_ip(WINDOW_WIDTH/2-textrect[2]/2, y)
        # 在指定位置绘制指定文字对象
        self.window.blit(textobj, textrect)
        # 更新界面
        pygame.display.update()

    def wait_player_input(self):
        while True:
            # 窗口事件
            event_list = pygame.event.get()

            for event in event_list:
                # 1. 鼠标点击关闭窗口事件
                if event.type == pygame.QUIT:
                    print("关闭了窗 口")
                    sys.exit()
                # 2. 键盘按下事件
                if event.type == pygame.KEYDOWN:

                    # 判断用户按下的键是否是a键
                    if event.key == pygame.K_RETURN:
                        print("按了回车")
                        return

    def gameover(self):
        # 停止背景音乐
        pygame.mixer.music.stop()
        # 加载音效
        boom_sound = pygame.mixer.Sound("./res/gameover.wav")
        # 播放音效
        boom_sound.play()

        self.write("游戏结束", 150, 50)
        self.write("按Enter关闭窗口", 230, 40)
        self.wait_player_input()

    def gamebegin(self):
        """游戏开始界面"""
        self.map.blited()
        self.write("游戏开始", 150, 50)
        self.write("按Enter开始游戏", 230, 40)
        self.wait_player_input()

    def run(self):

        self.gamebegin()
        while True:
            # 1、事件
            self.events()
            # 2、各个对象(飞机、子弹、敌机、地图)的移动
            self.move()

            # 判断子弹是否打中敌机
            self.is_bullet_hit_enemy()
            # 判断飞机是否撞击到敌机
            if self.is_hero_hit_enemy():
                break
            # 3、往窗口中绘制图片
            self.blit()
            self.write("得分：%s" % self.score, 0, 30)
            # 4、更新界面
            self.update()
        # gameover界面
        self.gameover()

if __name__ == "__main__":

    game = PlaneWar()   # 创建游戏对象并且初始化工作
    game.run()  # 启动游戏

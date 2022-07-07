__Author__ = 'Nero Wu'
# 金币组件

import pygame
from data import tools,setup
from data import constants as C

# pygame的精灵类（精灵指：游戏可移动元素）
class FlshingCoin(pygame.sprite.Sprite):
    def __init__(self):
        super(FlshingCoin, self).__init__()
        self.frames = []
        self.frame_index = 0
        # 四个元组，对应四张图片的X,Y,宽,高
        # 要实现闪烁效果，需要对图片进行: 1->2->3->2的更新
        frame_rects = [(1,160,5,8),(9,160,5,8),(17,160,5,8),(9,160,5,8)]
        self.load_frame(frame_rects)

        # 继承精灵类，获取图片信息
        self.image = self.frames[self.frame_index]
        # 获取金币坐标
        self.rect = self.image.get_rect()
        # 设置金币位置
        self.rect.x = 280
        self.rect.y = 65

        # 计时器，用于时间判断
        self.timer = 0

    def load_frame(self,frame_rects):
        # 加载item_objects图片
        sheet = setup.GRAPHICS['item_objects']
        # 把剪切后的金币图片，存入frames列表里
        for frame_rect in frame_rects:
            # *frame_rect表示把元组内的元素，分解成4个
            self.frames.append(tools.get_image(sheet,*frame_rect,(0,0,0),C.BG_MULTI))

    # 金币闪烁逻辑，简单理解就是每到一定时间，换一张图片展示
    def update(self):
        # 获取当前时间
        self.current_time = pygame.time.get_ticks()
        # 每张图片超时时间
        frame_durations = [375,125,125,125]

        if self.timer == 0:
            self.timer = self.current_time
        # 当前时间-计时器的值，假如大于当前图片超时时间，更换index(换图片)
        elif self.current_time - self.timer > frame_durations[self.frame_index]:
            # 图片 index + 1
            self.frame_index += 1
            self.frame_index %= 4
            self.timer = self.current_time

        # 更换图片
        self.image = self.frames[self.frame_index]
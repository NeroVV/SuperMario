__Author__ = 'Nero Wu'
# 文字信息

import pygame
from data import constants as C
pygame.font.init()

'''
文字实现方式有2种:
1. 字体 -> 文字 -> 图片
2. 文字 -> 抠图 -> 图片
'''
class Info:
    def __init__(self,state):
        self.state = state
        self.create_state_labels()
        self.create_info_labels()

    # 用于创建某阶段特有的文字
    def create_state_labels(self):
        self.state_labels = {}
        if self.state == C.MAIN_MENU:
            self.state_labels[(self.create_label('1 PLAYER GAME'))] = (270,350)
            self.state_labels[(self.create_label('2 PLAYER GAME'))] = (270,395)
            self.state_labels[(self.create_label('TOP - '))] = (288,455)
            self.state_labels[(self.create_label('000000'))] = (398,455)

    # 用于创建通用分数、金币数等信息
    def create_info_labels(self):
        self.info_labels = {}
        self.info_labels[(self.create_label('MARIO'))] = (75,30)
        self.info_labels[(self.create_label('WORLD'))] = (480,30)
        self.info_labels[(self.create_label('TIME'))] = (655,30)
        self.info_labels[(self.create_label('000000'))] = (73,55)
        self.info_labels[(self.create_label('x00'))] = (300,55)
        self.info_labels[(self.create_label('1-1'))] = (495,55)

    # 通用方法，字体大小、缩放多少
    def create_label(self,label,size=35,width_scale=1.25,height_scale=1):
        # 新建一个字体，载入字体文件
        font = pygame.font.Font(C.FONT,size)
        # 将文字渲染成图片
        # False:关闭抗锯齿
        label_image = font.render(label,True,(255,255,255))
        '''
        # 获取图片坐标
        rect = label_image.get_rect()
        # 缩放图片大小
        label_image = pygame.transform.scale(
            label_image,(
                int(rect.width * width_scale),
                int(rect.height * height_scale)
            )
        )
        '''

        return label_image

    # 实时更新分数、金币数信息
    def update(self):
        pass


    # 传入图层，用于显示
    def draw(self,surface):
        # main_menu 特有的文字
        for label in self.state_labels:
            # label为key，代表图片
            # self.state_labels[label]为value值，代表位置
            surface.blit(label,self.state_labels[label])

        # 通用分数、金币数
        for label in self.info_labels:
            # label为key，代表图片
            # self.state_labels[label]为value值，代表位置
            surface.blit(label,self.info_labels[label])
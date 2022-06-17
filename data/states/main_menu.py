__Author__ = 'Nero Wu'
# 游戏主界面

import pygame
from data import setup
from data import tools
from data import constants as C

class MainMenu:
    def __init__(self):
        self.setup_backgroud()
        self.setup_player()
        self.setup_cursor()
    
    def setup_backgroud(self):
        self.backgroud = setup.GRAPHICS['level_1']
        # get_rect获得背景图片矩形
        self.backgroud_rect = self.backgroud.get_rect()
        # 放大图片，把图片宽和高放大为屏幕（800，600）
        self.backgroud = pygame.transform.scale(
            self.backgroud,
            (
                int(self.backgroud_rect.width* C.BG_MULTI),
                int(self.backgroud_rect.height* C.BG_MULTI)
            )
        )
        # 游戏滑动窗口,滑动窗口设置为屏幕大小
        self.viewport = setup.SCREEN.get_rect()

        # 获得标题图片
        self.title = setup.GRAPHICS['title_screen']
        # get_image把标题裁剪出来
        '''
        标题图片参数
        左上角X: 1
        左上角Y: 60
        宽: 176
        高: 88
        底色紫色: 255,0,220
        '''
        self.caption = tools.get_image(
            self.title,
            1,
            60,
            176,
            88,
            (255,0,220),
            C.BG_MULTI
        )
    
    def setup_player(self):
        # 获得马里奥图片
        self.mario_bros = setup.GRAPHICS['mario_bros']
        '''
        马里奥图片参数
        左上角X: 178
        左上角Y: 32
        宽: 12
        高: 16
        底色白色: 0,0,0
        '''
        self.player_image = tools.get_image(
            self.mario_bros,
            178,
            32,
            12,
            16,
            (0,0,0),
            C.PLAYER_MULTI
        )
    
    def setup_cursor(self):
        # 获得物品图片
        self.item_objects = setup.GRAPHICS['item_objects']
        '''
        光标图片参数
        左上角X: 24
        左上角Y: 160
        宽: 8
        高: 8
        底色白色: 0,0,0
        '''
        self.cursor = tools.get_image(
            self.item_objects,
            24,
            160,
            8,
            8,
            (0,0,0),
            C.PLAYER_MULTI
        )

    def update(self,surface):
        # 把滑动窗口载入画布
        surface.blit(self.backgroud,self.viewport)
        # 把标题图片载入画布(170,100)位置
        surface.blit(self.caption,(170,100))
        # 把人物图片载入画布(110,490)位置
        surface.blit(self.player_image,(110,490))
        # 把光标图片载入画布(220,360)位置
        surface.blit(self.cursor,(220,360))

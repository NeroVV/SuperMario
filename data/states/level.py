__Author__ = 'Nero Wu'
# 游戏关卡

from data.components import info
from data import tools,setup
from data import constants as C
import pygame

class Level:
    def __init__(self):
        self.finished = False
        self.next = None
        # 虽然Info create_state_labels暂时没有level这个label
        # 但还有create_info_labels和flash_coin这些通用的方法
        self.info = info.Info(C.LEVEL)
        self.setup_background()

    # 设置背景图片
    def setup_background(self):
        self.backgroud = setup.GRAPHICS['level_1']
        rect = self.backgroud.get_rect()
        self.backgroud = pygame.transform.scale(
            self.backgroud,(
                int(rect.width * C.BG_MULTI),
                int(rect.height * C.BG_MULTI)
            )
        )
        self.backgroud_rect = self.backgroud.get_rect()

    def update(self,surface,keys):
        self.draw(surface)

    def draw(self,surface):
        # 把背景画到画布上
        surface.blit(self.backgroud,(0,0))
        # 把分数、关卡信息等，画到画布上
        self.info.draw(surface)
        # 调用update方法，令金币闪烁
        self.info.update()
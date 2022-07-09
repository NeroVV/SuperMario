__Author__ = 'Nero Wu'
# 载入游戏界面

from data.components import info
from data import constants as C
import pygame

class LoadScreen:
    def __init__(self):
        self.finished = False
        self.next = C.LEVEL
        # loadScreen阶段时间到，自动切换finished状态
        self.timer = 0
        # 载入文字和马里奥图片
        self.info = info.Info(C.LOAD_SCREEN)

    def update(self,surface,keys):
        self.draw(surface)
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - self.timer > 2000:
            self.finished = True
            self.timer = 0

    # 设置背景颜色
    def draw(self,surface):
        surface.fill((0,0,0))
        # 把文字和马里奥画到画布上
        self.info.draw(surface)
        # 调用update方法，令金币闪烁
        self.info.update()
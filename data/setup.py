__Author__ = 'Nero Wu'
# 游戏启动初始化设置

import pygame
from data import constants as C
from data import tools

pygame.init()
#设置屏幕大小
pygame.display.set_mode((C.SCREEN_W,C.SCREEN_H))

# 加载全部图片
GRAPHICS = tools.load_graphics('resources/graphics')
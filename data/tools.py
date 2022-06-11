__Author__ = 'Nero Wu'
# 工具和游戏主控

import pygame
import random

class Game:
    def __init__(self):
        # 画布初始化
        self.screen = pygame.display.get_surface()
        # 帧数初始化
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            # 获取输入设备更新事件
            for event in pygame.event.get():
                # 事件类型为退出
                if event.type == pygame.QUIT:
                    # 退出游戏
                    pygame.display.quit()

            # 填充画布颜色
            self.screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            # 更新画布
            pygame.display.update()
            # 帧数设置（每秒60帧）
            self.clock.tick(60)

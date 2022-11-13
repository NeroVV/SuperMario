__Author__ = 'Nero Wu'
# 游戏关卡

from data.components import info,player
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
        self.setup_player()

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

    # 设置游戏人物
    def setup_player(self):
        self.player = player.Player('mario')
        self.player.rect.x = 300
        self.player.rect.y = 300

    def update(self,surface,keys):
        # 根据键盘输入信息，获取玩家速度
        self.player.update(keys)
        self.update_player_position()
        self.draw(surface)

    # 通过玩家速度，更新玩家位置信息
    def update_player_position(self):
        self.player.rect.x += self.player.x_vel
        self.player.rect.y += self.player.y_vel

    def draw(self,surface):
        # 把背景画到画布上
        surface.blit(self.backgroud,(0,0))
        surface.blit(self.player.image,self.player.rect)

        # 把分数、关卡信息等，画到画布上
        self.info.draw(surface)

        # 调用update方法，令金币闪烁
        self.info.update()
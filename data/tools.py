__Author__ = 'Nero Wu'
# 工具和游戏主控

import pygame
import random
import os

class Game:
    def __init__(self):
        # 画布初始化
        self.screen = pygame.display.get_surface()
        # 帧数初始化
        self.clock = pygame.time.Clock()

    def run(self,GRAPHICS):
        while True:
            # 获取输入设备更新事件
            for event in pygame.event.get():
                # 事件类型为退出
                if event.type == pygame.QUIT:
                    # 退出游戏
                    pygame.display.quit()

            # 填充画布颜色
            self.screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            image = get_image(GRAPHICS['mario_bros'],145,32,16,16,(0,0,0),5)
            self.screen.blit(image,(300,300))
            # 更新画布
            pygame.display.update()
            # 帧数设置（每秒60帧）
            self.clock.tick(60)

# 图片加载
def load_graphics(path,accept=('.jpg','.png','.bmp','.gif')):
    graphics = {}
    # 获取文件下文件名称
    for pic in os.listdir(path):
        # 分割文件名 (name文件名，ext文件类型)
        name,ext = os.path.splitext(pic)
        if ext.lower() in accept:
            # 载入图片
            img = pygame.image.load(os.path.join(path,pic))
            # 判断图片是否为透明底
            if img.get_alpha():
                # 提高 blit 的速度，也实现透明效果
                # 保留底部透明的部分
                img = img.convert_alpha()
            else:
                # 使用 convert 可以转换格式，提高 blit 的速度
                img = img.convert()
            graphics[name] = img
    return graphics

# 图片剪裁
def get_image(sheet,x,y,width,height,colorkey,scale):
    '''
    :param sheet: 图片
    :param x: 方框左上角x轴坐标
    :param y: 方框左上角y轴坐标
    :param width: 方框宽度
    :param height: 方框高度
    :param colorkey: 把图片底色抠出
    :param scale: 放大倍数
    :return:
    '''
    # 创建跟方框一样大小空图层
    image = pygame.Surface((width,height))
    # 把方框图载入画布
    # 0.0代表画到哪个位置，x、y、w、h代表sheet里哪个区域要取出来
    image.blit(sheet,(0,0),(x,y,width,height))
    # 底色抠图
    image.set_colorkey(colorkey)
    # 放大图片
    image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    return image

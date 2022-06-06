__Author__ = 'Nero Wu'
# 熟悉pygame的代码

import pygame

def ToyCode():
    # pygame初始化
    pygame.init()

    #设置屏幕大小
    w,h = 500,500
    pygame.display.set_mode((w,h))
    # 画布初始化
    screen = pygame.display.get_surface()

    # 导入背景图
    graphics = pygame.image.load('graphics.png')
    # 设置背景图大小跟屏幕一致
    graphics = pygame.transform.scale(graphics,(w,h))

    # 载入超级马里奥图片
    mario_image = pygame.image.load('mario.png')

    # 创建精灵（游戏可移动元素）
    mario = pygame.sprite.Sprite()
    mario.image = mario_image
    # 获取精灵坐标（初始在左上角）
    mario.rect = mario.image.get_rect()
    # 设置人物初始位置
    mario.rect.x,mario.rect.y = w/2,h/2

    # 玩家组（存储精灵信息）
    player_group = pygame.sprite.Group()
    player_group.add(mario)

    # 开始游戏
    # 基础原理：更新人物信息->画图展现->再次更新人物信息->再次画图展现
    # 一直循环这2步，直到游戏结束
    while True:
        # 获取输入设备更新事件
        for event in pygame.event.get():
            # 事件类型为退出
            if event.type == pygame.QUIT:
                # 退出游戏
                pygame.display.quit()
                quit()
            # 返回一系列布尔值，表示键盘上每个键的状态。使用键常量值来索引数组。True值表示按下该按钮
            keys = pygame.key.get_pressed()
            # 检索到向下按键，人物向下移动10坐标
            if keys[pygame.K_DOWN]:
                mario.rect.y += 10
            elif keys[pygame.K_UP]:
                mario.rect.y -= 10
            elif keys[pygame.K_RIGHT]:
                mario.rect.x += 10
            elif keys[pygame.K_LEFT]:
                mario.rect.x -= 10

        # 画图展示
        # 把背景图载入画布
        screen.blit(graphics,(0,0))
        # 把精灵按照坐标载入画布
        player_group.draw(screen)
        # 更新画布
        pygame.display.update()


if __name__ == '__main__':
    ToyCode()
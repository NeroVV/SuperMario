import pygame
from data import tools,setup
from data import constants as C

class Player(pygame.sprite.Sprite):
    def __init__(self,name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.setup_states()
        self.setup_velocities()
        self.setup_timers()
        self.load_images()


    # 设置主角状态
    def setup_states(self):
        pass

    # 主角速度设置
    def setup_velocities(self):
        # x和y轴方向的初始速度
        self.x_vel = 0
        self.y_vel = 0

    # 主角动作的计时器
    def setup_timers(self):
        # 步行时长
        self.walking_timer = 0
        # 变身时长
        self.transition_timer = 0

    def load_images(self):
        sheet = setup.GRAPHICS['mario_bros']
        self.right_frames = []
        self.left_frames = []

        # 运动的4个帧信息
        frame_rects = [
            (178,32,12,16),
            (80,32,15,16),
            (96,32,12,16),
            (112,32,12,16),
        ]

        for frame_rect in frame_rects:
            right_image = tools.get_image(sheet,*frame_rect,(0,0,0),C.PLAYER_MULTI)
            left_image = pygame.transform.flip(right_image,True,False)

            self.right_frames.append(right_image)
            self.left_frames.append(left_image)

        self.frame_index = 0
        self.frames = self.right_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    # 根据按键行为，改变图片帧数
    def update(self,keys):
        # 设置时间间隔，修改运动图片
        self.current_time = pygame.time.get_ticks()
        if keys[pygame.K_RIGHT]:
            self.x_vel = 5
            self.y_vel = 0
            self.frames = self.right_frames
        if keys[pygame.K_LEFT]:
            self.x_vel = -5
            self.y_vel = 0
            self.frames = self.left_frames

        # 时间间隔大于100毫秒，切换下一张图片
        if self.current_time - self.walking_timer > 100:
            self.walking_timer = self.current_time
            self.frame_index += 1
            self.frame_index %= 4
        self.image = self.frames[self.frame_index]


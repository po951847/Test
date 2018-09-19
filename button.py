import pygame.sysfont


class Button:
    def __init__(self, ai_settings, screen, msg):
        # 初始化按钮属性
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 设置按钮的尺寸和属性
        self.width, self.height = 200, 50
        self.button_color = (233, 233, 233)
        self.text_color = (0, 255, 0)
        self.font = pygame.sysfont.SysFont(None, 50)

        # 创建按钮的rect对象
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮标签
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """msg渲染成图像"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
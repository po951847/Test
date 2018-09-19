import pygame.sysfont


class Scoreboard():
    """显示得分设计的属性"""
    def __init__(self, ai_settings, screen, stats):
        """初始化属性"""
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # 字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.gb_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """显示得分"""
        self.screen.blit(self.score_image, self.score_rect)

class Settings():
    """存储游戏的所有设置"""
    def __init__(self):
        """初始化设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.gb_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 4
        self.ship_limit = 3   # 3条命
        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 600
        self.bullet_height = 1
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 10
        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
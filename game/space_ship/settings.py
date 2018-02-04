class Settings:
    """ 게임 설정을 저장 """
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 80, 230)

        # 우주선 설정
        self.ship_speed_factor = 1.5
        self.ship_limit = 3


        # 미사일 설정
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 60, 60
        self.bullets_allowed = 10

        # 외계인 설정
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # 게임 속도 높이는 설정
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction
        self.fleet_direction = 1

        # 점수 설정
        self.alien_points = 50

    def increase_speed(self):
        # 1.1 배씩 증가함
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

    
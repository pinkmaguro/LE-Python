import pygame

class Ship:
    def __init__(self, ai_settings, screen):
        """우주선을 초기화 하고 시작 위치를 지정한다."""
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() # 직삭각형
        self.screen_rect = screen.get_rect()

        # 우주선을 화면 중앙 아래에 위치시킴
        self.rect.centerx = self.screen_rect.centerx # 직사각형 가운데 위치를 저장하는 변수가 있음 쩐다.
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # 이동 플래그
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """우주선의 현재 위치에 우주선을 그린다."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 이동 범위 제한
        if self.moving_right and self.rect.right < self.screen_rect.right:
             self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left:
             self.center += -self.ai_settings.ship_speed_factor
             
        # 이렇게 위치를 먼저 계산해서 ship 의 속성에 대입하는 편이 유연하다.
        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx
        



import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 게임 화면 만들기
    pygame.init()

    ai_settings = Settings()

    # 스크린 크기를 정해서 만든다.
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Play 버튼
    play_button = Button(ai_settings, screen, "Play")

    # 게임 기록용 인스턴스
    stats = GameStats(ai_settings)

    # 우주선을 만든다.
    ship = Ship(ai_settings, screen)

    # 미사일을 만든다.
    bullets = Group()

    # 외계인 을 만든다.
    # alien = Alien(ai_settings, screen)
    aliens = Group()

    # 점수판을 만든다.
    sb = Scoreboard(ai_settings, screen, stats)


    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_event(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 움직임을 계산한 후에 
            ship.update()
            
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 각 객체를 그린다.
        gf.update_screen(ai_settings, stats, screen, sb, ship, aliens, bullets, play_button)

if __name__ == '__main__':
    run_game()
import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien
from button import Button

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = (alien.rect.height * 2 * row_number) + alien.rect.height
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                            alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height)
                            - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows




def check_keydown_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
     

def fire_bullet(ai_settings, screen, ship, bullets):
    # 화면상 마사일이 3개 초과로는 못 만듬
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)   

def check_keyup_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False    


def check_event(ai_settings, screen, stats, play_button, ship, aliens ,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
                    bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
            bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)     
    if button_clicked and not stats.game_active:
        # 게임설정 리셋
        ai_settings.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_screen(ai_settings, stats, screen, sb, ship, aliens, bullets, play_button):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 점수를 표시
    sb.show_score()

    # 게임이 진행중이지 않다면 Play 버튼을 그린다.
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.update()



def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()

    # 화면 밖으로 나간 마시일 제거
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 마사일과 외계인이 충돌하면 둘 다 사라진다.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship,  aliens)   

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """ 우주선이 외계인과 충돌했을 때 """
    # 우주선 남은 목숨을 줄인다.
    if stats.ship_left > 0:
        stats.ship_left += -1
        aliens.empty()
        bullets.empty()
        sleep(0.5)
    else:
        stats.game_active = False
    # 외계인과 미사일 리스틀르 비운다.
    

    # 외계인 함대를 새로 만들고 우주선을 중앙에 배치한다.
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    sleep(0.5)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    # 그룹에 속한 모든 객체에 대해서 update() 가 실행된다.
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 우주선이 외계인과 출돌하는지 검사
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)



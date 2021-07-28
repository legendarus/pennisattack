import sys
import pygame
import write_hscore as wh
from bullet import Bullet
from vagine import Vagine
from time import sleep
def check_keydown_events(event, pa_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        pa_settings.sound_shot.play()
        fire_bullet(pa_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_play_buttom(pa_settings, screen, stats, sb, play_buttom, ship, vagines, bullets, mouse_x, mouse_y):
    """Запускает новую игру при нажатии кнопки ИГРАТЬ"""
    buttom_clicked = play_buttom.rect.collidepoint(mouse_x, mouse_y)
    if buttom_clicked and not stats.game_active:

        pygame.mixer.music.load("Trach.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        #Сброс игровых настроек
        pa_settings.initialize_dynamic_settings()
        #Скрывает указатель мыши
        pygame.mouse.set_visible(False)
        #Сброс игровой статистики
        stats.reset_stats()
        stats.game_active = True
        #Сброс изображений счетов и уровня
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ship()
        #Очистка вагин и пуль
        vagines.empty()
        bullets.empty()
        # Cоздание нового флота и размещение нового корабля в центре
        create_fleet(pa_settings, screen, ship, vagines)
        ship.center_ship()
def check_events(pa_settings, screen, stats, sb, play_buttom, ship, vagines, bullets):
    """Отрабатывает нажатия клавиш и движение мышью"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, pa_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_buttom(pa_settings, screen, stats, sb, play_buttom, ship, vagines, bullets, mouse_x, mouse_y)

def update_screen(pa_settings, screen, stats, sb, ship, vagines, bullets, play_buttom):
    """Обновляет изоображение экрана и отображает новый"""
    # при каждом проходе цикла отображается цвет
    screen.fill(pa_settings.bg_color)
    #Все пули выводятся позади корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    vagines.draw(screen)
    #Ввывод Счёта
    sb.show_score()
    #Отображение кнопки если игра неактивна
    if not stats.game_active:
        play_buttom.draw_buttom()
    # отображение последнего прорисованного экрана
    pygame.display.flip()

def ship_hit(pa_settings, screen, stats, sb, ship, vagines, bullets):
    """Отрабатывает столкновение вагин с кораблём"""
    if stats.ships_left > 0:
        #Уменьшение ship_left
        stats.ships_left -= 1
        #Обновление игровой информации
        sb.prep_ship()
        #Очистка вагин и пуль
        vagines.empty()
        bullets.empty()
        #Cоздание нового флота и размещение нового корабля в центре
        create_fleet(pa_settings, screen, ship, vagines)
        ship.center_ship()
        #пауза
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
def check_vagine_bottom(pa_settings, screen, stats, sb, ship, vagines, bullets):
    """Проверяет добрались ли Вагины до нижнего края экрана"""
    screen_rect = screen.get_rect()
    for vagine in vagines.sprites():
        if vagine.rect.bottom >= screen_rect.bottom:
            #Происходит тоже что и при столкновении с кораблём
            ship_hit(pa_settings, screen, stats, sb, ship, vagines, bullets)
            break
def check_bullet_vagine_collisions(pa_settings,screen, stats, sb, ship, vagines, bullets):
    """Обработка коализий пуль с вагинами"""
    collisions = pygame.sprite.groupcollide(bullets, vagines, True, True)
    if collisions:
        for vagine in collisions.values():
            stats.score += pa_settings.vagine_point * len(vagine)
            sb.prep_score()
            check_high_store(stats,sb)
    if len(vagines) == 0:
        #Уничтожение существующих пуль, увеличение скорости и создание нового влота
        bullets.empty()
        pa_settings.increase_speed()
        #Увеличивает уровень
        stats.level += 1
        sb.prep_level()
        create_fleet(pa_settings, screen, ship, vagines)
def update_bullets(pa_settings,screen, stats, sb, ship, vagines, bullets):
    """Обновляет позиции пуль и удаляет старые"""
    #Обновление позиции пуль
    bullets.update()
    # Удаление пуль, когда они достигают верхнего края экрана
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_vagine_collisions(pa_settings, screen, stats, sb, ship, vagines, bullets)

def fire_bullet(pa_settings, screen, ship, bullets):
    """Выпускает пюлю если пуля ещё не достигла вверхнего края"""
    # Создание новой пули и включение её в группу bullets
    if len(bullets) < pa_settings.bullet_allowed:
        new_bullet = Bullet(pa_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_vagines_x(pa_settings, vagine_width):
    """Вычисляем количество вагин в ряду"""
    available_space_x = pa_settings.screen_widht - (2 * vagine_width)
    number_vagines_x = int(available_space_x / (2 * vagine_width))
    return number_vagines_x
def get_number_rows(pa_settings, ship_height, vagine_height):
    """Определяется количество рядов, помещающихся на экране"""
    available_space_y = (pa_settings.screen_height - (3 * vagine_height) - ship_height)
    number_rows = int(available_space_y / (2 * vagine_height))
    return number_rows
def create_vagine(pa_settings,screen, vagines,vagine_number,row_number):
    """Создание вагины и размещение её в ряду"""
    vagine = Vagine(pa_settings, screen)
    vagine_width = vagine.rect.width
    vagine.x = vagine_width + (2 * vagine_width) * vagine_number
    vagine.rect.x = vagine.x
    vagine.rect.y = vagine.rect.height + 2 * vagine.rect.height * row_number
    vagines.add(vagine)
def create_fleet(pa_settings, screen, ship, vagines):
    """Создаёт флот вагин"""
    #Создание Вагины и вычисление количества вагин в ряду
    vagine = Vagine(pa_settings, screen)
    number_vagines_x = get_number_vagines_x(pa_settings, vagine.rect.width)
    number_rows = get_number_rows(pa_settings, ship.rect.height, vagine.rect.height)
    #Создание флота вагин
    for row_number in range(number_rows):
        for vagine_number in range(number_vagines_x):
            create_vagine(pa_settings, screen, vagines, vagine_number, row_number)
def check_fleet_edges(pa_settings,vagines):
    """Реагирует на достижение вагиной края экрана"""
    for vagine in vagines.sprites():
        if vagine.check_edges():
            change_fleet_direction(pa_settings, vagines)
            break
def change_fleet_direction(pa_settings, vagines):
    """Опускает весь флот и меняет направление флота"""
    for vagine in vagines.sprites():
        vagine.rect.y += pa_settings.fleet_drop_speed
    pa_settings.fleet_direction *= -1
def update_vagines(pa_settings, screen, stats, sb, ship, vagines, bullets):
    """Проверяет, достиг ли флот  края экрана,
    после чего обновляет позиции всех вагин во флоте"""
    check_fleet_edges(pa_settings, vagines)
    vagines.update()
    #Проверка коализий вагина-корабль
    if pygame.sprite.spritecollideany(ship, vagines):
        ship_hit(pa_settings, screen, stats, sb, ship, vagines, bullets)
    check_vagine_bottom(pa_settings, screen, stats, sb, ship, vagines, bullets)
def check_high_store(stats, sb):
    """Проверяет, появился ли новый рекорд"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        wh.write_record(stats.high_score)
        sb.prep_high_score()
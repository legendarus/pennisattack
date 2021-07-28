import pygame
from pygame.sprite import Group
from settings import Settings
from penis_ship import Ship
from game_stats import GameStats
from buttom import Buttom
from scoreboard import Scoreboard
import game_function as gf

def run_game():
    """Инициализирует игру и создаёт объект экрана"""
    pygame.init()
    pa_settings = Settings()
    #назначение цвета фона
    screen = pygame.display.set_mode((pa_settings.screen_widht,pa_settings.screen_height))
    pygame.display.set_caption("Penis Attack")
    #Создание кнопки Оплодотворять
    play_buttom = Buttom(pa_settings, screen, "ИГРАТЬ!")
    #Создание игровой статистики и подсчёта очков
    stats = GameStats(pa_settings)
    sb = Scoreboard(pa_settings, screen, stats)
    #Создание коробля, группы пуль и вагин
    ship = Ship(pa_settings, screen)
    bullets = Group()
    vagines = Group()

    #Создадим флот вагин
    gf.create_fleet(pa_settings,screen, ship, vagines)
    #Запуск основного цикла игры
    while True:
        #отслеживание действий клавы и мыши
        gf.check_events(pa_settings, screen, stats, sb, play_buttom, ship, vagines, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(pa_settings, screen, stats, sb, ship, vagines, bullets)
            gf.update_vagines(pa_settings, screen, stats, sb, ship, vagines, bullets)
        gf.update_screen(pa_settings, screen, stats, sb, ship, vagines, bullets,play_buttom)
run_game()
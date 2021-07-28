import pygame.font
from pygame.sprite import Group
from penis_ship import Ship
class Scoreboard:
    """Класс для ввывода игровой инвормации"""
    def __init__(self, pa_settings, screen, stats):
        """Инициализация подсчёта очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pa_settings = pa_settings
        self.stats = stats
        #Настройка шрифта для ввывода счёта
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #Подготовка исходного изоображения
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()
    def prep_score(self):
        """Преобразует текущий счёт в графическое изоображение"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.pa_settings.bg_color)
        #Вывод счёта в правой верхней части
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
    def prep_high_score(self):
        """Преобразует рекордный счёт в графическое изоображение"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.pa_settings.bg_color)
        #Выравниваем по верхней стороне
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    def prep_level(self):
        """Преобразует уровень в графическое изоображение"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.pa_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    def prep_ship(self):
        """Cообщает количество оставшиехся кораблей"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.pa_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """Создаём класс корабля-пениса, который задаёт правила его палёта"""
    def __init__(self, pa_settings, screen):
        """Инициализирует корабль и задаёт его изначальную позицию"""
        super().__init__()
        self.screen = screen
        self.pa_settings = pa_settings
        #Загрузка изоображения корабля
        self.image = pygame.image.load("images/pixelpenis.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Сохранение вещественной координаты центра коробля
        self.center = float(self.rect.centerx)
        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию коробля с учётом флага"""
        #Обновляем атрибут сenter не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.pa_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.pa_settings.ship_speed_factor
        #Обновление атрибута rect на основании center
        self.rect.centerx = self.center
    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        """Размещает корабль в центре нижнего края"""
        self.center = self.screen_rect.centerx

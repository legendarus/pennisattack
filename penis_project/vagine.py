import pygame
from pygame.sprite import Sprite

class Vagine(Sprite):
    """Класс представляет собой одну вагину"""
    def __init__(self, pa_settings,screen):
        """Инициилизирует Вагину и задаёт ей параметры"""
        super().__init__()
        self.screen = screen
        self.pa_settings = pa_settings
        # Загрузка изоображения вагины и назначение атрибута rect
        self.image = pygame.image.load("images/vagina.png")
        self.rect = self.image.get_rect()
        #Каждый новый пришелец появляется в верхнем левом углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Cохранение точной позиции вагины
        self.x = float(self.rect.x)
    def blitme(self):
        """Выводит вагину на экран"""
        self.screen.blit(self.image, self.rect)
    def check_edges(self):
        """Возвращает True, если вагина находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        """Перемещение вагин вправо или влево"""
        self.x += self.pa_settings.vagine_speed_factor * self.pa_settings.fleet_direction
        self.rect.x = self.x


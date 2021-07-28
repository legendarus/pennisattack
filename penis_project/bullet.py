import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Создаёт пули корабля"""
    def __init__(self,pa_settings,screen, ship):
        """Cоздаёт объект пули в текущей позиции корабля"""
        super().__init__()
        self.screen = screen
        #Создание пули в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0,0, pa_settings.bullet_widht,pa_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #Позиция пули хравиться в вещественном формате
        self.y = float(self.rect.y)
        self.color = pa_settings.bullet_color
        self.speed_factor = pa_settings.bullet_speed_factor
    def update(self):
        """Перемещает пулю вврех по экрану"""
        #Обновление позиции пули в вещественном формате
        self.y -= self.speed_factor
        #Обновление позиции прямоутольника
        self.rect.y = self.y
    def draw_bullet(self):
        """Ввывод пули на экран"""
        pygame.draw.rect(self.screen,self.color,self.rect)
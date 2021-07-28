from pygame import mixer
class Settings():
    """Класс настроек игры Penis Attack"""
    def __init__(self):
        "Инициализация настровет игры"
        self.screen_widht = 1200
        self.screen_height = 800
        self.bg_color = (234, 109, 33)
        #Настройки корабля
        self.ship_limit = 3
        #Настройки пуль
        self.bullet_widht = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullet_allowed = 3
        #Настройки Вагин
        self.fleet_drop_speed = 10
        #Темп ускорения игры
        self.speedup_scale = 1.1
        #Темп увеличения стоимости вагин
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        self.sound_shot = mixer.Sound('shot.wav')
    def initialize_dynamic_settings(self):
        """Инициализирует настройки меняющиеся в ходе игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.vagine_speed_factor = 1
        # fleet_direction = 1 обохначает движение вправо; а -1 - влево
        self.fleet_direction = 1
        #Подсчёт очков
        self.vagine_point = 50

    def increase_speed(self):
        """Увеличивает настройки скорости игры и стоимоти вагин"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.vagine_speed_factor *= self.speedup_scale
        self.vagine_point = int(self.vagine_point * self.score_scale)

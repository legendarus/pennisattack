import os.path
import write_hscore as wh
class GameStats():
    """Отслеживание статистики"""
    def __init__(self, pa_settings):
        """Инициализирует статистику"""
        self.pa_settings = pa_settings
        self.reset_stats()
        #Игра запускается в активном состоянии
        self.game_active = False
        #рекорд не должен сбрасываться
        if os.path.isfile("record.json"):
            self.high_score = wh.read_record()
        else:
            self.high_score = 0
    def reset_stats(self):
        """Инициализирует статистику изменяющееся в ходе игры"""
        self.ships_left = self.pa_settings.ship_limit
        self.score = 0
        self.level = 1
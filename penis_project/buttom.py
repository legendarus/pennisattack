import pygame.font
class Buttom ():
    """Кнопка в игре"""
    def __init__(self, pa_settings, screen, msg):
        """Инициализируем кнопку"""
        #self.pa_settings = pa_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #Назначение размеров и свойств кнопки
        self.width,self.height = 200, 50
        self.buttom_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.msg = msg
        #Построение объекта и выравнивание по центру экрана
        self.rect = pygame.Rect(0, 0, self.width,self.height)
        self.rect.center = self.screen_rect.center
        #Сообщение кновки создаётся только один раз
        self.prep_msg(msg)
    def prep_msg(self,msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.buttom_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    def draw_buttom(self):
        #Отображение пустой кнопки и ввывод сообщения
        self.screen.fill(self.buttom_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
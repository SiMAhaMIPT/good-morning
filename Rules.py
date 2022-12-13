import pygame
import webbrowser
from button import Button
from Window import Window
pygame.init()
import Preferences


class Rules(Window):
    
    def __init__(self, surface) -> None:
        self.running = True
        self.action = 0
        self.link_font = pygame.font.SysFont('Comic Sans MS', 24)
        self.link_color = (0,0,0)
        self.rect = pygame.Rect(0,0,0,0)
        rect : pygame.Rect = surface.get_rect()
        rb = pygame.image.load('Images/return-arrow.png')
        self.button = Button((rect.topright[0] - 100, rect.topright[1] + 30,70,70), (27, 128, 42, 100), self.openMenu
                             , **Preferences.BUTTON_STYLE, texture=rb)
    
    
    def blit_text(surface, text, pos, font, color):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width - 100: #Right border!!!
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
    
    
    
    def check(self, events):
        for event in events:
            self.button.check_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if self.rect.collidepoint(pos):
                    webbrowser.open(r"https://ru.wikipedia.org/wiki/%D0%9F%D1%83%D0%BB-8")
                    
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.link_color = (70, 29, 219)

        else:
            self.link_color = (0, 0, 0)
            
    def callback(self):
        r = self.action
        self.action = 0
        return r
    
    def openMenu(self):
        self.action = 'menu'
        
    def draw(self, screen):
        ground = pygame.image.load("Images/summer.png")
        ground = pygame.transform.smoothscale(ground, screen.get_size())

        text_1 = "Для начала вспомним правила классического бильярда-восьмёрка (pool-8): \n \nТак же команда разработчиков добавила дополнительные режимы: \n1. Классичаский режим \n2. Пониженный коэффицент трения (Лёд) \n3. Повышенный коэффицент трения (Клей) \n4. Абсолютно упругие соударения (резиновые мачики) \n5. Неупругие соударения (пластелиновые мячики) \nИгрок может менять их на своё усмотрение, как перед ударом, так и в процессе движения шаров."
        font_1 = pygame.font.SysFont('Comic Sans MS', 24)


        screen.fill((255, 255, 255))
        screen.blit(ground, [0, 0])
        self.rect = screen.blit(self.link_font.render("Основные правила на Wikipedia", True, self.link_color), (10, 44)) #control
        
        Rules.blit_text(screen, text_1, (10, 10), font_1, (0, 0, 0))
        self.button.update(screen)
        
            
        
if(__name__ =='__main__'):
        
    show = False
    clock = pygame.time.Clock()
    running = True
    
    SIZE = (1024, 720)
    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
    rs = Rules(screen)
    while running and running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        rs.draw(screen)
        rs.check(events)
        pygame.display.update()

    pygame.quit()
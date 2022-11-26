import pygame
import Preferences
from button import Button
    
class Menu:
    
    def __init__(self, screen : pygame.Surface) -> None:
        self.action = 0
        self.screen = screen
        rect = screen.get_rect() 
        width = 650
        height = 60
        paddings = 20
        self.button = []
        self.button.append(Button((rect.center[0], rect.center[1],width,height), (27, 128, 42, 100), self.doNothing,
                             text='Играть', **Preferences.BUTTON_STYLE))
        self.button.append(Button((rect.center[0], rect.center[1],width,height), (27, 128, 42, 100), self.doNothing,
                             text='Настройки', **Preferences.BUTTON_STYLE))
        self.button.append(Button((rect.center[0], rect.center[1],width,height), (27, 128, 42, 100), self.openAuthors,
                             text='Авторы', **Preferences.BUTTON_STYLE))
        self.button.append(Button((rect.center[0], rect.center[1],width,height), (27, 128, 42, 100), exit,
                             text='Выход', **Preferences.BUTTON_STYLE))
        self.gameName = pygame.font.Font("Roboto-Regular.ttf", 76).render("The_BBbW", True, (230, 230, 230))
        center = rect.center
        for i in range(0, len(self.button)):
            cx = center[0]
            cy = center[1] - (height + paddings) * (len(self.button)*0.5 - i - 0.5) + 50
            self.button[i].rect.center = (cx, cy)
        self.bg = pygame.image.load("Images/dark-green-texture.jpg")
    
    
    def check(self, event):
        for b in self.button:
            b.check_event(event)
        
    def draw(self):
        self.screen.blit(self.bg, (0,0))
        s = pygame.Surface((Preferences.WIDTH, Preferences.HEIGHT), pygame.SRCALPHA)
        for b in self.button:
            b.update(s)
        self.screen.blit(s, (0, 0))
        vc = self.gameName.get_rect(center = self.screen.get_rect().center)
        vc[1] -= 200
        self.screen.blit(self.gameName, vc)
        
    def callback(self):
        return self.action
        
    def openAuthors(self):
        self.action = 'authors'
    def doNothing(self):
        pass
    
    

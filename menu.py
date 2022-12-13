import pygame
import Preferences
from button import Button
from Window import Window

class Menu(Window):
    
    def __init__(self, screen : pygame.Surface) -> None:
        self.action = 0
        self.screen = screen
        rect = screen.get_rect() 
        width = 650
        height = 60
        paddings = 20
        self.button = []
        self.button.append(Button((rect.center[0], rect.center[1],width,height), (27, 128, 42, 100), self.openGame,
                             text='Играть', **Preferences.BUTTON_STYLE))
        self.button.append(Button((rect.center[0], rect.center[1],width,height), (27, 128, 42, 100), self.openRules,
                             text='Правила', **Preferences.BUTTON_STYLE))
        self.button.append(Button((rect.center[0], rect.center[1],width,height), (27, 128, 42, 100), self.openAuthors,
                             text='Авторы', **Preferences.BUTTON_STYLE))
        self.button.append(Button((rect.center[0], rect.center[1],width,height), (27, 128, 42, 100), exit,
                             text='Выход', **Preferences.BUTTON_STYLE))
        self.gameName = pygame.font.Font('Caveat-VariableFont_wght.ttf', 76).render("GOOD MORNING", True, (230, 230, 230))
        center = rect.center
        for i in range(0, len(self.button)):
            cx = center[0]
            cy = center[1] - (height + paddings) * (len(self.button)*0.5 - i - 0.5) + 50
            self.button[i].rect.center = (cx, cy)
        self.bg = pygame.image.load("Images/dark-green-texture.jpg")
    
    
    def check(self, events):
        for event in events:
            for b in self.button:
                b.check_event(event)
        
    def draw(self, surface):
        surface.blit(self.bg, (0,0))
        s = pygame.Surface((Preferences.WIDTH, Preferences.HEIGHT), pygame.SRCALPHA)
        for b in self.button:
            b.update(s)
        surface.blit(s, (0, 0))
        vc = self.gameName.get_rect(center = surface.get_rect().center)
        vc[1] -= 200
        surface.blit(self.gameName, vc)
        
    def callback(self):
        r = self.action
        self.action = 0
        return r
        
    def openAuthors(self):
        self.action = 'authors'
        
    def openGame(self):
        self.action = 'game'
    def doNothing(self):
        pass
    def openRules(self):
        self.action = 'rules'
    
    

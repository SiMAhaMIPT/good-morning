import pygame

pygame.init()

from menu import Menu
from Authors import Authors
from windowManager import Windows
import Preferences

surface = pygame.display.set_mode((Preferences.WIDTH,Preferences.HEIGHT))

wManager = Windows()
wManager.add('menu', Menu(surface))
wManager.add('authors', Authors(surface))

while True:
    events = pygame.event.get()
    for event in events:
        wManager.get_window().check(event)
        
        if event.type == pygame.QUIT:
            exit()
    
    wManager.get_window().draw()
    wManager.open_window(wManager.get_window().callback())
    pygame.display.update()

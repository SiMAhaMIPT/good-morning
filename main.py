import pygame

pygame.init()

from GameWindow import gameWindow
from menu import Menu
from Authors import Authors
from windowManager import Windows
from Rules import Rules
import graphics

canvas = graphics.Canvas()

surface = canvas.surface#pygame.display.set_mode((Preferences.WIDTH,Preferences.HEIGHT))
wManager = Windows()
print("Hello")
wManager.add('menu', Menu(surface))
wManager.add('authors', Authors(surface))
wManager.add('game', gameWindow(canvas))
wManager.add("rules", Rules(surface))
#surface = pygame.display.set_mode((Preferences.WIDTH,Preferences.HEIGHT))
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
            
    wManager.get_window().check(events)
    wManager.get_window().draw(surface)
    wManager.open_window(wManager.get_window().callback())
    pygame.display.update()
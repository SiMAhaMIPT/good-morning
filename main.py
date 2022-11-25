import pygame

pygame.init()

from menu import Menu
import Preferences

surface = pygame.display.set_mode((Preferences.WIDTH,Preferences.HEIGHT))
menu = Menu(surface)
while True:
    events = pygame.event.get()
    for event in events:
        menu.check(event)
        
        if event.type == pygame.QUIT:
            exit()

    menu.draw()
    pygame.display.update()

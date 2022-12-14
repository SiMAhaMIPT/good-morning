import numpy as np
import pygame

class GameEvent():
    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data

def set_allowed_events():
    # разрешать только события нажатия клавиш, чтобы не перегружать тип процессора при проверке бесполезных событий
    pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
    pass

def events_m(events):
    closed = False
    quit = False

    for event in events:
        if event.type == pygame.QUIT:
            closed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit = True

    return {"quit_to_main_menu": quit,
            "closed": closed,
            "clicked": pygame.mouse.get_pressed()[0],
            "mouse_pos": np.array(pygame.mouse.get_pos())}

def events():
    closed = False
    quit = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit = True

    return {"quit_to_main_menu": quit,
            "closed": closed,
            "clicked": pygame.mouse.get_pressed()[0],
            "mouse_pos": np.array(pygame.mouse.get_pos())}
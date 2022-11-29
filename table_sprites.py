import numpy as np
import pygame

import config
import Game

class Hole(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(
            (2 * config.hole_radius, 2 * config.hole_radius))

        self.image.fill((200, 200, 200))
        self.image.set_colorkey((200, 200, 200))

        pygame.draw.circle(self.image, (0, 0, 0),
                           (config.hole_radius, config.hole_radius), config.hole_radius, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.pos = np.array([x, y])

# этот класс содержит свойства TableSide line, но не рисует его
class TableSide():
    def __init__(self, line):
        self.line = np.array(line)
        self.middle = (self.line[0] + self.line[1]) / 2
        self.size = np.round(np.abs(self.line[0] - self.line[1]))
        self.length = np.hypot(*self.size)
        if np.count_nonzero(self.size) != 2:
            # line is perpendicular to y or x axis
            if self.size[0] == 0:
                self.size[0] += 1
            else:
                self.size[1] += 1

# draws the yellow part of the table
class TableColoring(pygame.sprite.Sprite):
    def __init__(self, table_size, color, table_points):
        pygame.sprite.Sprite.__init__(self)
        self.points = table_points
        self.image = pygame.Surface(table_size)
        self.image.fill(color)
        color_key = (200, 200, 200)
        self.image.set_colorkey(color_key)
        pygame.draw.polygon(self.image, color_key, table_points)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.font = config.get_default_font(config.ball_radius)



    def redraw(self):
        self.image.fill(config.table_side_color)
        color_key = (200, 200, 200)
        self.image.set_colorkey(color_key)
        pygame.draw.polygon(self.image, color_key, self.points)

    def update(self, game_state):
        self.redraw()


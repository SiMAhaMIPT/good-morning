from abc import ABCMeta, abstractmethod
import pygame
class Window(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def draw(self, surface:pygame.Surface):
        pass
    @abstractmethod
    def check(self, event):
        pass
    @abstractmethod
    def callback(self):
        pass
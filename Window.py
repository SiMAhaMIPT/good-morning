from abc import ABCMeta, abstractmethod
import pygame

#abstract class for all windows
class Window(object):
    __metaclass__ = ABCMeta
    
    #method for drawing window
    @abstractmethod
    def draw(self, surface:pygame.Surface):
        pass
    #method for passing event to window
    @abstractmethod
    def check(self, event):
        pass
    
    #method to get output from window
    @abstractmethod
    def callback(self):
        pass
    
    #is called each time the window was opened
    def openWindow(self):
        return self
import pygame
import event
import Game
import graphics
import config
import physics
from button import Button
from Window import Window
import inventory
if(__name__=='__main__'):
    pygame.init()
import Preferences
class gameWindow(Window):
    def __init__(self, canvas):
        self.game = Game.GameState(canvas)
        self.game.start_pool()
        self.state = 0
        self.action = 0
        self.events = event.events()
        rb = pygame.image.load('Images/return-arrow.png')
        rect : pygame.Rect = canvas.surface.get_rect()
        self.buttons = list()
        self.buttons.append(Button((rect.topright[0] - 170, rect.topright[1] + 15,40,40), (27, 128, 42, 100), inventory.glue
                , **Preferences.BUTTON_STYLE, texture=rb))
        self.buttons.append(Button((rect.topright[0] - 230, rect.topright[1] + 15,40,40), (27, 128, 42, 100), inventory.ice
                , **Preferences.BUTTON_STYLE, texture=rb))
        self.buttons.append(Button((rect.topright[0] - 290, rect.topright[1] + 15,40,40), (27, 128, 42, 100), inventory.standart_friction
                , **Preferences.BUTTON_STYLE, texture=rb))
        self.buttons.append(Button((rect.topright[0] - 350, rect.topright[1] + 15,40,40), (27, 128, 42, 100), inventory.inelastic_col
                , **Preferences.BUTTON_STYLE, texture=rb))
        self.buttons.append(Button((rect.topright[0] - 410, rect.topright[1] + 15,40,40), (27, 128, 42, 100), inventory.elastic_col
                , **Preferences.BUTTON_STYLE, texture=rb))
    
    def draw(self, surf):
        ns = self.game.all_not_moving()
        if self.state == 0 and ns == 1:
            self.game.cue.make_visible(self.game.current_player)
            self.game.check_pool_rules()
            
        if self.state == 0 or self.state == 1:
            self.state = ns
        game = self.game
        if self.state == 0:
            physics.resolve_all_collisions(game.balls, game.holes, game.table_sides)
            game.redraw_all(False)
        elif self.state == 1:
            game.redraw_all(False)
            if game.cue.is_clicked(self.events):
                self.state = 2
                game.cue.set_up_cue(game, self.events)
                #game.cue.cue_is_active(game, self.events)
            elif game.can_move_white_ball and game.white_ball.is_clicked(self.events):
                self.state = 3
                #print("Muu")
                game.white_ball.set_up(game, game.is_behind_line_break())
                #game.white_ball.is_active(game, game.is_behind_line_break())
        elif self.state == 2:
            #game.cue.cue_is_active(game, self.events)
            if not(game.cue.update_check_cue(game, self.events)):
                self.state = 1
                game.cue.clean_up_cue(game,self.events)
        elif self.state == 3:
            if not(game.white_ball.update_check(game,self.events, game.is_behind_line_break())):#is_active(game, game.is_behind_line_break())
                self.state = 1
                game.white_ball.clean_up(game, game.is_behind_line_break())
            
        for b in self.buttons:
            b.update(surf)
        
        
        
    def openWindow(self):
        self.game.start_pool()
        return self
    
    def check(self, ev):
        for eve in ev:
            
            for b in self.buttons:
                b.check_event(eve)
        self.events = event.events_m(ev)
        pass
        
    
        
    def callback(self):
        if self.events['quit_to_main_menu']:
            self.action = 'menu'
        r = self.action
        self.action = 0
        if self.events['closed']:
            exit()
        return r
        
    def doNothing(self):
        print("hell")
        
if(__name__=='__main__'):
    canvas = graphics.Canvas()
    gp = gameWindow(canvas)
    while True:
        events = event.events() 
        if(events['closed']):
            exit()
        gp.check(pygame.event.get())
        gp.draw(canvas.surface)
        pygame.display.update()

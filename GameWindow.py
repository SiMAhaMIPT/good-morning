import pygame
import event
import Game
import graphics
import config
import physics
from Window import Window
class gameWindow(Window):
    def __init__(self, canvas):
        self.game = Game.GameState(canvas)
        self.game.start_pool()
        self.state = 0
        self.action = 0
        self.events = event.events()
    
    
    def draw(self, surf):
        ns = self.game.all_not_moving()
        if self.state == 0 and ns == 1:
            self.game.cue.make_visible(self.game.current_player)
            self.game.check_pool_rules()
            
        self.state = ns
        
        game = self.game
        if self.state == 0:
            physics.resolve_all_collisions(game.balls, game.holes, game.table_sides)
            game.redraw_all()
        elif self.state == 1:
            game.redraw_all()
            if game.cue.is_clicked(self.events):
                game.cue.cue_is_active(game, self.events)
            elif game.can_move_white_ball and game.white_ball.is_clicked(self.events):
                game.white_ball.is_active(game, game.is_behind_line_break())
            
        
    def openWindow(self):
        self.game.start_pool()
        return self
    
    def check(self, ev):
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
        
        
if(__name__=='__main__'):
    pygame.init()
    canvas = graphics.Canvas()
    gp = gameWindow(canvas)
    while True:
        events = event.events() 
        if(events['closed']):
            exit()
        gp.check(pygame.event.get())
        gp.draw(None)
        pygame.display.update()

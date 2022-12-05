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
    
    
    def draw(self, surf):
        ns = self.game.all_not_moving()
        if self.state == 0 and ns == 1:
            self.game.cue.make_visible(self.game.current_player)
            self.game.check_pool_rules()
            
        self.state = ns
        
        game = self.game
        if self.state == 0:
            #print('fine')
            physics.resolve_all_collisions(game.balls, game.holes, game.table_sides)
            game.redraw_all()
        elif self.state == 1:
            #print('np')
            game.redraw_all()
            events = event.events()
            if game.cue.is_clicked(events):
                game.cue.cue_is_active(game, events)
            elif game.can_move_white_ball and game.white_ball.is_clicked(events):
                game.white_ball.is_active(game, game.is_behind_line_break())
            
        
    def openWindow(self):
        self.game.start_pool()
        return self
    
    def check(self, ev):
            pass
        
        
    def callback(self):
        ev = event.events()
        if ev['quit_to_main_menu']:
            self.action = 'menu'
        r = self.action
        self.action = 0
        return r
        
        
if(__name__=='__main__'):
    pygame.init()
    gp = gameWindow()
    while True:
        events = event.events() 
        if(events['closed']):
            exit()
        gp.check(events)
        gp.draw(None)
        pygame.display.update()

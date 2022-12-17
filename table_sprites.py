import numpy as np
import pygame
import cue
import config
import Game
import event


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

        if self.size[0] == 0:
            self.size[0] += 1
        else:
            self.size[1] += 1


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
        self.target_ball_text = [self.font.render(config.player1_target_text, False, config.cue_color_standart),
                                 self.font.render(config.player2_target_text, False, config.cue_color_elastic)]




    def redraw(self):
        self.image.fill(config.table_side_color)
        color_key = (200, 200, 200)
        self.image.set_colorkey(color_key)
        pygame.draw.polygon(self.image, color_key, self.points)

    def update(self, game_state):
        self.redraw()
        self.generate_top_left_label(game_state)
        self.generate_target_balls(game_state)

    def generate_top_left_label(self, game_state):
        # generates the top left label (чей сейчас ход, и может ли он передвинуть мяч)
        top_left_text = ""
        if game_state.can_move_white_ball:
            top_left_text += config.penalty_indication_text
        if game_state.current_player.value == 1:
            top_left_rendered_text = self.font.render(config.player1_turn_label + top_left_text,
                                                      False, config.cue_color_standart)
        else:
            top_left_rendered_text = self.font.render(config.player2_turn_label + top_left_text,
                                                      False, config.cue_color_elastic)
        text_pos = [config.table_margin + config.hole_radius * 3,
                    config.table_margin - self.font.size(top_left_text)[1] / 2]
        self.image.blit(top_left_rendered_text, text_pos)

    def generate_target_balls(self, game_state):
        if game_state.ball_assignment is not None:
            start_x = np.array([config.table_margin + config.hole_radius * 3,
                                config.resolution[0] / 2 + config.hole_radius * 3])
            start_y = config.resolution[1] - config.table_margin - self.font.size(config.player1_target_text)[1] / 2
            # the text needs to be moved a bit lower to keep it aligned
            self.image.blit(self.target_ball_text[0], [start_x[0], start_y + config.ball_radius / 2])
            self.image.blit(self.target_ball_text[1], [start_x[1], start_y + config.ball_radius / 2])
            start_x += self.font.size(config.player2_target_text)[0]
            for ball in game_state.balls:
                do_draw = ball.number != 0 and ball.number != 8

                # draw to player holds the players which the balls will be added to
                draw_to_player = []

                # sorts the balls into their places
                if do_draw:
                    if game_state.ball_assignment[Game.Player.Player1] == ball.ball_type:
                        draw_to_player.append(1)
                    else:
                        draw_to_player.append(2)

                if ball.number == 8:
                    if game_state.potting_8ball[Game.Player.Player1]:
                        draw_to_player.append(1)
                    if game_state.potting_8ball[Game.Player.Player2]:
                        draw_to_player.append(2)

                # draws the balls
                for i in draw_to_player:
                    # i-1 because lists start with 0
                    ball.create_image(self.image, (start_x[i - 1], start_y))
                    start_x[i - 1] += config.ball_radius * 2 + config.target_ball_spacing












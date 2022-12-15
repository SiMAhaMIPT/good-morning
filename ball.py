import itertools
import math
from enum import Enum

import numpy as np
import pygame


import config
import event
import physics

class Ball():
    def __init__(self):
        self.pos = np.zeros(2, dtype=float)
        self.velocity = np.zeros(2, dtype=float)
        self.surface=0


    def apply_force(self, force, time=1):
        self.velocity += (force / config.ball_mass) * time

    def set_velocity(self, new_velocity):
        self.velocity = np.array(new_velocity, dtype=float)

    def move_to(self, pos):
        self.pos = np.array(pos, dtype=float)

    def update(self, *args):
        self.velocity *= (config.friction_coeff)
        self.pos += self.velocity
        # Если скорость меньше config.friction_threshold, скорость=0
        if np.hypot(*self.velocity) < config.friction_threshold:
            self.velocity = np.zeros(2)

    def check_surface(self):
        if self.surface==0:
            add_friction=0

class BallType(Enum):
    Striped = "striped"
    Solid = "solid"

class StripedBall():

    def __init__(self):
        # каждая точка является трехмерной координатой на шаре


        point_num = config.ball_stripe_point_num
        self.stripe_circle = config.ball_radius * np.column_stack((np.sin(np.linspace(0, 2 * np.pi, point_num)),
                                                                   np.cos(np.linspace(
                                                                       0, 2 * np.pi, point_num)),
                                                                   np.zeros(point_num)))

    def update_stripe(self, transformation_matrix):
        for i, stripe in enumerate(self.stripe_circle):
            self.stripe_circle[i] = np.matmul(stripe, transformation_matrix)

    def draw_stripe(self, sprite,stripe_color):
        for num, point in enumerate(self.stripe_circle[:-1]):
            if point[2] >= -1:
                pygame.draw.line(sprite, stripe_color, config.ball_radius + point[:2],
                                 config.ball_radius + self.stripe_circle[num + 1][:2], config.ball_stripe_thickness)


class SolidBall():
    def __init__(self):
        # каждая точка является трехмерной координатой на шаре

        point_num = config.ball_stripe_point_num
        self.stripe_circle = config.ball_radius * np.column_stack((np.sin(np.linspace(0, 2 * np.pi, point_num)),
                                                                   np.cos(np.linspace(
                                                                       0, 2 * np.pi, point_num)),
                                                                   np.zeros(point_num)))

    def update_stripe(self, transformation_matrix):
        for i, stripe in enumerate(self.stripe_circle):
            self.stripe_circle[i] = np.matmul(stripe, transformation_matrix)

    def draw_stripe(self, sprite,stripe_color=(255,255,255)):
        for num, point in enumerate(self.stripe_circle[:-1]):
            if point[2] >= -1:
                pygame.draw.line(sprite, (255,255,255), config.ball_radius + point[:2],
                                 config.ball_radius + self.stripe_circle[num + 1][:2], config.ball_stripe_thickness)

class BallSprite(pygame.sprite.Sprite):

    def __init__(self, ball_number):
        self.number = ball_number
        self.color = config.ball_colors[ball_number]
        self.stripe_color=config.stripe_colors[ball_number]
        if ball_number <= 8:
            self.ball_type = BallType.Solid
            self.ball_stripe = SolidBall()
        else:
            self.ball_type = BallType.Striped
            self.ball_stripe = StripedBall()
        self.ball = Ball()
        pygame.sprite.Sprite.__init__(self)
        self.label_offset = np.array([0, 0, config.ball_radius])
        self.label_size = config.ball_radius // 2

        self.update_sprite()
        self.update()
        self.top_left = self.ball.pos - config.ball_radius
        self.rect.center = self.ball.pos.tolist()

    def update(self, *args):
        if np.hypot(*self.ball.velocity) != 0:
            # updates label circle and number offset
            perpendicular_velocity = -np.cross(self.ball.velocity, [0, 0, 1])
            # angle formula is angle=((ballspeed*2)/(pi*r*2))*2
            rotation_angle = -np.hypot(
                *(self.ball.velocity)) * 2 / (config.ball_radius * np.pi)
            transformation_matrix = physics.get_rotation_matrix(
                perpendicular_velocity, rotation_angle)
            self.label_offset = np.matmul(
                self.label_offset, transformation_matrix)
            ## здесь происходит, переотрисовка полос, делаю наши шары обьемными
            if self.ball_type == BallType.Striped:
                self.ball_stripe.update_stripe(transformation_matrix)

            if self.ball_type == BallType.Solid:
                self.ball_stripe.update_stripe(transformation_matrix)



            self.update_sprite()
            self.ball.update()

    def update_sprite(self):
        sprite_dimension = np.repeat([config.ball_radius * 2], 2)
        new_sprite = pygame.Surface(sprite_dimension)
        colorkey = (200, 200, 200)
        new_sprite.fill(self.color)
        new_sprite.set_colorkey(colorkey)


        if self.ball_type == BallType.Striped:

            stripe_color=self.stripe_color
            self.ball_stripe.draw_stripe(new_sprite,stripe_color)
        if self.ball_type == BallType.Solid:
            #stripe_color=self.stripe_color
            #self.ball_stripe.draw_stripe(new_sprite,stripe_color)
            self.ball_stripe.draw_stripe(new_sprite)

        grid_2d = np.mgrid[-config.ball_radius:config.ball_radius +1, -config.ball_radius:config.ball_radius + 1]
        is_outside = config.ball_radius < np.hypot(*grid_2d)

        for xy in itertools.product(range(config.ball_radius * 2 + 1), repeat=2):
            if is_outside[xy]:
                new_sprite.set_at(xy, colorkey)

        self.image = new_sprite
        self.rect = self.image.get_rect()
        self.top_left = self.ball.pos - config.ball_radius
        self.rect.center = self.ball.pos.tolist()

    def create_image(self, surface, coords):
        surface.blit(self.image, coords)

    def is_clicked(self, events):
        return physics.distance_less_equal(events["mouse_pos"], self.ball.pos, config.ball_radius)

    def move_to(self, pos):
        self.ball.move_to(pos)
        self.rect.center = self.ball.pos.tolist()


    def set_up(self,game_state, behind_separation_line=False):
        game_state.cue.make_invisible()
        
    def clean_up(self,game_state, behind_separation_line=False):
        game_state.cue.make_visible(game_state.current_player)
        
    def update_check(self,game_state, events, behind_separation_line=False):
        if(events["clicked"]):
            if np.all(np.less(config.table_margin + config.ball_radius + config.hole_radius, events["mouse_pos"])) and \
                    np.all(np.greater(config.resolution - config.table_margin - config.ball_radius - config.hole_radius,
                                        events["mouse_pos"])) and \
                    not physics.check_if_ball_touches_balls(events["mouse_pos"], self.number, game_state.balls):
                if behind_separation_line:
                    if events["mouse_pos"][0] <= config.white_ball_initial_pos[0]:
                        self.move_to(events["mouse_pos"])
                else:
                    self.move_to(events["mouse_pos"])
            game_state.redraw_all(False)
        
        return events["clicked"]

    def is_active(self, game_state, behind_separation_line=False):
        game_state.cue.make_invisible()
        events = event.events()

        while events["clicked"]:
            events = event.events()
            # проверяет, не пытается ли пользователь поместить шар за пределы стола или внутрь другого шара

            if np.all(np.less(config.table_margin + config.ball_radius + config.hole_radius, events["mouse_pos"])) and \
                    np.all(np.greater(config.resolution - config.table_margin - config.ball_radius - config.hole_radius,
                                      events["mouse_pos"])) and \
                    not physics.check_if_ball_touches_balls(events["mouse_pos"], self.number, game_state.balls):
                if behind_separation_line:
                    if events["mouse_pos"][0] <= config.white_ball_initial_pos[0]:
                        self.move_to(events["mouse_pos"])
                else:
                    self.move_to(events["mouse_pos"])
            game_state.redraw_all()
        game_state.cue.make_visible(game_state.current_player)
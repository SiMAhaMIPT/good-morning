import math
import numpy as np
import pygame
# шрифты должны быть инициализированы перед использованием
def get_default_font(size):
    font_defualt = pygame.font.get_default_font()
    return pygame.font.Font(font_defualt, size)

def set_max_resolution():
    infoObject = pygame.display.Info()
    global resolution
    global white_ball_initial_pos

    resolution = np.array([infoObject.current_w, infoObject.current_h])
    white_ball_initial_pos = (resolution + [table_margin + hole_radius, 0]) * [0.25, 0.5]

# window settings
fullscreen = False
# полноэкранное разрешение можно узнать только после инициализации экрана
if not fullscreen:
    resolution = np.array([1024, 720])
window_caption = "Pool"
fps_limit = 60

# table settings
HEIGHT = 700
WIDTH = 1000
table_margin = 100
table_side_color = 	(90, 32, 8)
table_color_ice=(196, 216, 255)
table_color_glue=(247, 178, 57)
table_color_standart=(40, 150, 75)
table_color = table_color_standart
separation_line_color = (255, 255, 255)
hole_radius = 20
middle_hole_offset = np.array([[-hole_radius * 2, hole_radius], [-hole_radius, 0],
                               [hole_radius, 0], [hole_radius * 2, hole_radius]])
side_hole_offset = np.array([
    [- 2 * math.cos(math.radians(45)) * hole_radius - hole_radius, hole_radius],
    [- math.cos(math.radians(45)) * hole_radius, -math.cos(math.radians(45)) * hole_radius],
    [math.cos(math.radians(45)) * hole_radius, math.cos(math.radians(45)) * hole_radius],
    [- hole_radius, 2 * math.cos(math.radians(45)) * hole_radius + hole_radius]
    ])

# cue settings
cue_color_standart = (200, 100, 0)
cue_color_elastic = (0, 200, 200)
cue_color_inelastic = (0, 0, 0)
cue_color=cue_color_standart

cue_hit_power = 3
cue_length = 250
cue_thickness = 4
cue_max_displacement = 100
# safe displacement is the length the cue stick can be pulled before
# causing the ball to move
cue_safe_displacement = 1
aiming_line_length = 14

# ball settings
total_ball_num = 16
ball_radius = 14
ball_mass = 14
speed_angle_threshold = 0.09
visible_angle_threshold = 0.05
ball_colors = [
    (255, 255, 255),
    (0, 200, 200),
    (0, 0, 200),
    (150, 0, 0),
    (200, 0, 200),
    (200, 0, 0),
    (50, 60, 120),
    (100, 0, 0),
    (0, 0, 0),
    (255, 255, 255),
    (255, 255, 255),
    ((255, 255, 255)),
    (255, 255, 255),
    (255, 255, 255),
    (255, 255, 255),
    (255, 255, 255)
]
stripe_colors=[
    (255,200,100),
    (0, 200, 200),
    (0, 0, 200),
    (150, 0, 0),
    (200, 0, 200),
    (200, 0, 0),
    (50, 60, 120),
    (100, 0, 0),
    (0, 0, 0),
    (0, 200, 200),
    (0, 0, 200),
    (150, 0, 0),
    (200, 0, 200),
    (200, 0, 0),
    (50, 60, 120),
    (100, 0, 0)

]
ball_stripe_thickness = 5
ball_stripe_point_num = 25
# Начальное положение шаров
ball_starting_place_ratio = [0.75, 0.5]
# in fullscreen mode the resolution is only available after initialising the screen
# and if the screen wasn't initialised the resolution variable won't exist
if 'resolution' in locals():
    white_ball_initial_pos = (resolution + [table_margin + hole_radius, 0]) * [0.25, 0.5]
ball_label_text_size = 10

# physics
# Если скорость меньше friction_threshold, остановка
friction_threshold = 0.06
friction_coeff = 0.99
# 1 - perfectly elastic ball collisions(Упругое столкновение)
# 0 - perfectly inelastic collisions(Неупругое столкновение)
# coeff_of_restitution- коэф отношение конечной относительной скорости к начальной, т.е. могут быть расмотрены ситуации не абсолютно упругого столкновения
ball_coeff_of_restitution = 0.9
table_coeff_of_restitution = 0.9

# in-game ball target variables
player1_target_text = 'P1 balls - '
player2_target_text = 'P2 balls - '
target_ball_spacing = 3
player1_turn_label = "Player 1 turn"
player2_turn_label = "Player 2 turn"
penalty_indication_text = " (click on the ball to move it)"
game_over_label_font_size = 40

BUTTON_STYLE = {"hover_color" : (20, 102, 33, 120),
                "clicked_color" : (54, 156, 70, 150),
                "clicked_font_color" : (40, 40, 40),
                "font" : pygame.font.Font('Caveat-VariableFont_wght.ttf',28)
}
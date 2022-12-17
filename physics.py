import math
import numpy as np
import event
import config
import zope.event
import itertools
import random

def point_distance(p1, p2):
    dist_diff = p1 - p2
    #np.hypot Equivalent to sqrt(x1**2 + x2**2)
    return np.hypot(*dist_diff)
def distance_less_equal(p1, p2, dist):
    # делает сравнения расстояний без вычисления квадратных корней
    dist_diff = p1 - p2
    return (dist_diff[0] ** 2 + dist_diff[1] ** 2) <= dist ** 2

def ball_collision_check(ball1, ball2):
    # проверка расстояния с последующей проверкой того, движется ли какой-либо из шаров
    # с последующей проверкой векторной проекции, чтобы увидеть, движутся ли оба к друг к другу
    return distance_less_equal(ball1.pos, ball2.pos, 2 * config.ball_radius) and \
           np.count_nonzero(np.concatenate((ball1.velocity, ball2.velocity))) > 0 and \
           np.dot(ball2.pos - ball1.pos, ball1.velocity - ball2.velocity) > 0

def collide_balls(ball1, ball2):
    point_diff = ball2.pos - ball1.pos
    dist = point_distance(ball1.pos, ball2.pos)

    collision = point_diff / dist
    # проекция скорости шариков на вектор разности
    ball1_dot = np.dot(ball1.velocity, collision)
    ball2_dot = np.dot(ball2.velocity, collision)
    # так как массы шариков одинаковые, скорость просто поменяется (из Законов сохранения)
    ball1.velocity += (ball2_dot - ball1_dot) * collision * 0.5*(1+config.ball_coeff_of_restitution)
    ball2.velocity += (ball1_dot - ball2_dot) * collision * 0.5*(1+config.ball_coeff_of_restitution)
def get_rotation_matrix(axis, theta):
    """
    Args:
        axis (list): rotation axis of the form [x, y, z]
        theta (float): rotational angle in radians

    Returns:
        array. Rotation matrix.
    """
    axis = np.asarray(axis)
    theta = np.asarray(theta)
    axis = axis/math.sqrt(np.dot(axis, axis))
    a = math.cos(theta/2.0)
    b, c, d = -axis*math.sin(theta/2.0)
    aa, bb, cc, dd = a*a, b*b, c*c, d*d
    bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
    return np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
                     [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
                     [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])

def triangle_area(side1, side2, side3):
    # используется, чтобы определить, нажимает ли пользователь на cue
    # herons formula
    half_perimetre = abs((side1 + side2 + side3) * 0.5)
    return math.sqrt(half_perimetre * (half_perimetre - abs(side1)) * (half_perimetre - abs(side2)) * (
            half_perimetre - abs(side3)))

def resolve_all_collisions(balls, holes, table_sides):
    # уничтожает все круги, которые находятся в дыре

    for ball_hole_combination in itertools.product(balls, holes):
        if distance_less_equal(ball_hole_combination[0].ball.pos, ball_hole_combination[1].pos, config.hole_radius):
            zope.event.notify(event.GameEvent("POTTED", ball_hole_combination[0]))

    # сталкивает шарики со столом там, где это необходимо
    for line_ball_combination in itertools.product(table_sides, balls):
        if line_ball_collision_check(line_ball_combination[0], line_ball_combination[1].ball):
            collide_line_ball(line_ball_combination[0], line_ball_combination[1].ball)


    ball_list = balls.sprites()
    # ball list перемешивается для рандомизации столкновений мячей в первый раз
    random.shuffle(ball_list)

    for ball_combination in itertools.combinations(ball_list, 2):
        if ball_collision_check(ball_combination[0].ball, ball_combination[1].ball):
            collide_balls(ball_combination[0].ball, ball_combination[1].ball)
            zope.event.notify(event.GameEvent("COLLISION", ball_combination))

def check_if_ball_touches_balls(target_ball_pos, target_ball_number, balls):
    touches_other_balls = False
    for ball in balls:
        if target_ball_number != ball.number and \
                distance_less_equal(ball.ball.pos, target_ball_pos, config.ball_radius * 2):
            touches_other_balls = True
            break
    return touches_other_balls

def line_ball_collision_check(line, ball):
    # checks if the ball is half the line length from the line middle
    if distance_less_equal(line.middle, ball.pos, line.length / 2 + config.ball_radius):
        # displacement vector от первой точки к шарику
        displacement_to_ball = ball.pos - line.line[0]
        # displacement vector из первой точки во вторую точку на line

        displacement_to_second_point = line.line[1] - line.line[0]
        normalised_point_diff_vector = displacement_to_second_point / \
                                       np.hypot(*(displacement_to_second_point))
        # distance from the first point on the line to the perpendicular
        # projection point from the ball
        projected_distance = np.dot(normalised_point_diff_vector, displacement_to_ball)
        # closest point on the line to the ball
        closest_line_point = projected_distance * normalised_point_diff_vector
        perpendicular_vector = np.array(
            [-normalised_point_diff_vector[1], normalised_point_diff_vector[0]])
        #проверка, действительно ли ближайшая точка на линии находится на линии (что не всегда имеет место при проецировании)
        #затем проверяем, меньше ли расстояние от этой точки до шара, чем радиус шара и, наконец,
        #проверяем, движется ли шарик к линии со скалярным произведением
        return -config.ball_radius / 3 <= projected_distance <= \
               np.hypot(*(displacement_to_second_point)) + config.ball_radius / 3 and \
               np.hypot(*(closest_line_point - ball.pos + line.line[0])) <= \
               config.ball_radius and np.dot(
            perpendicular_vector, ball.velocity) <= 0

def collide_line_ball(line, ball):
    displacement_to_second_point = line.line[1] - line.line[0]
    normalised_point_diff_vector = displacement_to_second_point / \
                                   np.hypot(*(displacement_to_second_point))
    perpendicular_vector = np.array(
        [-normalised_point_diff_vector[1], normalised_point_diff_vector[0]])
    ball.velocity -= 2 * np.dot(perpendicular_vector,ball.velocity) * \
                     perpendicular_vector * 0.5*(1+config.table_coeff_of_restitution)
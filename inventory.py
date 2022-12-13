import config
import graphics

def ice():
    config.friction_coeff=0.9999
def clue():
    config.friction_coeff=0.8
    config.table_color =config.table_color_ice
def standart_friction():
    config.friction_coeff=0.99
    config.table_color=config.table_color_standart

def inelastic_col():
    config.ball_coeff_of_restitution=0

def elastic_col():
    config.ball_coeff_of_restitution=1

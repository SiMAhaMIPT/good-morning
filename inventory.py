import config
import graphics
import cue
def ice():
    config.friction_coeff=0.9999
    config.table_color =config.table_color_ice
    config.cue_color = config.player2_cue_color
def glue():
    config.friction_coeff=0.9
    config.table_color =config.table_color_glue
    config.cue_color=config.table_color_ice
def standart_friction():
    config.friction_coeff=0.99
    config.table_color=config.table_color_standart
    config.cue_color = config.player1_cue_color

def inelastic_col():
    config.ball_coeff_of_restitution=0

def elastic_col():
    config.ball_coeff_of_restitution=1

import config
import graphics
import cue
def ice():
    config.friction_coeff=0.9999
    config.table_color =config.table_color_ice
def glue():
    config.friction_coeff=0.9
    config.table_color =config.table_color_glue
def standart_friction():
    config.friction_coeff=0.99
    config.table_color=config.table_color_standart
    config.cue_color = config.cue_color_standart

def inelastic_col():
    config.ball_coeff_of_restitution=0
    config.cue_color = config.cue_color_elastic

def elastic_col():
    config.ball_coeff_of_restitution=1
    config.cue_color = config.cue_color_inelastic
    

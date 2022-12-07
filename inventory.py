import config


def ice():
    config.friction_coeff=0.9999


def inelastic_col():
    config.ball_coeff_of_restitution=0

def elastic_col():
    config.ball_coeff_of_restitution=1

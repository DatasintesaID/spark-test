from utils.dict import dict_get_default_zero


def max_rrc_user(counters, duration):
    return dict_get_default_zero(counters, 'C373200029')

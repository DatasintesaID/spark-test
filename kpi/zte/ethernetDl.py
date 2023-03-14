from utils.dict import dict_get_default_zero


def ethernet_dl(counters, duration):
    return dict_get_default_zero(counters, 'C370020010')

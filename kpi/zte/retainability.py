from utils.dict import dict_get_default_zero


def ethernet_dl(counters, duration):
    p340440 = dict_get_default_zero(counters, 'P340440')
    p340441 = dict_get_default_zero(counters, 'P340441')

    if p340441 == 0:
        return 0
    else:
        return p340440/p340441

from utils.dict import dict_get_default_zero


def voltage_traffic(counters, duration):
    c373240800 = dict_get_default_zero(counters, 'C373240800')

    return c373240800 * duration / 3600

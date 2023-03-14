from utils.dict import dict_get_default_zero


def ul_prb_utilization(counters, duration):
    c373424608 = dict_get_default_zero(counters, 'C373424608')
    c373424609 = dict_get_default_zero(counters, 'C373424609')

    if c373424609 == 0:
        return 0
    else:
        return (c373424608/c373424609)

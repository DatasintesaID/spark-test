from utils.dict import dict_get_default_zero


def volte_ul_volume(counters, duration):
    c373343765 = dict_get_default_zero(counters, 'C373343765')
    c373343766 = dict_get_default_zero(counters, 'C373343766')

    return (c373343765*1000000) + (c373343766 * 1000)

from utils.dict import dict_get_default_zero


def user_ul_throughput(counters, duration):
    c374107517 = dict_get_default_zero(counters, 'C374107517')
    c374107518 = dict_get_default_zero(counters, 'C374107518')
    c374107519 = dict_get_default_zero(counters, 'C374107519')

    if c374107519 == 0:
        return 0
    else:
        return ((c374107517 * 1000) + c374107518) / c374107519

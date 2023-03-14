from utils.dict import dict_get_default_zero


def ul_payload(counters, duration):
    c373343804 = dict_get_default_zero(counters, 'C373343804')
    c373343805 = dict_get_default_zero(counters, 'C373343805')

    return ((c373343804 * 1000000) + (c373343805 * 1000)) / (8 * 1024 * 1024)

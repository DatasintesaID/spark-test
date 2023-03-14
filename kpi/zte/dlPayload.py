from utils.dict import dict_get_default_zero


def dl_payload(counters, duration):
    c373343806 = dict_get_default_zero(counters, 'C373343806')
    c373343807 = dict_get_default_zero(counters, 'C373343807')

    return ((c373343806 * 1000000) + (c373343807 * 1000)) / (8 * 1024 * 1024)

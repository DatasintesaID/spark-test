from utils.dict import dict_get_default_zero


def cell_dl_throughput(counters, duration):
    c373343806 = dict_get_default_zero(counters, 'C373343806')
    c373343807 = dict_get_default_zero(counters, 'c373343807')
    c373343885 = dict_get_default_zero(counters, 'C373343885')
    if c373343885 == 0:
        return 0
    else:
        return ((c373343806 * 1000) + c373343807) / c373343885

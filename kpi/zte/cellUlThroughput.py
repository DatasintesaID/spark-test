from utils.dict import dict_get_default_zero


def cell_ul_throughput(counters, duration):
    c373343804 = dict_get_default_zero(counters, 'C373343804')
    c373343805 = dict_get_default_zero(counters, 'C373343805')
    c373343875 = dict_get_default_zero(counters, 'C373343875')
    if c373343875 == 0:
        return 0
    else:
        return ((c373343804 * 1000) + c373343805) / c373343875

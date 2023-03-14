from utils.dict import dict_get_default_zero


def dl_prb_utilization(counters, duration):
    c373424610 = dict_get_default_zero(counters, 'C373424610')
    c373424611 = dict_get_default_zero(counters, 'C373424611')

    if c373424611 == 0:
        return 0
    else:

        return c373424610 / c373424611

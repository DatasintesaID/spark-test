from utils.dict import dict_get_default_zero


def s1_signal_success(counters, duration):
    c373495201 = dict_get_default_zero(counters, 'C373495201')
    c373495200 = dict_get_default_zero(counters, 'C373495200')

    if c373495200 == 0:
        return 0
    else:
        return (c373495201/c373495200)

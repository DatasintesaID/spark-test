from utils.dict import dict_get_default_zero


def availability(counters, duration):
    c = dict_get_default_zero(counters, 'C373230700')
    if duration == 0:
        return 0
    else:
        return 100 * (c/duration)

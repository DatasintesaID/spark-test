from utils.dict import dict_get_default_zero


def last_tti_ratio(counters, duration):

    c373343806 = dict_get_default_zero(counters, 'C373343806') * 1000
    c373343807 = dict_get_default_zero(counters, 'C373343807')

    C374107460 = dict_get_default_zero(counters, 'C374107460') * 1000
    C374107461 = dict_get_default_zero(counters, 'C374107461')
    C374107463 = dict_get_default_zero(counters, 'C374107463') * 1000
    C374107464 = dict_get_default_zero(counters, 'C374107464')
    C374107466 = dict_get_default_zero(counters, 'C374107466') * 1000
    C374107467 = dict_get_default_zero(counters, 'C374107467')
    C374107469 = dict_get_default_zero(counters, 'C374107469') * 1000
    C374107470 = dict_get_default_zero(counters, 'C374107470')
    C374107472 = dict_get_default_zero(counters, 'C374107472') * 1000
    C374107473 = dict_get_default_zero(counters, 'C374107473')
    C374107475 = dict_get_default_zero(counters, 'C374107475') * 1000
    C374107476 = dict_get_default_zero(counters, 'C374107476')
    C374107478 = dict_get_default_zero(counters, 'C374107478') * 1000
    C374107479 = dict_get_default_zero(counters, 'C374107479')
    C374107481 = dict_get_default_zero(counters, 'C374107481') * 1000
    C374107482 = dict_get_default_zero(counters, 'C374107482')
    C374107484 = dict_get_default_zero(counters, 'C374107484') * 1000
    C374107485 = dict_get_default_zero(counters, 'C374107485')

    p = c373343807 + c373343806
    m = C374107460 + C374107461 + C374107463 + C374107464 + C374107466 + C374107467 + C374107469 + C374107470 + C374107472 + \
        C374107473 + C374107475 + C374107476 + C374107478 + C374107479 + \
        C374107481 + C374107482 + C374107484 + C374107485

    if p == 0:
        return 0
    else:
        return (p-m)/p

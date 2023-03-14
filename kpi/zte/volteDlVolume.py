from utils.dict import dict_get_default_zero


def volte_dl_volume(counters, duration):
    c373210372 = dict_get_default_zero(counters, 'C373210372')
    c373343739 = dict_get_default_zero(counters, 'C373343739')

    return (c373210372*1000000) + (c373343739 * 1000)

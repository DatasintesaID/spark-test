from utils.dict import dict_get_default_zero


def volte_call_drop_rate(counters, duration):

    p = sum(map(lambda x: dict_get_default_zero(counters, x), [
            'C373210372', 'C373210382', 'C373210412', 'C373210432', 'C373210442', 'C373210502', 'C373210512', 'C373505345']))

    c = sum(map(lambda x: dict_get_default_zero(counters, x), [
            'C373210200', 'C373210254', 'C373210452', 'C373240809', 'C373546248']))

    if c == 0:
        return 0
    else:
        return p/c

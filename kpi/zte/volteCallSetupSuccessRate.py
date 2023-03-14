from utils.dict import dict_get_default_zero


def volte_call_setup_success_rate(counters, duration):

    p = sum(map(lambda x: dict_get_default_zero(counters, x), [
            'C373210200', 'C373210254']))

    c = sum(map(lambda x: dict_get_default_zero(counters, x), [
        'C373210200', 'C373210201', 'C373210202', 'C373210203', 'C373210204', 'C373210205', 'C373210254', 'C373210255', 'C373210256', 'C373210257', 'C373210258', 'C373210259', 'C373210580', 'C373210590', 'C373505375', 'C373505384']))

    if c == 0:
        return 0
    else:
        return p/c

from utils.dict import dict_get_default_zero


def mobility(counters, duration):

    p = sum(map(lambda x: dict_get_default_zero(counters, x),
            ["C373250980" + "C373261280", "C373271580"]))
    c = sum(map(lambda x: dict_get_default_zero(counters, x),
            ["C373250900", "C373261200", "C373271500"]))

    if c == 0:
        return 0
    else:
        return p/c

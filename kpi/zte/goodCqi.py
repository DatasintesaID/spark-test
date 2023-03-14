from utils.dict import dict_get_default_zero


def good_cqi(counters, duration):
    p = sum(map(lambda x: dict_get_default_zero(counters, x), ["C373434707", "C373434708", "C373434709", "C373434710",
                                                               "C373434711", "C373434712", "C373434713", "C373434714", "C373434715"]))
    c = sum(map(lambda x: dict_get_default_zero(counters, x), ["C373434700", "C373434701", "C373434702", "C373434703", "C373434703", "C373434704",
            "C373434705 +C373434706", "C373434707", "C373434708", "C373434709", "C373434710", "C373434711", "C373434712", "C373434713", "C373434714", "C373434715"]))

    if c == 0:
        return 0
    else:
        return p/c

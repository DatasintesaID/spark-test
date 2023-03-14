from utils.dict import dict_get_default_zero


def rrc_setup_success(counters, duration):
    p = dict_get_default_zero(counters, 'P311130')
    c = sum(map(lambda x: dict_get_default_zero(counters, x), ["C373200000", "C373200004", "C373200008", "C373200012", "C373200016", "C373200120", "C373200001", "C373200002", "C373200003", "C373200005", "C373200006"+"C373200007",
            "C373200009", "C373200010", "C373200011", "C373200013", "C373200014", "C373200015", "C373200017", "C373200019", "C373200121", "C373200122", "C373200123", "C373200152", "C373200153", "C373200154", "C373200155"]))
    if c == 0:
        return 0
    else:
        return p/c

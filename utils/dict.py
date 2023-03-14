

def dict_get_default(d: dict, key: str, default: any):
    return d.get(key, default)


def dict_get_default_zero(d: dict, key: str):
    return dict_get_default(d, key, 0)


def dict_get_default_none(d: dict, key: str):
    return dict_get_default(d, key, None)

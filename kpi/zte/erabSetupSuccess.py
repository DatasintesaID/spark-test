from utils.dict import dict_get_default_zero


def erab_setup_success(counters, duration):
    p311149 = dict_get_default_zero(counters, 'P311149')
    c = sum(map(lambda x: dict_get_default_zero(counters, x), ["C373505473", "C373505474", "C373505475", "C373505476", "C373505477", "C373505478", "C373505479", "C373210589",
                                                               "C373505481", "C373505482", "C373505483", "C373505484", "C373505485", "C373505486", "C373505487", "C373210599"]))
    if c == 0:
        return 0
    else:
        return (p311149/c)

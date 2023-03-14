from utils.dict import dict_get_default_zero


def user_dl_throughput(counters, duration):
    c374107514 = dict_get_default_zero(counters, 'C374107514')
    c374107515 = dict_get_default_zero(counters, 'C374107515')
    c374107516 = dict_get_default_zero(counters, 'C374107516')

    if c374107516 == 0:
        return 0
    else:
        return ((c374107514 * 1000) + c374107515) / c374107516

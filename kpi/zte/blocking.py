from utils.dict import dict_get_default_zero


# @F.udf(returnType=T.DoubleType())
# def blocking(counters, duration):
#     data = json.loads(counters)
#     return dict_get_default_zero(data, 'C373404503')


def blocking(counters, duration):
    return dict_get_default_zero(counters, 'C373404503')

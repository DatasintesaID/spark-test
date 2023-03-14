from utils.dict import dict_get_default_zero


# @F.udf(returnType=T.DoubleType())
# def avg_user_number(counters, duration):
#     data = json.loads(counters)
#     return dict_get_default_zero(data, 'C373200030')

def avg_user_number(counters, duration):
    return dict_get_default_zero(counters, 'C373200030')

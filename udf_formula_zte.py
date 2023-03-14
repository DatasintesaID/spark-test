
import sys
import json
from pyspark.sql import SparkSession, Row, functions as F, Column, types as T
from formula_zte import formulas

sys.path.append('./kpi/zte/')


def default_func(a, b):
    return None


@F.udf(returnType=T.StringType())
def udf_formula(counters, duration):
    data = json.loads(counters)

    res = dict()

    for x in formulas.items():
        v = x[1](data,  duration)
        if v is not None:
            res[x[0]] = v

    return json.dumps(res)

    # return {x[1] : x[1] for y in map(lambda x: getattr(globals()[x[0]], x[1], default_func)(data,  duration), formulas.items()) if y is not None}
    # return json.dumps({"availability": maxActiveUser.max_active_user(data, duration)})

from udf_formula_zte import udf_formula
import json

# print(udf_formula(json.dumps({'C373230700': 100}), 100))

from sqlalchemy import create_engine

# print(create_engine)

db = create_engine('postgresql://postgres:root@localhost:5432/pasti')
conn = db.connect()

print(conn)

# @F.udf()
# def sum_json(x):
#     result = dict(functools.reduce(operator.add,
#                                    map(collections.Counter, map(lambda a: json.loads(a), x))))
#     return json.dumps(result)


# def default_func(a, b):
#     return None

#     # .groupBy('enodeb_id') \
#     # .agg(sum_json(F.collect_list('counters')).alias('counters'), F.sum('duration').alias('duration')) \
# a = df \
#     .withColumns({
#         'kpi': F.to_json(
#             F.struct(
#                 *[x for x in map(lambda x: getattr(globals()[x[0]], x[1], default_func)(F.col('counters'),  F.col('duration')).cast(T.DoubleType()).alias(x[0]), formulas.items()) if x is not None]
#             ),
#         )
#     }) \
#     .collect()

# print(a[0]['kpi'])

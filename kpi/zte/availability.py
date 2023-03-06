from pyspark.sql import SparkSession, Row, functions as F, Column


def availability():
    return (100 * (F.when(F.get_json_object('counters', '$.C373230700').isNotNull(),
                          F.get_json_object('counters', '$.C373230700')).otherwise(0) / F.col('duration')))

# availability = (100 * (F.when(F.get_json_object('counters', '$.C373230700').isNotNull(),
#                               F.get_json_object('counters', '$.C373230700}')).otherwise(0) / F.col('duration')))

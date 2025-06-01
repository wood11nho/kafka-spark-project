from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType, LongType

# 1. Inițializează Spark
spark = SparkSession.builder \
    .appName("KafkaSparkSQL") \
    .getOrCreate()

# 2. Schema JSON-ului
schema = StructType() \
    .add("timestamp", LongType()) \
    .add("ip_address", StringType()) \
    .add("trx_amount", DoubleType())

# 3. Citește din Kafka
df_kafka = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:29092") \
    .option("subscribe", "tranzactii") \
    .option("startingOffsets", "latest") \
    .load()

# 4. Transformă și parsează
df_json = df_kafka.selectExpr("CAST(value AS STRING) as json_value") \
    .select(from_json(col("json_value"), schema).alias("data")) \
    .select("data.*")

# 5. Query SQL – doar tranzacții mari
df_json.createOrReplaceTempView("transactions")

df_fraude = spark.sql("""
    SELECT timestamp, ip_address, trx_amount
    FROM transactions
    WHERE trx_amount > 500
""")

# 6. Afișare în consolă
# query = df_fraude.writeStream \
#     .outputMode("append") \
#     .format("parquet") \
#     .option("path", "/app/output/tranzactii_parquet") \
#     .option("checkpointLocation", "/app/output/checkpoint") \
#     .start()
    
# ALERTĂ pe tranzacții suspecte (ex: > 900)
df_alert = df_json.filter(col("trx_amount") > 900)

query_alert = df_alert.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .option("numRows", 1) \
    .start()

# query.awaitTermination()
query_alert.awaitTermination()
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode
import os

# Asegurar carpeta de salida
os.makedirs("data/processed", exist_ok=True)

# Iniciar sesión Spark
spark = SparkSession.builder \
    .appName("JobMarketSpark") \
    .master("local[*]") \
    .getOrCreate()

print("📊 Spark UI activa en http://localhost:4040")

# Leer JSON desde la API
df_raw = spark.read.option("multiLine", "true").json("data/raw/job_data.json")

# Explode de las ofertas de trabajo
df_jobs = df_raw.select(explode(col("SearchResult.SearchResultItems")))
input("⌛ Spark está corriendo. Abre http://localhost:4040 y presiona ENTER aquí cuando quieras cerrarlo.")
spark.stop()

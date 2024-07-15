from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
import faker

# Initialize Spark session
spark = SparkSession.builder.appName("AnonymizeCSV").getOrCreate()

# Load CSV file into DataFrame
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# Initialize Faker
fake = faker.Faker()

# Define UDFs for anonymization
fake_first_name = udf(lambda: fake.first_name(), StringType())
fake_last_name = udf(lambda: fake.last_name(), StringType())
fake_address = udf(lambda: fake.address(), StringType())

# Apply UDFs to DataFrame
df_anonymized = df.withColumn("first_name", fake_first_name()) \
                  .withColumn("last_name", fake_last_name()) \
                  .withColumn("address", fake_address())

# Write anonymized data to CSV
df_anonymized.write.csv("anonymized_data_spark.csv", header=True)

# Stop Spark session
spark.stop()

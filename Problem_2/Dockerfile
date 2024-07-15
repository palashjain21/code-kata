# Use the official Apache Spark image
FROM bitnami/spark:latest

# Copy the application code
COPY anonymize_spark.py /app/anonymize_spark.py
COPY data.csv /app/data.csv

# Set the working directory
WORKDIR /app

# Run the Spark job
CMD ["spark-submit", "--master", "local[*]", "anonymize_spark.py"]

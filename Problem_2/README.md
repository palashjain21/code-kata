1. Create and Anonymize CSV File
python3 generate_csv.py 

2. Anonymize the CSV file
python3 anonymize_csv.py

3. Handling Large Datasets with Apache Spark
For larger datasets, we can use Apache Spark to process the data. Spark can handle large volumes of data across multiple nodes in a cluster.

Step 1: Install Apache Spark
You can install Spark locally by following the instructions here.

Step 2: Anonymize Data using PySpark

Run Dockerfile

Basic Engineering Principles
1. Modularity: Each part of the code performs a single task.
2. Scalability: Solution scales from small to large datasets.
3. Readability: Code is well-documented and easy to understand.
4. Dockerfile for Spark Job
To further simplify deployment, we can use Docker to containerize our Spark job.

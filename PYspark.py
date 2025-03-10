# PySpark Tutorial for Beginners 🚀
# PySpark is the Python API for Apache Spark, an open-source distributed computing framework used for big data processing and analytics. This tutorial will introduce you to PySpark and help you get started.

# . What is PySpark?
# PySpark is the Python API for Apache Spark.
# It allows data engineers and data scientists to process large datasets efficiently.
# It supports distributed computing and can be used for data processing, machine learning, and real-time analytics.

# pip install pyspark

# import pyspark
# print(pyspark.__version__)

 # Creating a PySpark Session
# A SparkSession is the entry point for using PySpark. It allows you to create and manipulate DataFrames.

# from pyspark.sql import SparkSession

# Create a Spark session
# spark = SparkSession.builder.appName("PySparkTutorial").getOrCreate()
#
# # Check the Spark session
# print(spark)

# data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
# columns = ["Name", "Age"]
#
# df = spark.createDataFrame(data, columns)
# df.show()

# df = spark.read.csv("data.csv", header=True, inferSchema=True)
# df.show()

# 3️⃣ Basic DataFrame Operations
# a) Show & Describe Data

# df.show(5)  # Show first 5 rows
# df.printSchema()  # Print DataFrame schema
# df.describe().show()  # Get summary statistics


# b) Selecting & Filtering

# df.select("name", "age").show()  # Select specific columns
#
# df.filter(df.age > 25).show()  # Filter rows where age > 25
#
# Grouping & Aggregation
#
# df.groupBy("age").count().show()  # Count occurrences of each age
# df.agg({"age": "max"}).show()  # Get max age
#
#

# SQL Queries in PySpark

# df.createOrReplaceTempView("people")
# result = spark.sql("SELECT name, age FROM people WHERE age > 25")
# result.show()


# Working with Missing Data

# df.na.drop().show()  # Drop rows with missing values
# df.na.fill("Unknown").show()  # Fill missing values with "Unknown"


# Saving Data

# df.write.csv("output.csv", header=True)  # Save as CSV
# df.write.parquet("output.parquet")  # Save as Parquet format

# Closing Spark Session
# spark.stop()
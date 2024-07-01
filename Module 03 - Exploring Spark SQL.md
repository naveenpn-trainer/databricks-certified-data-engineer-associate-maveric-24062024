# Spark SQL

![image-20240627142048213](I:\My Drive\Training Providers\Corporate Trainings\Edyoda\Maveric - Databricks Associate\imgs\Module 03 - Exploring Spark SQL\image-20240627142048213.png)

> Spark SQL is one of the module in the Spark Eco-system to query and analyze structured and semi-structured data.

* Spark SQL provides a unified API to perform
  * Batch Computation
  * Real-time Streaming
* GraphX : Neo4J
* To interact with Spark SQL, there are three ways
  * SQL
  * DataFrame (Python, Scala)
  * Dataset (Scala)

## Data Source API

* The primary interface to create DataFrame is by DataFrameReader (C)

* All the methods to create DataFrame is present inside DataFrameReader

  * .csv
  * .json
  * .load
  * .parquet
  * .orc
  * .jdbc

* By default 2 objects will be created

  * spark (SparkSession)

  * sc (SparkContext)

    ```
    dfr = spark.read
    print(type(dfr))
    
    
    ```

    

## Data Frame API



## Deep Dive DataFrame API
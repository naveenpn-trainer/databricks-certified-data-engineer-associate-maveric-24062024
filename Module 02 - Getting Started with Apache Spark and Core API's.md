# Getting Started with Apache Spark and Core API's

> Apache Spark is an **in-memory cluster computing framework**, <u>designed to handle a wide range of big data workloads</u>.

![image-20240624162121410](I:\My Drive\Training Providers\Corporate Trainings\Edyoda\Maveric - Databricks Associate\imgs\Module 02 - Getting Started with Apache Spark and Core API's\image-20240624162121410.png)

Designed to handle a wide range of big data workloads

1. Data Integration and ETL
2. High Performance Batch Computation
3. Machine Learning Analytics
4. Real-time stream processing
5. Graph computation

**Important Points**

1. Apache Spark is natively written using Scala 
   1. Scala is a JVM based language

## PySpark (Python + Spark)

> PySpark is the **Python API for Apache Spark**.

![img](https://lh7-us.googleusercontent.com/docsz/AD_4nXf5Tll_0tIPj7uLpFmkUnIL4F5svJvrVjs05FSXWH8K_xjab1hcpsNZOCm0xn6BknkjAO7lbY-Rx5cQMexzvv3Ez1PAuhqALeFn_e0DifG1p1PFmXKiJAhIcHoKFQ6zYCX-ZbsD7bqd3O9bEa4FFOOq6RY?key=uvmlVet7-pBAx-jz0PuzLA)

```
class DBConnection {

   public String getData() {
       return "Welcome to Integrate Java with Python"
   }
}
```

* The PySpark communicates with Spark using Py4J API

![img](https://lh7-us.googleusercontent.com/docsz/AD_4nXdJpW6Rw8SFSns_fXHB6TWpX6qs0e6gOvUWPKMrIDHj5OP6M7OONvzIuR0segS0qS6fIV67U-FS-DcXTyuYi7OEXFX1n-ZvF_j-DAeph5GsTYX2Wp4_uyXvIbE36NbYJKYzceQkswgaHt9-LO3Bd92_eXo?key=uvmlVet7-pBAx-jz0PuzLA)

## MapReduce and Spark Data Flow



## Ecosystem

![img](https://lh7-us.googleusercontent.com/docsz/AD_4nXeHUzHVFdhI35p72T04O1p2zRqf_Rc5p-GmUbaXKqfb7G-x7yQSwWLp6m5CdX7B3IgjC2H-w4qBaZmpPjuVAsuZs0enHzlTvIdj-Dg0UqfNs68vTak2qwe5Vr3UneUg6qLJJDf_mbFUsrinaJmjy1q17VU?key=uvmlVet7-pBAx-jz0PuzLA)

1. Spark SQL is one of the module in the Spark ecosystem to analyze structured and semi-structured data
   1. Batch Computation
   2. Real-time Comput
2. MLLib : Machine Learning Library
3. GraphX : 
4. Streaming (Deprecated)

**Important Points**

1. Spark SQL provides a **unified API for Batch and Stream Processing**
2. Spark allows you to have a plug and play resource management layer 

## Ways to Write and Execute Spark Programs

1. Spark Interactive Shell
2. AWS EMR (Elastic Map Reduce) vs Azure HDInsight
3. Databricks
4. Azure
5. Google Colabs

### Spark Interactive Shell

* It is a command line interface provided by Apache Spark
* Spark provides two main interactive shells
  * Spark Shell (Scala)
  * PySpark Shell (Pytho)

## Assignments

1. Use Py4J API to demonstrate invoking Java code from python



1. Low Level API (RDD's)
2. High Level API (Spark SQL)

## RDD (Resilient Distributed Dataset)

> RDD' are the building blocks of any spark application.

* it is deprecated

R : Fault tolerant

D : Data is distributed among multiple nodes

D : Collection of partitioned data

## Partitions

> A partition in spark is a logical division of data stored on the node in the cluster.

* RDD is a collection of partitions

![img](https://lh7-us.googleusercontent.com/docsz/AD_4nXewvLI3I9uCj47q8s8FufCd-6egZuag0b1DDrwuWN7P2l8jT2avurtEX4FGRrKb93CimOusLjpiWYn6JqNp9TtN-Cya2bHIUjsMp-YDeibP_4z_BTZNdh5JPZpMSavU__UgtUh6bN4e6p5jpjTta0OLqpaM?key=uvmlVet7-pBAx-jz0PuzLA)



![img](https://lh7-us.googleusercontent.com/docsz/AD_4nXdcv9gw3Sh1LweQAtWtBZd04ULNK1B-Z2k13QzAL-HEjHwmeY5fDyWvIKhThFS8I6lVd9EiL482rTCGG_NI-NlUGUZ8U72kyhSHBIaGpghIzFyy69Xq2VG74iPhPjAfI7j39FVV98aQBGbebYgFGWTanV0?key=uvmlVet7-pBAx-jz0PuzLA)

## RDD Creation

There are two popular ways to create an RDD

1. Create an RDD from Collection
2. Create an RDD from external source

* All the methods to create RDD is present inside SparkContext (sc)

![img](https://lh7-us.googleusercontent.com/docsz/AD_4nXdjXTuuZbh7Np9i8tDQM7J9ANqY8Jb4VtlrMRLpNFEazmJ7GqIoTQUM82gaLnlQwe4BGjiJyh6X07R_sOe8cSm2fCc-CdBXGHU0HSPwssu45-7T9YE5CL4nvj5l1zsOYx3ow9TkS1G-ArOSTet20tRtkEc?key=uvmlVet7-pBAx-jz0PuzLA)

## Operations

once an RDD is created we can perform two types of operations

1. Transformation
2. Actions

### Transformation

* Only applying transformation, it creates a new RDD from an existing RDD
* .map(func), filter(predFun), reduceBYKey(func),

![img](https://lh7-us.googleusercontent.com/docsz/AD_4nXcCeOBIYcxhzL7ZWtQTikW5fjXRAc_gV63-5t7LYwwLZZL6X5_Iyy3XV9CoqR1NE5lIOH6DtkOqCcJ1WNbdIqOIPQicvyF3v2sD79TmNcRgQc2ng21uyMYUdjwc9UF9eu2xC5p3hJg3iEV1XKRSEIVc-rwJ?key=uvmlVet7-pBAx-jz0PuzLA)

### Actions

* Actions are the operation on RDD to carry o

## Self Study Topics / Assignments

![img](https://lh7-us.googleusercontent.com/docsz/AD_4nXdzGmFICqzaPl6V5JFUOhWuvsjObQ7z9yw1gkUj8m4Uw5Ms-aUwoXebdRy7gSJ8rnbkd2MKS7m6sQwjXY5m6QogsMPsezZUjHh2Ib9pYvryqmMdKckZxyqEgeK7aiCq1zrzTsM7OskjTG3sQTMTJKudftnF?key=uvmlVet7-pBAx-jz0PuzLA)

1. Loaded users_001.csv
2. List of Distinct Regions Name

# Azure Databricks Platform

> Azure Databricks is a unified platform for Data Engineering, Data Analytics and ML

## Architecture 

It consists of two components

![img](https://lh7-us.googleusercontent.com/docsz/AD_4nXdxejkPnWGscoKG8y9TzK45PaFj1GH-Z1DC5RKjiCxqCoJ33UyLjpeF38uMCCk4vRsjXgM8WRgrSDXm9A_GChl7DX81rr-Fa9QMH6lfVsUtZmrKtGfYwQ0e5kLKr8hPOoUwt60crDX5r7cUUdN_6YihD30?key=aJiAWgzYP3udRlKejSDPqw)

### Control Plane

* The control plane consists of backend services that databricks manages in its own cloud
* Most data isn't stored here.

### Data Plane / Compute

* The DP is where the data is stored and processed.
* All compute resources resides in the cloud provider

## Azure Components

1. Workspace
   1. Folders
   2. Repos
   3. Notebooks
2. Compute 

| All Purpose / Interactive Cluster     | Job Cluster                      |
| ------------------------------------- | -------------------------------- |
| Created manually by users or automate | Created by Jobs                  |
| Persistent                            | Terminated at the end of the job |
| Suitable for interactive workloads    | Suitable for automated workloads |
| Shared among multiple users           | isolated just for the Job.       |
| Expensive to run                      | Cheaper to run                   |
























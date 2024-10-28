# Databricks notebook source
# MAGIC %md 
# MAGIC ###Data Ingestion of the previous day

# COMMAND ----------

import requests
from datetime import datetime, timedelta

schema: str = "so_schema"
limit: int = 200
yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
csv_path_yesterday: str = f"/Volumes/dbx_training/{schema}/raw_files_objets_trouves/file_{yesterday}.csv"

raw_url_objets_trouves_yesterday: str = f"https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/objets-trouves-restitution/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B&refine.date={yesterday}&limit={limit}"

response = requests.get(raw_url_objets_trouves_yesterday)
response.raise_for_status()

with open(csv_path_yesterday, "wb") as file:
    file.write(response.content)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ###Update the bronze table with the new data

# COMMAND ----------

df_data_yesterday = spark.read.option("header","true").option("delimiter",";").csv(csv_path_yesterday)

# Rename columns to delete " "
df_data_yesterday = (df_data_yesterday
             .withColumnRenamed("Date et heure de restitution", "Date_et_heure_de_restitution")
             .withColumnRenamed("Code UIC", "Code_UIC")
             .withColumnRenamed("Nature d'objets", "Nature_d'objets")
             .withColumnRenamed( "Type d'objets", "Type_d'objets")
             .withColumnRenamed( "Type d'enregistrement", "Type_d'enregistrement"))

# Append new data to the bronze table
df_data_yesterday.write.mode("append").saveAsTable(f"dbx_training.{schema}.bronze_objets_trouves")

# Databricks notebook source
# MAGIC %md
# MAGIC # History Ingest

# COMMAND ----------

# MAGIC %md ## Générer un csv localement

# COMMAND ----------

import requests

schema: str = "so_schema"
limit: int = 200

raw_url_objets_trouves: str = f"https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/objets-trouves-restitution/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B&limit={limit}"

response = requests.get(raw_url_objets_trouves)
response.raise_for_status()

with open(f"/Volumes/dbx_training/{schema}/raw_files_objets_trouves/file.csv", "wb") as file:
    file.write(response.content)

# COMMAND ----------



# COMMAND ----------



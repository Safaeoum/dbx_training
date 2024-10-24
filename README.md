# TP Databricks - Data Engineering avec les données publiques de la SNCF

## Objectif du TP

L’objectif est de créer un pipeline d’ingestion et de transformation de données
sur Databricks en utilisant les données publiques de la SNCF. Vous allez
structurer les données dans **Unity Catalog** et veiller à produire un code
propre et bien organisé.

Vous travaillerez avec les datasets suivants :

- **Objets trouvés SNCF** : Historique des objets trouvés dans les gares
  ([source](https://ressources.data.sncf.com/explore/dataset/objets-trouves-restitution/information/)).

Chaque membre de l’équipe devra organiser ses données dans **son propre schéma**
dans Unity Catalog pour assurer une bonne gestion et isolation des jeux de
données.

## Étapes du TP

Versionner son code avec Databricks Repo.

### 1. Pipeline d’ingestion historique (RAW -> BRONZE)

_Cette pipeline se déclenche manuellement._

1. Requêtez l’API d'export de la SNCF pour générer localement un fichier CSV
   contenant les données historiques des objets trouvés.
2. Créez une pipeline pour ingérer ces données dans une table **BRONZE** dans
   votre schéma Unity Catalog. Cette table contiendra les données brutes et non
   transformées.
3. Supprimez le fichier CSV local après ingestion dans Databricks.

### 2. Pipeline d’ingestion quotidienne (RAW -> BRONZE)

_Cette pipeline se déclenche automatiquement chaque matin._

1. Requêtez l’API de la SNCF pour récupérer les nouvelles données de la veille.
2. Modifiez votre pipeline d’ingestion pour ajouter automatiquement ces
   nouvelles données à votre table **BRONZE**.
3. Conservez le fichier CSV du jour pour des besoins d'auditabilité.

### 3. Transformation et typification des données (BRONZE -> SILVER)

1. Créez une table **SILVER** dans laquelle vous appliquez les transformations
   nécessaires pour nettoyer et structurer les données.
2. Appliquez les transformations suivantes :
   - Convertir les dates dans le bon format (par exemple, `yyyy-MM-dd`).
   - Transformer les colonnes contenant des nombres en types appropriés (`INT`,
     `FLOAT`, etc.).
   - Gérer les valeurs manquantes de façon appropriée (soit les supprimer, soit
     les remplacer par des valeurs par défaut).
3. Assurez-vous que les données dans cette table sont conformes et prêtes pour
   des analyses plus approfondies.

### 4. Analyse des données (SILVER -> GOLD)

1. Créez une table **GOLD** contenant les données prêtes pour l’analyse.
2. Répondez aux questions suivantes en utilisant des requêtes SQL ou PySpark :
   - Dans quelle gare perd-on le plus d’objets ?
   - Quelle est l’heure où les objets sont le plus souvent perdus ?

### 5. Création d’un Dashboard

1. Créez un tableau de bord interactif dans Databricks pour visualiser les
   résultats des analyses :
   - Une visualisation des gares où le plus d’objets sont perdus.
   - Une visualisation des moments de la journée où les pertes d’objets sont les
     plus fréquentes.

### 6. **Structuration du Unity Catalog et du code**

1. Chaque membre de l'équipe doit structurer ses tables BRONZE, SILVER et GOLD
   dans son propre schéma au sein d’**Unity Catalog**. Par exemple, les tables
   doivent suivre une convention claire de nommage (`bronze_objets_trouves`,
   `silver_objets_trouves`, etc.).
2. Organisez le code de manière modulaire et propre, en respectant les bonnes
   pratiques de programmation (séparation des responsabilités, réutilisation du
   code, documentation).

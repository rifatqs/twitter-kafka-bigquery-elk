from google.cloud import bigquery

PROJECT_ID = "static-cirrus-354813"
DATASET_ID = "BIGPROJECT"
TABLE_ID = "twitter"

client = bigquery.Client()

# 1) create table
schema = [
    bigquery.SchemaField("created_at", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("id", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("username", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("tweet", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("topic", "STRING", mode="REQUIRED")
]

table = bigquery.Table(f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}", schema=schema)
table = client.create_table(table)
print(
    "Created table {}.{}.{}".format(
        table.project, table.dataset_id, table.table_id
    )
)

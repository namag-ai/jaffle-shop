# pylint: disable=invalid-name,consider-using-f-string
import os
import pandas as pd
from sqlalchemy import create_engine
import time
from sqlalchemy.exc import OperationalError

POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_HOST_NAME = os.environ.get('POSTGRES_HOST_NAME')

MAX_TRIES = 3

SLEEP_TIME = 4

conn_string = "postgresql+psycopg2://{}:{}@{}/{}".format(
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST_NAME,
    POSTGRES_DB
    )

engine = create_engine(conn_string, echo=False)

schemas = ['jaffle_shop', 'stripe']
schema_files = {}

success = 0
total_files = 0

for k in schemas:
    schema_files[k] = os.listdir(f'data/{k}')

for k, csv_files in schema_files.items():
    for csv_file in csv_files:
        table_name = csv_file.removesuffix('.csv')
        table_name = table_name.removeprefix('raw_')

        df = pd.read_csv(f'data/{k}/{csv_file}')
        attempts = 0
        while attempts < 3:
            try:
                df.to_sql(name=table_name,schema=k, con=engine, if_exists='replace', index=False)
                print (f"Sucess table: {table_name}")
                success+=1
                break
            except OperationalError as erro:
                attempts += 1
                time.sleep(SLEEP_TIME)
                print (f"Erro Raised: OperationalError: {erro}")

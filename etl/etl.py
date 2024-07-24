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


csv_files = os.listdir('data')
success = 0

for csv_file in csv_files:
    table_name = csv_file.removesuffix('.csv')
    table_name = table_name.removeprefix('raw_')

    df = pd.read_csv(f'data/{csv_file}')
    attempts = 0
    while attempts < 3:
        try:
            df.to_sql(name=table_name,schema='jaffle_shop', con=engine, if_exists='replace', index=False)
            success+=1
            break
        except OperationalError as erro:
            attempts += 1
            time.sleep(SLEEP_TIME)
            print (f"OperationalError: {erro}")



print(f'success in {success}/{len(csv_files)}')

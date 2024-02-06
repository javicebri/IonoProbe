import os
import psycopg2
import GLOBAL_VARS

from dotenv import load_dotenv


def store_local_postgresql(db_name, df):
    """
    """
    load_dotenv()
    engine = psycopg2.connect(
        database=db_name,
        user=os.getenv('LOCAL_POSTGRESQL_USER'),
        password=os.getenv('LOCAL_POSTGRESQL_PASS'),
        host=GLOBAL_VARS.local_postgresql_host,
        port=GLOBAL_VARS.local_postgesql_port
    )
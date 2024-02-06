import os
import psycopg2
import GLOBAL_VARS

from dotenv import load_dotenv
from sqlalchemy import create_engine
from logger import logger, init_logger


def store_local_postgresql(table_name, df):
    """
    """
    load_dotenv()

    db_name=os.getenv('LOCAL_POSTGRESQL_DATABASE')
    user=os.getenv('LOCAL_POSTGRESQL_USER')
    password=os.getenv('LOCAL_POSTGRESQL_PASS')
    host=GLOBAL_VARS.local_postgresql_host
    port=GLOBAL_VARS.local_postgresql_port

    engine = psycopg2.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        port=port
    )

    cur = engine.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname=%s", (db_name,)) # Check if db exists
    exists = cur.fetchone()

    # Close
    if cur:
        cur.close()
    if engine:
        engine.close()

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

    if not exists:
        logger.warning(f'{db_name} data base does not exist.')
    else:
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        engine.dispose()


import pandas as pd
import boto3
from io import StringIO
from dotenv import load_dotenv
import os

def store_in_s3(bucket_name, s3_path, file_name, data):
    load_dotenv()
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    region_name = os.getenv('AWS_REGION')

    # file_key = 'ruta_en_s3/nombre_del_archivo.csv'
    file_key = os.path.join(s3_path, file_name)

    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    if ".csv" in file_name:
        csv_buffer = StringIO()
        data.to_csv(csv_buffer, index=False)
        s3_client.put_object(Body=csv_buffer.getvalue(), Bucket=bucket_name, Key=file_key)
    else:
        s3_client.put_object(Body=data, Bucket=bucket_name, Key=file_key)


    # print(f'DataFrame guardado en s3://{bucket_name}/{file_key}')
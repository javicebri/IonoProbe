# main.py

import os
import json
import requests
import logging
from logger import logger
from paths import get_paths, add_config_paths
from config import load_config
from connect.url_connect import req_GOES, req_Digisonde
from connect.aws_connect import store_in_s3


# Start

# Create paths dict
root = '/home/javier/Projects/IonoProbe/'
paths_dict = get_paths(root)

# Read Config
config = load_config(paths_dict)

# Add paths
paths_dict = add_config_paths(root, paths_dict, config)

# logger.info('Start GOES ETL.')
# logger.info('Req')

run_steps = config['RUN']

for step_i in run_steps:
    if step_i == 'Download_GOES':
        download_GOES(paths_dict['GOES_url'])
        data_df = req_GOES(paths_dict['GOES_url']['url_de'])
    elif step_i == 'Download_DIGISONDE':
        download_Digisonde(paths_dict['DIGISONDE_url'])
        image_bytes = req_Digisonde(paths_dict['DIGISONDE_url']['url_obsebre'])

# store_in_s3(bucket_name = 'ionoprobe', s3_path = 'GOES', file_name = 'prueba.csv', df = data_df)

# print('Finish')
# # with open('output.json', 'w') as file:
# #     json.dump(data_json, data_json, indent=4)  # indent opcional para formato legible

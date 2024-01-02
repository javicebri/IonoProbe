# main.py

import os
import json
import requests
import logging
from logger import logger
from connect.url_connect import req_GOES, req_Digisonde
from connect.aws_connect import store_in_s3


# Start
data_paths = {}
data_paths['url_de'] = 'https://services.swpc.noaa.gov/json/goes/primary/differential-electrons-7-day.json'
data_paths['url_dp'] = 'https://services.swpc.noaa.gov/json/goes/primary/differential-protons-7-day.json'
data_paths['url_ie'] = 'https://services.swpc.noaa.gov/json/goes/primary/integral-electrons-7-day.json'
data_paths['url_ip']= 'https://services.swpc.noaa.gov/json/goes/primary/integral-protons-7-day.json'
data_paths['url_ip_plot'] = 'https://services.swpc.noaa.gov/json/goes/primary/integral-protons-plot-7-day.json'
data_paths['url_mag'] = 'https://services.swpc.noaa.gov/json/goes/primary/magnetometers-7-day.json'
data_paths['url_xray_back'] = 'https://services.swpc.noaa.gov/json/goes/primary/xray-background-7-day.json'
data_paths['url_xray_flares'] = 'https://services.swpc.noaa.gov/json/goes/primary/xray-flares-7-day.json'
data_paths['url_xray'] = 'https://services.swpc.noaa.gov/json/goes/primary/xrays-7-day.json'
data_paths['url_digisonde'] = 'http://dgs.obsebre.es:8081/ionogif//EB040_2023360222001_IO.PNG'


# logger.info('Start GOES ETL.')
# logger.info('Req')
data_df = req_GOES(data_paths['url_de'])

# store_in_s3(bucket_name = 'ionoprobe', s3_path = 'GOES', file_name = 'prueba.csv', df = data_df)

# print('Finish')
# # with open('output.json', 'w') as file:
# #     json.dump(data_json, data_json, indent=4)  # indent opcional para formato legible

req_Digisonde(data_paths['url_digisonde'])
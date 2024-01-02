# main.py

import os
import json
import requests
import logging
from logger.logger import logger
from connect.url_connect import req_GOES
from connect.aws_connect import store_in_s3


# Start
url_de = 'https://services.swpc.noaa.gov/json/goes/primary/differential-electrons-7-day.json'
url_dp = 'https://services.swpc.noaa.gov/json/goes/primary/differential-protons-7-day.json'
url_ie = 'https://services.swpc.noaa.gov/json/goes/primary/integral-electrons-7-day.json'
url_ip = 'https://services.swpc.noaa.gov/json/goes/primary/integral-protons-7-day.json'
url_ip_plot = 'https://services.swpc.noaa.gov/json/goes/primary/integral-protons-plot-7-day.json'
url_mag = 'https://services.swpc.noaa.gov/json/goes/primary/magnetometers-7-day.json'
url_xray_back = 'https://services.swpc.noaa.gov/json/goes/primary/xray-background-7-day.json'
url_xray_flares = 'https://services.swpc.noaa.gov/json/goes/primary/xray-flares-7-day.json'
url_xray = 'https://services.swpc.noaa.gov/json/goes/primary/xrays-7-day.json'

logger.info('Start GOES ETL.')
logger.info('Req')
data_df = req_GOES(url_de)

store_in_s3(bucket_name = 'ionoprobe', s3_path = 'GOES', file_name = 'prueba.csv', df = data_df)

print('Finish')
# with open('output.json', 'w') as file:
#     json.dump(data_json, data_json, indent=4)  # indent opcional para formato legible

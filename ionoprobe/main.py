# main.py

import os
import json
import requests
import logging
from logger import logger
from paths import get_paths, add_config_paths
from config import load_config
from connect.download import download_Digisonde, download_GOES

def main(root="/"):
    # Create paths dict
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
            download_GOES(paths_dict['GOES_url'], config)
        elif step_i == 'Download_DIGISONDE':
            download_Digisonde(paths_dict['DIGISONDE_url'], config)

main(root = '/home/javier/Projects/IonoProbe/')




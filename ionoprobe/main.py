# main.py

import os
import json
import requests
import logging
from logger import logger, init_logger
from paths import get_paths, create_paths, add_config_paths
from config import load_config, format_config
from connect.download import download_digisonde, download_GOES

def main(root="/"):

    # Create paths dict
    paths_dict = get_paths(root)
    create_paths(paths_dict)
    logger = init_logger(root, 'inoprobe')

    # Read Config
    config = load_config(paths_dict)
    config = format_config(config)

    # Add paths
    paths_dict = add_config_paths(root, paths_dict, config)

    # logger.info('Start GOES ETL.')
    # logger.info('Req')

    run_steps = config['RUN']

    for step_i in run_steps:
        if step_i == 'Download_GOES':
            download_GOES(paths_dict, config)
        elif step_i == 'Download_DIGISONDE':
            download_digisonde(paths_dict, config)

main(root = '/home/javier/Projects/IonoProbe/')




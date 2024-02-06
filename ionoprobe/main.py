# main.py

import os
import json
import requests
import logging
import GLOBAL_VARS
from logger import logger, init_logger
from paths import get_paths, create_paths, add_config_paths
from config import load_config, format_config
from connect.goes import GOES_SWPC_NOAA
from connect.digisonde import DIGISONDE_GIRO


def main(root="/"):

    # Create paths dict
    paths_dict = get_paths(root)
    create_paths(paths_dict)
    logger = init_logger(root, 'ionoprobe')
    logger.info(GLOBAL_VARS.header_art)

    # Read Config
    logger.info('Load config.')
    config = load_config(paths_dict)
    logger.info('Format config.')
    config = format_config(config)

    # Add paths
    paths_dict = add_config_paths(root, paths_dict, config)

    goes_swpc_noaa = GOES_SWPC_NOAA(paths_dict=paths_dict, config=config)
    goes_swpc_noaa.download(url_dict=paths_dict['GOES_SWPC_NOAA_url'], target=['local_postgresql', 'local_csv', 's3_csv']) #In the future these arg must be passed by gui selection

    digisonde_giro = DIGISONDE_GIRO(paths_dict=paths_dict, config=config)
    digisonde_giro.download(url_dict=paths_dict['DIGISONDE_GIRO_url'], target=['local_postgresql', 'local_csv', 's3_csv']) #In the future these arg must be passed by gui selection

    logger.info('END IONOPROBE.')

main(root = '/home/javier/Projects/IonoProbe/')




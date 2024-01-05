import time
import itertools
import GLOBAL_VARS
import pandas as pd

from logger import logger
from model.image import get_str_from_image, transform_str_to_df
from model.digiPlain import transform_digi_plain_str_to_df
from connect.url_connect import req_GOES, req_digisonde_image, gen_url_digisonde_plain, req_digisonde_plain
from connect.aws_connect import store_in_s3


def download_digisonde(paths_dict, config):
    """
    Iterate reqs

    @param paths_dict: The URL to retrieve the file from.
    @type paths_dict: dict
    @param config: config file
    @type config: dict
    @return: None
    @rtype: None
    """
    if "DIGISONDE_image_url" in config['DIGISONDE_source']:
        for path_i in paths_dict['DIGISONDE_image_url'].keys():
            image_bytes = req_digisonde_image(paths_dict[path_i])
            # Extract information of the image
            image_str = get_str_from_image(image_bytes)
            # Transform str to df
            image_df = transform_str_to_df(image_str)
        
    if "DIGISONDE_plain_url" in config['DIGISONDE_source']:
        # Get a tuple of each combination ESTATION <-> DATA
        req_couples_list = list(itertools.product(GLOBAL_VARS.sta_dict.keys(), GLOBAL_VARS.DIGISONDE_plain_data.keys()))

        total_df = pd.DataFrame()
        # For each station
        for station_i, data_i in req_couples_list:
            url_str = gen_url_digisonde_plain(paths_dict['DIGISONDE_plain_url']['url_giro'], station_i, data_i, config)
            data_bytes = req_digisonde_plain(url_str)
            # Transform str to df
            data_df = transform_digi_plain_str_to_df(data_bytes)
            if not data_df.shape[0] == 0:
                total_df = pd.concat([total_df, data_df], ignore_index=True)
            else:
                logger.info(f'{station_i} and {data_i} has no data.')
            time.sleep(2)

        total_df.to_feather(paths_dict['output_DIGISONDE'])

  

        # if config is local save in folder, if is aws save in s3
        if "local" in config['save']:
            # print('Finish')
            # # with open('output.json', 'w') as file:
            # #     json.dump(data_json, data_json, indent=4)  # indent opcional para formato legible
            pass
        if "s3" in config['save']:
            # store_in_s3(bucket_name = 'ionoprobe', s3_path = 'DIGISONDE', file_name = 'prueba.png', data = image_bytes)
            pass


def download_GOES(paths_dict, config):
    """
    Iterate reqs

    @param paths_dict: The URL to retrieve the file from.
    @type paths_dict: dict
    @param config: config file
    @type url: Dictionary
    @return: The content of the retrieved image.
    @rtype: DataFrame
    """
    for path_i in paths_dict['GOES_url'].keys():
        data_df = req_GOES(paths_dict['path_i'])
        # if config is local save in folder, if is aws save in s3
        if "local" in config['save']:
            pass
        if "s3" in config['save']:
            # store_in_s3(bucket_name = 'ionoprobe', s3_path = 'DIGISONDE', file_name = 'prueba.png', data = data_df)
            pass

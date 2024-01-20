import os
import time
import itertools
import GLOBAL_VARS
import pandas as pd

from logger import logger
from model.image import get_str_from_image, transform_str_to_df
from model.digiPlain import transform_digi_plain_str_to_df, group_time_quarter_digi_plain_df
from connect.data_connect import get_digisonde_last_date
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
        # req_couples_list = list(itertools.product(GLOBAL_VARS.sta_dict.keys(), GLOBAL_VARS.DIGISONDE_plain_data.keys()))

        for station_i in GLOBAL_VARS.sta_dict.keys():
            raw_df = pd.DataFrame() # DF Container of all new data

            for data_i in GLOBAL_VARS.DIGISONDE_plain_data.keys():
                time.sleep(2) # Avoid server saturation
                logger.info(f' - Download {station_i} - {data_i}')
                raw_file_path = os.path.join(paths_dict['output'], "raw_data_" + station_i + ".feather")
                grouped_file_path = os.path.join(paths_dict['output'], "grouped_data_" + station_i + ".feather")
                # 1º Look in the data to know the range of dates to request
                last_date = get_digisonde_last_date(raw_file_path, station_i, data_i)
                logger.info(f' - Last date is {last_date}')
                # 2º Build request url    
                url_str = gen_url_digisonde_plain(paths_dict['DIGISONDE_plain_url']['url_giro'], station_i, data_i, config)
                # 3º Request    
                data_bytes = req_digisonde_plain(url_str)
                # 4º Transform str to df
                if data_bytes is not None:
                    data_df = transform_digi_plain_str_to_df(data_bytes)
                else:
                    logger.info(f'{station_i} and {data_i} is None.')
                    break
                if not data_df.shape[0] == 0:
                    raw_df = pd.concat([raw_df, data_df], ignore_index=True)
                    # 5º Group in the quarter hh:00, hh:15, hh:30, hh:45. raw df is too sparse because the time of each column can be any minute:
                    grouped_data_df = group_time_quarter_digi_plain_df(raw_df)
                    grouped_df = pd.concat([grouped_df, grouped_data_df], ignore_index=True)


                else:
                    logger.info(f'{station_i} and {data_i} has no data.')

            # 6º SAVE DATA
            # if config is local save in folder, if is aws save in s3
            if "local" in config['save']:
                raw_df.to_feather(raw_file_path)
                grouped_df.to_feather(raw_file_path)
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

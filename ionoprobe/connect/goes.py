import os
import json
import time
import requests
import GLOBAL_VARS
import pandas as pd

from logger import logger
from .connect import Connect
from .aws import store_in_s3, store_rds_postgresql
from .local import store_local_postgresql


class GOES_SWPC_NOAA(Connect):
    def __init__(self, paths_dict, config):
        super().__init__(paths_dict, config)

    def _get_url(self, url):
        """
        Get file from URL.

        @param url: The URL to retrieve the file from.
        @type url: str
        @return: The content of the retrieved file.
        @rtype: DataFrame
        """
        res = requests.get(url)
        if res.status_code == 200:
            res_json = json.loads(res.text)
            return pd.DataFrame(res_json)
        else:
            logger.warning(f'Req ERROR {res.status_code}')
    
    def _get_url_dict(self, url_dict):
        """
        For each url in url_dict get the data

        @param url_dict: The URL dict to retrieve the files from.
        @type url_dict: dict
        @return: dict
        """
        df_dict = {}
        for key_i, url_i in url_dict.items():
            df = self._get_url(url_i)
            df_dict[key_i] = df
            time.sleep(1)      
        return df_dict

    def _save_local_csv(self, df_dict):
        """
        For each url save the csv file in save path set in paths_dict

        @param df_dict: dict with dataframes to be saved
        @type paths_dict: dict
        @return: None
        """
        folder_path = os.path.join(self.paths_dict['output'], GLOBAL_VARS.GOES_SWPC_NOAA_s3_path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for key_i, df_i in df_dict.items():
            f_name = key_i + "_" + self.config['date_hour_str'] + ".csv"
            f_path = os.path.join(folder_path, f_name)
            df_i.to_csv(f_path, sep=';', index=False)

    def _save_s3_csv(self, df_dict):
        """
        Save CSV files in AWS S3

        @param df_dict: dict with dataframes to be saved
        @type paths_dict: dict
        @return: None
        """
        for key_i, df_i in df_dict.items():
            f_name = key_i + "_" + self.config['date_hour_str'] + ".csv"
            store_in_s3(bucket_name = GLOBAL_VARS.S3_BUCKET_NAME, 
                        s3_path = GLOBAL_VARS.GOES_SWPC_NOAA_s3_path, 
                        file_name = f_name, 
                        data = df_i)

    def _save_local_postgresql(self, df_dict):
        """
        Iterate reqs

        @param df_dict: dict with dataframes to be saved
        @type paths_dict: dict
        @return: None
        """
        for key_i, df_i in df_dict.items():
            store_local_postgresql(table_name=key_i, df=df_i)

    def download(self, url_dict, target):
        """
        For each url save the output target type

        @param paths_dict: The URL dict to retrieve the files from.
        @type paths_dict: dict
        @param target: indicate the output type
        @type target: list
        @return: None
        """
        if GLOBAL_VARS.DEBUG_MODE:
            df_dict = {}
            df_dict['differential_electrons'] = pd.read_csv(os.environ['DEBUG_MODE_GOES_FPATH'], sep=';')
        else:
            df_dict = self._get_url_dict(url_dict)

        for target_i in target:
            if target_i.lower() == "local_csv":
                self._save_local_csv(df_dict)
            if target_i == "s3_csv":
                self._save_s3_csv(df_dict)
            if target_i == "local_postgresql":
                self._save_local_postgresql(df_dict)
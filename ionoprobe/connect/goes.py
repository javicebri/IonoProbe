import os
import json
import requests
import pandas as pd

from logger import logger
from .connect import Connect



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
    

    def _download_local_csv(self, url_dict):
        """
        For each url save the csv file in save path set in paths_dict

        @param paths_dict: The URL dict to retrieve the files from.
        @type paths_dict: dict
        @return: None
        """
        for key_i, url_i in url_dict.items():
            df = self._get_url(url_i)
            f_name = key_i + ".csv"
            f_path = os.path.join(self.paths_dict['output'], f_name)
            df.to_csv(f_path, sep=';', index=False)

    
    def _download_s3(self, url_dict):
        """
        Iterate reqs

        @param paths_dict: The URL to retrieve the file from.
        @type paths_dict: dict
        @param config: config file
        @type url: Dictionary
        @return: The content of the retrieved image.
        @rtype: DataFrame
        """
        # store_in_s3(bucket_name = 'ionoprobe', s3_path = 'DIGISONDE', file_name = 'prueba.png', data = data_df)
        pass    


    def download(self, url_dict, target):
        """
        For each url save the output target type

        @param paths_dict: The URL dict to retrieve the files from.
        @type paths_dict: dict
        @param target: indicate the output type
        @type target: list
        @return: None
        """
        for target_i in target:
            if target.lower() == "csv":
                self._download_local_csv(url_dict)
            if target == "s3":
                self._download_s3(url_dict)
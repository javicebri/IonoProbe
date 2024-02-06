import os
import json
import time
import requests
import datetime
import itertools
import GLOBAL_VARS
import pandas as pd

from .aws import store_in_s3, store_rds_postgresql
from logger import logger
from .connect import Connect
from tools.datetools import get_now_date_str
from .local import store_local_postgresql



class DIGISONDE_GIRO(Connect):
    def __init__(self, paths_dict, config):
        super().__init__(paths_dict, config)

    def _get_url(self, url):
        """
        Get file from URL.

        @param url: The URL to retrieve the file from.
        @type url: str
        @return: The content of the retrieved file.
        @rtype: Bytes
        """
        res = requests.get(url)
        if res.status_code == 200:
            return res.content
        else:
            logger.warning(f'REQ ERROR for {url}')

    # def _get_digisonde_giro_last_date(self, station, data):
    #     """
    #     Get the last date from DIGISONDE data.

    #     Parameters:
    #     @param paths_dict (dict): A dictionary containing file paths.
    #     @param station (str): The name of the station.
    #     @param data (str): The type of data.
    #     Returns:
    #     @return datetime.datetime: The last date from DIGISONDE data.
    #     """
    #     current_date_utc = datetime.datetime.now(datetime.timezone.utc)
    #     # Check if exist previous data:
    #     if os.path.exists(paths_dict['data_DIGISONDE_feather_f']):
    #         df = pd.read_feather(paths_dict['data_DIGISONDE_feather_f'], columns=['Time', 'CS_' + data, data, station])
    #         df = df.dropna(subset=['Time', 'CS_' + data, data])
    #         date = df['Time'].max().to_pydatetime()
    #     else:
    #         year_ago_date = current_date_utc - datetime.timedelta(days=365)
    #         date = year_ago_date.replace(hour=0, minute=0, second=0, microsecond=0)
        
    #     return date
        
    def _gen_url_digisonde_giro(self, station_name, data_name):
        """
        Generate the url to make the request for https://giro.uml.edu/didbase/scaled.php.

        @param station_name: Name of the station.
        @type station_name: str
        @param data_name: Name of the data request.
        @type data_name: str
        @return: The url with for the request.
        @rtype: str
        """
        url = self.config['DIGISONDE_GIRO_url']['url']

        origin_date = self.config['DIGISONDE_GIRO_url']["origin_date"]
        origin_year = origin_date.strftime("%Y")
        origin_month = origin_date.strftime("%m")
        origin_day = origin_date.strftime("%d")
        origin_hour = origin_date.strftime("%H")
        origin_minute = origin_date.strftime("%M")
        origin_second = origin_date.strftime("%S")

        last_date = self.config['DIGISONDE_GIRO_url']["last_date"]
        last_year = last_date.strftime("%Y")
        last_month = last_date.strftime("%m")
        last_day = last_date.strftime("%d")
        last_hour = last_date.strftime("%H")
        last_minute = last_date.strftime("%M")
        last_second = last_date.strftime("%S")

        req_url = f'{url}?ursiCode={station_name}&' + \
                f'charName={data_name}&' + \
                'DMUF=3000&' + \
                f'fromDate={origin_year}%2F{origin_month}%2F{origin_day}+{origin_hour}%3A{origin_minute}%3A{origin_second}&' + \
                f'toDate={last_year}%2F{last_month}%2F{last_day}+{last_hour}%3A{last_minute}%3A{last_second}'
        
        return req_url
    
    def _transform_digisonde_giro_str_to_df(self, data_bytes):
        """
        Transform bytes to DataFrame -> cols : Time CS_DataName DataName QD
        """
        data_list = data_bytes.decode('utf-8').split('\n')
        col_names = data_list[19].replace('#','').split()
        data_splitted = [row.split() for row in data_list[20:]]

        if not len(col_names) == 0 and not len(data_splitted[0]) == 0:
            col_names[1] = "CS_" + col_names[2] # To reference the confidence to its data name
            df = pd.DataFrame(data_splitted, columns=col_names)
            df = df.dropna(how='all')
        else:
            df = pd.DataFrame()
        return df
   
    def _get_url_dict(self, url_dict):
        """
        For each url in url_dict get the data

        @param url_dict: The URL dict to retrieve the files from.
        @type url_dict: dict
        @return: DataFrame
        """
        # Get a tuple of each combination ESTATION <-> DATA
        req_couples_list = list(itertools.product(GLOBAL_VARS.STA_DICT.keys(), GLOBAL_VARS.DIGISONDE_GIRO_data.keys()))

        total_df = pd.DataFrame() # DF Container of all new data
        # For each station
        for station_i, data_i in req_couples_list:
            logger.info(f' - Download {station_i} - {data_i}')
            # 1º Look in the data to know the range of dates to request
            # last_date = _get_digisonde_giro_last_date(station_i, data_i)
            # logger.info(f' - Last date is {last_date}')
            # 2º Build request url    
            print(f' - Download {station_i} - {data_i}')
            url_str = self._gen_url_digisonde_giro(station_i, data_i)
            # 3º Request    
            data_bytes = self._get_url(url_str)
            # 4º Transform str to df
            data_df = self._transform_digisonde_giro_str_to_df(data_bytes)
            if not data_df.shape[0] == 0:
                total_df = pd.concat([total_df, data_df], ignore_index=True)
            else:
                logger.info(f'{station_i} and {data_i} has no data.')
            time.sleep(2) # Avoid server saturation
        
        return total_df

    def _save_local_csv(self, df):
        """
        For each url save the csv file in save path set in paths_dict

        @param df: df to be saved
        @type df: df
        @return: None
        """
        folder_path = os.path.join(self.paths_dict['output'], GLOBAL_VARS.DIGISONDE_GIRO_s3_path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        f_name = GLOBAL_VARS.DIGISONDE_GIRO_fn + "_" + self.config['date_hour_str'] + ".csv"
        f_path = os.path.join(folder_path, f_name)
        df.to_csv(f_path, sep=';', index=False)

    def _save_s3_csv(self, df):
        """
        Save CSV files in AWS S3

        @param df: dataframe to be saved
        @type df: df
        @return: None
        """
        f_name = GLOBAL_VARS.DIGISONDE_GIRO_fn + "_" + self.config['date_hour_str'] + ".csv"
        store_in_s3(bucket_name = GLOBAL_VARS.S3_BUCKET_NAME, 
                    s3_path = GLOBAL_VARS.DIGISONDE_GIRO_s3_path, 
                    file_name = f_name, 
                    data = df)
    
    def _save_local_postgresql(self, df):
        """
        Iterate reqs

        @param df: dataframe to be saved
        @type df: df
        @return: None
        """
        store_local_postgresql(db_name=GLOBAL_VARS.DIGISONDE_GIRO_TABLE_NAME, df=df)

    def _transform_df(self, df):
        """
        Agrupate rows around the time in 00, 15, 30, 45 

        @param df: dataframe to be transformed
        @type df: df
        @return: df
        """
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
        store_rds_postgresql()

        if GLOBAL_VARS.DEBUG_MODE:
            df = pd.read_csv()
        else:
            df = self._get_url_dict(url_dict)

        for target_i in target:
            if target_i.lower() == "local_csv":
                self._save_local_csv(df)
            if target_i == "s3_csv":
                self._save_s3_csv(df)
            if target_i == "local_postgresql":
                self._save_local_postgresql(df)

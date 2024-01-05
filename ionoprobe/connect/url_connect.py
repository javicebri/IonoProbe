# connect.py

import os
import json
import requests
import itertools
import GLOBAL_VARS
import pandas as pd
from logger import logger

def req_GOES(url):
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
       logger.warning('REQ ERROR')

def req_digisonde_image(url):
    """
    Get image from URL.

    @param url: The URL to retrieve the file from.
    @type url: str
    @return: The content of the retrieved image.
    @rtype: bytes
    """
    res = requests.get(url)
    if res.status_code == 200:
        return res.content
    else:
       logger.warning('REQ ERROR')

def req_digisonde_plain(url):
    """
    Get plain text from URL.

    @param url: The URL to retrieve the file from.
    @type url: str
    @return: The content of the retrieved str.
    @rtype: str
    """
    res = requests.get(url)
    if res.status_code == 200:
        return res.content
    else:
       logger.warning('REQ ERROR')

def gen_url_digisonde_plain(url, config):
    """
    Generate the url to make the request for https://giro.uml.edu/didbase/scaled.php.

    @param url: base url.
    @type url: str
    @param config: config dictionary.
    @type config: dict
    @return: The url with for the request.
    @rtype: str
    """
    https://lgdc.uml.edu/common/DIDBGetValues?ursiCode=AL945&charName=foF2&DMUF=3000&fromDate=2023%2F07%2F01+21%3A00%3A00&toDate=2024%2F01%2F03+03%3A00%3A00

    # Get a tuple of each combination ESTATION <-> DATA
    req_couples_list = list(itertools.product(GLOBAL_VARS.sta_dict.keys(), GLOBAL_VARS.DIGISONDE_plain_data.keys()))

    # For each station
    for station_i, data_i in req_couples_list:

        origin_year = config["origin_date"]
        origin_month = config["origin_date"]
        origin_day = config["origin_date"]
        origin_hour = config["origin_date"]
        origin_minute = config["origin_date"]
        origin_second = config["origin_date"]

        last_year = config["last_date"]
        last_month = config["last_date"]
        last_day = config["last_date"]
        last_hour = config["last_date"]
        last_minute = config["last_date"]
        last_second = config["last_date"]

        req_url = f'https://lgdc.uml.edu/common/DIDBGetValues?ursiCode={station_i}&' + \
                  f'charName={data_i}&' + \
                  'DMUF=3000&' + \
                  f'fromDate={origin_year}%2F{origin_month}%2F{origin_day}+{origin_hour}%3A{origin_minute}%3A{origin_second}&' + \
                  f'toDate={last_year}%2F{last_month}%2F{last_day}+{last_hour}%3A{last_minute}%3A{last_second}'





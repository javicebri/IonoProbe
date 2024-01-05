# connect.py

import os
import json
import requests
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


    origin_date = config['DIGISONDE_plain_url']["origin_date"]
    origin_year = origin_date.strftime("%Y")
    origin_month = origin_date.strftime("%m")
    origin_day = origin_date.strftime("%d")
    origin_hour = origin_date.strftime("%H")
    origin_minute = origin_date.strftime("%M")
    origin_second = origin_date.strftime("%S")

    last_date = config['DIGISONDE_plain_url']["last_date"]
    last_year = last_date.strftime("%Y")
    last_month = last_date.strftime("%m")
    last_day = last_date.strftime("%d")
    last_hour = last_date.strftime("%H")
    last_minute = last_date.strftime("%M")
    last_second = last_date.strftime("%S")

    req_url = f'{url}?ursiCode={station_i}&' + \
            f'charName={data_i}&' + \
            'DMUF=3000&' + \
            f'fromDate={origin_year}%2F{origin_month}%2F{origin_day}+{origin_hour}%3A{origin_minute}%3A{origin_second}&' + \
            f'toDate={last_year}%2F{last_month}%2F{last_day}+{last_hour}%3A{last_minute}%3A{last_second}'
    req_digisonde_plain(url)

    return req_url





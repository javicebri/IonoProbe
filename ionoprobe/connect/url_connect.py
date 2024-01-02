# connect.py

import json
import requests
import pandas as pd
from logger.logger import logger



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

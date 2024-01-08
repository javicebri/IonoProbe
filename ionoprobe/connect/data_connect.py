# data_connect.py

import os
import datetime
import pandas as pd

def get_digisonde_last_date(paths_dict, station, data):
    """
    Get the last date from DIGISONDE data.

    Parameters:
    @param paths_dict (dict): A dictionary containing file paths.
    @param station (str): The name of the station.
    @param data (str): The type of data.
    Returns:
    @return datetime.datetime: The last date from DIGISONDE data.
    """
    current_date_utc = datetime.datetime.now(datetime.timezone.utc)
    # Check if exist previous data:
    if os.path.exists(paths_dict['data_DIGISONDE_feather_f']):
        df = pd.read_feather(paths_dict['data_DIGISONDE_feather_f'], columns=['Time', 'CS_' + data, data, station])
        df = df.dropna(subset=['Time', 'CS_' + data, data])
        date = df['Time'].max().to_pydatetime()
    else:
        year_ago_date = current_date_utc - datetime.timedelta(days=365)
        year_ago_date = year_ago_date.replace(hour=0, minute=0, second=0, microsecond=0)
        date = year_ago_date
    
    return date

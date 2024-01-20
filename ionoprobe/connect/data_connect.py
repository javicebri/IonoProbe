# data_connect.py

import os
import datetime
import pandas as pd

def get_digisonde_last_date(file_path, station, data):
    """
    Get the last date from DIGISONDE data.

    Parameters:
    @param file_path (str): Path of the file.
    @param station (str): The name of the station.
    @param data (str): The type of data.
    Returns:
    @return datetime.datetime: The last date from DIGISONDE data.
    """
    current_date_utc = datetime.datetime.now(datetime.timezone.utc)
    # Check if exist previous data:
    if os.path.exists(file_path):
        df = pd.read_feather(file_path, columns=['Time', 'CS_' + data, data, station])
        df = df.dropna(subset=['Time', 'CS_' + data, data])
        date = df['Time'].max().to_pydatetime()
    else:
        year_ago_date = current_date_utc - datetime.timedelta(days=365)
        date = year_ago_date.replace(hour=0, minute=0, second=0, microsecond=0)
    
    return date

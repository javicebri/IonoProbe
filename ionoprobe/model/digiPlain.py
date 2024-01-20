# digiPlain.py

import pandas as pd
from logger import logger


def transform_digi_plain_str_to_df(data_bytes):
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


def group_time_quarter_digi_plain_df(df):
    """
    Group in the quarter hh:00, hh:15, hh:30, hh:45. raw df is too sparse because the time of each column can be any minute
    """
    df['Time'] = pd.to_datetime(df['Time']).dt.round('15min')

    df.groupby(['Time', 'CS_foF2']).mean().reset_index()


    df.mean().reset_index()
    return df



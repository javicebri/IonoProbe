# digiPlain.py

import pandas as pd
from logger import logger


def transform_digi_plain_str_to_df(data_bytes):
    """
    Transform bytes to DataFrame -> cols : Time CS_DataName DataName QD
    """
    data_list = data_bytes.decode('utf-8').split('\n')
    col_names = data_list[19].replace('#','').split()
    col_names[1] = "CS_" + col_names[2] # To reference the confidence to its data name
    data_splitted = [row.split() for row in data_list[20:]]
    if not len(data_splitted[0]) == 0:
        df = pd.DataFrame(data_splitted, columns=col_names)
        df = df.dropna(how='all')
    else:
        df = pd.DataFrame()
    return df



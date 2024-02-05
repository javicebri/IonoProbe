import datetime as dt
import json
import os

import GLOBAL_VARS

from tools.datetools import get_now_date_str



def load_config(paths_dict):
    config_fn = os.path.join(paths_dict['config'], GLOBAL_VARS.base_file_names_dict["config_fn"])
    with open(config_fn, 'r') as json_file:
        config_dict = json.load(json_file)
    return config_dict


def validate_config(config_dict):
    pass


def format_config(config):
    """
    Format config file with the expected data, for example datetime variables etc.

    @param config: config file
    @type url: dict
    @return: Dictionary with correct format.
    @rtype: Dictionary
    """
    origin_date = dt.datetime.strptime(config['DIGISONDE_GIRO_url']['origin_date'], "%Y%m%d_%H:%M:%S")
    config['DIGISONDE_GIRO_url']['origin_date'] = origin_date
    last_date = dt.datetime.strptime(config['DIGISONDE_GIRO_url']['last_date'], "%Y%m%d_%H:%M:%S")
    config['DIGISONDE_GIRO_url']['last_date'] = last_date
    config['date_hour_str'] = get_now_date_str()

    return config
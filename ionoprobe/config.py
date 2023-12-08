import datetime as dt
import json


def load_config(paths_dict):
    config_fn = paths_dict['config_fn']
    with open(config_fn, 'r') as json_file:
        config_dict = json.load(json_file)
    return config_dict


def validate_config(config_dict):
    pass


def format_config(config, exec_str):
    exec_dt = dt.datetime.strptime(exec_str, "%Y%m%d_%H%M%S")
    config['exec_dt'] = exec_dt
    config['exec_str'] = exec_str
    return config
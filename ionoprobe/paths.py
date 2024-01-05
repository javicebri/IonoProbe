import GLOBAL_VARS
import os


def get_paths(root):
    paths_dict = {
        'config': os.path.join(root, 'config'),
        'data': os.path.join(root, 'data'),
        'logs': os.path.join(root, 'logs'),
        'output': os.path.join(root, 'output')
    }
    return paths_dict


def format_paths(paths_dict, exec_str):
    for key, value in paths_dict.items():
        paths_dict[key] = value.replace("%exec_time%", exec_str)


def create_paths(root, paths_dict):
    for path_i in paths_dict:
        if not os.path.exists(path_i):
            os.makedirs(path_i)


def add_config_paths(root, paths_dict, config):
    paths_dict['GOES_url'] = config['GOES_url']
    paths_dict['DIGISONDE_image_url'] = config['DIGISONDE_image_url']
    paths_dict['DIGISONDE_plain_url'] = config['DIGISONDE_plain_url']
    paths_dict['output_DIGISONDE'] = os.path.join(paths_dict['output'], 'digisonde_data.feather')
    return paths_dict


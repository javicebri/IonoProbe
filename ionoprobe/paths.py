from . import GLOBAL_VARS
import os


def get_paths(root):
    paths_dict = {
        'config': os.path.join(root, 'config'),
        'config_fn': os.path.join(root, 'config', GLOBAL_VARS.config_file),
        'data': os.path.join(root, 'data'),
        'logs': os.path.join(root, 'logs'),
        'output': os.path.join(root, 'output')
    }
    return paths_dict


def format_paths(paths_dict, exec_str):
    for key, value in paths_dict.items():
        paths_dict[key] = value.replace("%exec_time%", exec_str)


def create_paths(root, paths_dict):
    output_path = os.path.join(root,'output')
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    logs_path = os.path.join(root,'logs')
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)

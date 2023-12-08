import time
import datetime as dt


from .logger import init_logger, logger
from . import GLOBAL_VARS
from .paths import get_paths, create_paths, format_paths
from .config import load_config, format_config, validate_config



def main(root):
    """
    Main execution
    param root: path of the folder with config, output... folders.
    """
    start = time.time()
    exec_dt = dt.datetime.now()
    exec_str = exec_dt.strftime("%Y%m%d_%H%M%S")

    logger = init_logger(root, exec_str)

    logger.info(GLOBAL_VARS.header_art)
    logger.info('Start IONOPROBE: {}'.format(exec_str))

    logger.info('Get paths')
    paths_dict = get_paths(root)
    logger.info('Format paths')
    format_paths(paths_dict, exec_str)
    logger.info('Create path structure')
    create_paths(root, paths_dict)

    logger.info('Read config file')
    config = load_config(paths_dict)
    logger.info('Validate config file')
    validate_config(config)
    logger.info('Format config file')
    format_config(config, exec_str)

    ## Read raw to create csv
    # 1 GOES
    # 2 Digisonde
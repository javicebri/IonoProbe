import time
import datetime as dt


from .logger import init_logger, logger
from . import GLOBAL_VARS


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
    logger.info('Start scraping: {}'.format(exec_str))
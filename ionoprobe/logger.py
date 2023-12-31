import logging
import datetime
import logging.handlers
import sys
import os
from logging import Logger


def init_logger(root, exec_str):
    date = datetime.datetime.now()
    date_str = date.strftime("%Y%m%d_%H%M%S")
    logger_path = os.path.join(root, 'logs', 'log_' + exec_str + '_' + date_str + '.log')
    if not os.path.exists(logger_path):
        with open(logger_path, 'w') as f:
            f.write("")
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    log = logging.getLogger('MyLogger')
    log.setLevel(logging.INFO)
    handler = logging.FileHandler(logger_path)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s:%(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    log.addHandler(handler)

    return log

logger: Logger = logging.getLogger('MyLogger')

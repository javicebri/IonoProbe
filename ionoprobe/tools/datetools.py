from datetime import datetime


def get_now_date_str():
    now_datetime = datetime.now()
    format = "%Y%m%d_%H%M"
    return now_datetime.strftime(format)
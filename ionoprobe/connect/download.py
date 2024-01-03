from logger import logger
from connect.url_connect import req_GOES, req_Digisonde
from connect.aws_connect import store_in_s3


def download_Digisonde(paths_dict):
    """
    Iterate reqs

    @param paths_dict: The URL to retrieve the file from.
    @type url: dict
    @return: The content of the retrieved image.
    @rtype: bytes
    """
    for path_i in paths_dict.keays():
         image_bytes = req_Digisonde(paths_dict[path_i])
        # if config is local save in folder, if is aws save in s3


def download_GOES(paths_dict):
    """
    Iterate reqs

    @param paths_dict: The URL to retrieve the file from.
    @type paths_dict: dict
    @return: The content of the retrieved image.
    @rtype: DataFrame
    """
    for path_i in paths_dict.keays():
        data_df = req_GOES(paths_dict['path_i'])
        # if config is local save in folder, if is aws save in s3

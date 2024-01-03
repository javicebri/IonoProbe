from logger import logger
from connect.url_connect import req_GOES, req_Digisonde
from connect.aws_connect import store_in_s3


def download_Digisonde(paths_dict, config):
    """
    Iterate reqs

    @param paths_dict: The URL to retrieve the file from.
    @type url: dict
    @param config: config file
    @type url: dict
    @return: The content of the retrieved image.
    @rtype: bytes
    """
    for path_i in paths_dict.keys():
        image_bytes = req_Digisonde(paths_dict[path_i])
        # if config is local save in folder, if is aws save in s3
        if "local" in config['save']:
            # print('Finish')
            # # with open('output.json', 'w') as file:
            # #     json.dump(data_json, data_json, indent=4)  # indent opcional para formato legible
            pass
        if "s3" in config['save']:
            # store_in_s3(bucket_name = 'ionoprobe', s3_path = 'DIGISONDE', file_name = 'prueba.png', data = image_bytes)
            pass


def download_GOES(paths_dict, config):
    """
    Iterate reqs

    @param paths_dict: The URL to retrieve the file from.
    @type paths_dict: dict
    @param config: config file
    @type url: dict
    @return: The content of the retrieved image.
    @rtype: DataFrame
    """
    for path_i in paths_dict.keys():
        data_df = req_GOES(paths_dict['path_i'])
        # if config is local save in folder, if is aws save in s3
        if "local" in config['save']:
            pass
        if "s3" in config['save']:
            # store_in_s3(bucket_name = 'ionoprobe', s3_path = 'DIGISONDE', file_name = 'prueba.png', data = data_df)
            pass

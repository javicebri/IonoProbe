# image.py
import io
import pytesseract
import GLOBAL_VARS
import pandas as pd

from PIL import Image
from logger import logger

# sudo apt install tesseract-ocr

def get_str_from_image(image_bytes):
    """
    Get text from image in bytes format
    @param image_bytes: Bytes representing the image
    @type image_bytes: bytes
    @return: Extracted text from the image
    @rtype: str
    """
    try:
        pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
        imagen_pil = Image.open(io.BytesIO(image_bytes))
        extracted_text = pytesseract.image_to_string(imagen_pil)
        return extracted_text
    except Exception as e:
        print(f"Error during image extraction")
        exit(-1)


def transform_str_to_df(image_str):
    """
    Transform the Digisonde str to the expected pandas dataframe. Digisonde has a standard data table.
    @param image_str: String representing the image
    @type image_bytes: str
    @return: Expected Digisonde DataFrame
    @rtype: DataFrame
    """
    image_list = image_str.split('\n')

    # Extract Station Name, Date and General Data
    # station_legend_pos = next((i for i, elem in enumerate(image_list) if elem.startswith('Station')), None)
    # station_legend = image_list[station_legend_pos].replace("_","").split(" ")
    station_legend = GLOBAL_VARS.STATION_LEGEND
    station_data = image_list[4].split(" ")
    if not len(station_data) == len(station_legend):
        logger.error('Error station_legend DIGISONDE ETL')
    else:
        station_df = pd.DataFrame([station_data], columns=station_legend)


    # st_splt = station_data.split(" ")
    # station_name = st_splt[0]
    # station_year = st_splt[1]
    # station_MMMDD = st_splt[2]
    # station_HHMMSS = st_splt[4]





    df = pd.DataFrame()
    return df

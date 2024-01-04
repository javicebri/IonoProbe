# image.py

from PIL import Image
import pytesseract
import io

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

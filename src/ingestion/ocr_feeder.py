# pip install pytesseract
# https://github.com/tesseract-ocr/tesseract/wiki/Downloads

import pytesseract
from PIL import Image
# add path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'Path to the tesseract executable'

# add path to the image
img = Image.open(r'Path to the image')
text = pytesseract.image_to_string(img)
print(text)
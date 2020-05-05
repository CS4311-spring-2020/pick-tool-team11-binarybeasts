# pip install pytesseract
# https://github.com/tesseract-ocr/tesseract/wiki/Downloads

import pytesseract
from PIL import Image
import pandas as pd

# add path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\jlluj\AppData\Local\Tesseract-OCR\tesseract.exe'

# add path to the image
img = Image.open(r'C:\Users\jlluj\Documents\PICK\pick-tool-team11-binarybeasts\src\ingestion\testimage.jpg')
text = pytesseract.image_to_string(img)
print(text)
saveFile = open('ingestion\ImageToText.txt', 'w')
saveFile.write(text)
saveFile.close()

data = pd.read_csv("ImageToText.txt",delimiter=',')
data.to_csv(r'C:\Users\jlluj\Documents\PICK\pick-tool-team11-binarybeasts\src\ingestion\imageCSV.csv')
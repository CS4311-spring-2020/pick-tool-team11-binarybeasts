#pip install regex
import regex as re
import pandas as pd
import numpy as np

class Cleansing:

    def cleanse(str):
        df = pd.read_csv('pathLocation/of/file.csv')
        # looks at the entries
        df.head()



#def remove_control_characters(str):
 #   return re.sub(r'\p{C}', '', 'my-string')
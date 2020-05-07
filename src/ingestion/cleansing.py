#pip install regex
#pip install pandas
import regex as re
import pandas as pd
import numpy as np
import csv
from configuration.configurations import Configuration
from threading import Thread
from ingestion.splunk_interface import SplunkInterface

class Cleansing:

    def cleanse(str):

        data = pd.read_csv(r'C:\pathToTheFile\prices.csv')
        #Examine the shape of the data
        data.shape
        #Explore null cells
        data.isnull()
        #View total of null values by column
        data.isnull().sum()
        # Remove rows where all values are missing
        data.dropna(inplace = True, how='all')
        #Remove all null values
        data=data.dropna()

        #Store the dataframe as a new CSV
        data.to_csv(r'C:\pathToTheFile\cleansed.csv',index=False)


configuration = Configuration.get_instance()
if configuration.splunk != None:
all_log_entries = configuration.splunk.get_log_entries()

if (all_log_entries == )

    def get_log_entries_thread(self, configuration):
        if configuration.splunk:
            all_log_entries = configuration.splunk.get_log_entries()
            self.insert_log_entry_search_data(all_log_entries)



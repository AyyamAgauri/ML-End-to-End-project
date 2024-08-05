import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass #Use for directly define the class variables.

#Input for Data Ingestion component. Where to save data after reading
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train_data.csv')
    test_data_path:str = os.path.join('artifacts','test_data.csv')
    raw_data_path:str = os.path.join('artifacts','raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    #Main function to read data
    def main_func(self):
        logging.info('Data Ingestion Started')

        try:
            df = pd.read_csv('notebook\Data.csv')
            logging.info('Data read as DataFrame')

            #Starts making artifacts directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
        except:
            pass
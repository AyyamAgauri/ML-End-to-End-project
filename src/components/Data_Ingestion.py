import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.Data_Transform import DataTransformConfig
from src.components.Data_Transform import DataTransformer
from src.components.Model_trainer import ModelTrainer
from src.components.Model_trainer import ModelTrainerConfig

@dataclass #Automatically generates special methods for classes like __init__.

#Input for Data Ingestion component. Where to save data after reading
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train_data.csv')
    test_data_path:str = os.path.join('artifacts','test_data.csv')
    raw_data_path:str = os.path.join('artifacts','raw_data.csv')

#Without the __init__ function we had to manually setup the attributes which can lead to errors.
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    #Main function to read data
    def main_func(self):
        logging.info('Data Reading Started')

        try:
            #Data can be read from any source from this code line.
            df = pd.read_csv('notebook\Data.csv')
            logging.info('Data Ingestion Started')

            #Artifacts directory created using train_file_path
            #os.path.dir.name returns the Folder/directory path in which the file is specified
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            #Raw Data csv file created
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('Train Test Split Started')

            train_set, test_set = train_test_split(df,test_size=0.2,random_state=69)

            #train  &test data csv files created
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info('Data Ingestion Completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == '__main__':
    obj = DataIngestion()
    train_data, test_data = obj.main_func()

    data_transformation = DataTransformer()
    train_arr,test_arr,_ = data_transformation.intiate_data_transform(train_data,test_data)

    modeltrainer = ModelTrainer()
    modeltrainer.initiate_model_trainer(test_arr,test_arr)
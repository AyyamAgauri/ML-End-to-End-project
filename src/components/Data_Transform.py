import os
import sys

from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from dataclasses import dataclass

from src.utils import save_object

@dataclass
class DataTransformConfig:
    preprocessor_object_file = os.path.join('artifacts','preprocessor.pkl')

class DataTransformer:
    def __init__(self):
        self.data_transformation_config = DataTransformConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns = ['writing_score','reading_score']
            categorical_columns = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
            ] 

            num_pipeline = Pipeline(
                steps=[
                    ('Impute',SimpleImputer(strategy='median')),
                    ('Scaler',StandardScaler(with_mean=False))
                ]
            )

            logging.info('Numerical Columns Scaling Completed')

            cat_pipeline = Pipeline(
                steps=[
                    ('Impute',SimpleImputer(strategy='most_frequent')),
                    ('Encode',OneHotEncoder()),
                    ('Scaler',StandardScaler(with_mean=False))
                ]
            )

            logging.info("Categorical Columns Encoding Completed.")

            #Combining both pipelines
            preprocessor = ColumnTransformer(
                transformers=[
                    ('Num_pipeline',num_pipeline,numerical_columns),
                    ('cat_pipeline',cat_pipeline,categorical_columns)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)


    def intiate_data_transform(self,train_path,test_path):
            try:
                train_df = pd.read_csv(train_path)
                test_df = pd.read_csv(test_path)

                logging.info('Data Reading Started')
                logging.info('Obtaining Preprocessor object')

                preprocessor_obj = self.get_data_transformer_object()

                target_column = 'math_score'

                input_feature_train_df = train_df.drop(columns = [target_column],axis=1)
                target_feature_train_df = train_df[target_column]

                input_feature_test_df = test_df.drop(columns = [target_column],axis=1)
                target_feature_test_df = test_df[target_column]

                logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
                )

                input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
                input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)

                train_arr = np.c_[
                    input_feature_train_arr, np.array(target_feature_train_df)
                ]
                test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

                logging.info(f"Saved preprocessing object.")

                save_object(

                    file_path=self.data_transformation_config.preprocessor_object_file,
                    obj=preprocessor_obj

                )

                return (
                    train_arr,
                    test_arr,
                    self.data_transformation_config.preprocessor_object_file
                )
            except Exception as e:
                raise CustomException(e,sys)

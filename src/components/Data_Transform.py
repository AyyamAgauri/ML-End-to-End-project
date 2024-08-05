import os
import sys

from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataTransformConfig:
    preprocessor_object_file = os.path.join('artifacts','preprocessor.pkl')

class DataTransformer:
    def __init__(self):
        self.data_transformation_config = DataTransformConfig()

    def get_data_transformer_object(self):
        try:
            pass
        except:
            pass

import numpy as np
import pandas as pd

import os
import sys
import dill
from src.exception import CustomException

#for the creation of pkl file
def save_object(file_path, obj):
    try:
        dir_name = os.path.dirname(file_path)

        os.makedirs(dir_name,exist_ok=True)
        
        with open(dir_name,'wb') as f:
            dill.dump(obj,f)
    except Exception as e:
        raise CustomException(e,sys)
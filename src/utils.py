import numpy as np
import pandas as pd

import os
import sys
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

#for the creation of pkl file
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    

#For Evaluating models trained in src/components/models.py

def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}

        for i in range(len(models)):
            #Accessing every model present one by one
            model = list(models.values())[i]

            #Hyperparameter Tuning
            # gs = GridSearchCV(model,cv=3)
            # gs.fit(X_train,y_train)

            #Setting the best hyperparameter
            # model.set_params(**gs.best_params_)

            #Training model
            model.fit(X_train,y_train)
            #Train Output prediction
            y_train_pred = model.predict(X_train)
            #Test Output prediction
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_model_score

            return report
    except Exception as e:
        raise CustomException(e,sys)
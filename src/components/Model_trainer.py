import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    RandomForestRegressor,
    GradientBoostingRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_model


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info('Data Splitting Started as Train & Test Data')

            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            #List of models to test on.
            models = {
                'Random Forest' : RandomForestRegressor(),
                'Decision Tree' : DecisionTreeRegressor(),
                'Gradient Boosting' : GradientBoostingRegressor(),
                'Linear Rregression' : LinearRegression(),
                'K-Nearest Neighbours' : KNeighborsRegressor(),
                'XgBoost Regressor' : XGBRegressor(),
                'SVM' : SVR(),
                'CatBoost Regressor' : CatBoostRegressor(),
                'AdaBoost Regressor' : AdaBoostRegressor()
            }

            model_report:dict = evaluate_model(X_train=X_train,
                                               y_train=y_train,
                                               X_test=X_test,
                                               y_test=y_test,
                                               models=models
            )

            #Get the Best r2_score from report dict
            best_model_score = max(sorted(model_report.values()))

            #Get the best r2_score model name
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score<0.7:
                raise CustomException("No best model found")
            
            logging.info(f'Best model found {best_model} with r2_score {best_model_score}')

            
        except:
            pass
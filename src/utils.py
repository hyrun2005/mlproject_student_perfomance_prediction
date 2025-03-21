import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from sklearn.model_selection import GridSearchCV
from src.logger import logging
import dill
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e, sys)


def evaluate_model(X_train, y_train, X_test, y_test, models:dict, params:dict):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]

            clf = GridSearchCV(model, param, cv=3)
            clf.fit(X_train, y_train)

            model.set_params(**clf.best_params_)
            model.fit(X_train, y_train)

            y_test_predicted = model.predict(X_test)

            test_model_score = r2_score(y_test, y_test_predicted)

            report[list(models.keys())[i]] = test_model_score

        return report
    
    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)

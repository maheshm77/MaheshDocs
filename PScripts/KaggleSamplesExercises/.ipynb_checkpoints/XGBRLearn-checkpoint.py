import pandas as pd
import numpy as np
import csv
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, LabelEncoder, Imputer
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble.partial_dependence import partial_dependence, plot_partial_dependence
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from xgboost import XGBRegressor


def getTrainMAE():
    trn_data_fromCSV = pd.read_csv("./Input/train.csv")
    trn_data = trn_data_fromCSV.fillna(0)
    trn_data_dummies = pd.get_dummies(trn_data)            
    
    features = trn_data_dummies.axes[1]
    X = trn_data_dummies[features]
    y = trn_data_dummies.SalePrice


    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

    my_model = RandomForestRegressor(random_state=1, n_estimators=100)
    my_model.fit(train_X, train_y)
    predictedSalePrices = my_model.predict(val_X)
    print("Mean Absolute Error using RandomForestRegressor: ", mean_absolute_error(val_y, predictedSalePrices))


    train_X2, val_X2, train_y2, val_y2 = train_test_split(X, y, random_state=1)

    my_pipeline = make_pipeline(SimpleImputer(), XGBRegressor(random_state=1, n_estimators=1000, early_stopping_rounds = 5, learning_rate=0.05))
    my_pipeline.fit(train_X2, train_y2)
    predictedSalePrices2 = my_pipeline.predict(val_X)

    print("Mean Absolute Error using XGBRegressor: ", mean_absolute_error(val_y2, predictedSalePrices2))
    
    
    scores = cross_val_score(my_pipeline, X, y, scoring='neg_mean_absolute_error', cv=5)
    #print(scores)
    print('Mean Absolute Error %2f' %(-1 * scores.mean()))
    return
    
getTrainMAE()
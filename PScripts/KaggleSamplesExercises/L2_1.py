import pandas as pd
import numpy as np
import csv
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, LabelEncoder

#### Make X for the model
training_data_fromCSV = pd.read_csv("/Users/maheshmachapalli/MaheshDocs/PScripts/KaggleSamplesExercises/Input/train.csv")
training_data = training_data_fromCSV.fillna(0)
#training_data = training_data_fromCSV.dropna(how='any') #Need to find a way to remove only those rows.

#print ("training_data_fromCSV size : ", training_data_fromCSV.size)
#print ("training_data size : ", training_data.size)


missing_val_count_by_column = (training_data_fromCSV.isnull().sum())
#print(missing_val_count_by_column[missing_val_count_by_column > 0])

#print (training_data_fromCSV) #[1460 rows x 81 columns]
data_without_missing_values = training_data_fromCSV.dropna(axis=1) #[1460 rows x 62 columns]

#print (data_without_missing_values)

from sklearn.impute import SimpleImputer
my_imputer = SimpleImputer()
data_with_imputed_values = my_imputer.fit_transform(pd.get_dummies(training_data_fromCSV))
#print (data_with_imputed_values)



# make copy to avoid changing original data (when Imputing)
new_data = pd.get_dummies(training_data_fromCSV).copy()

# make new columns indicating what will be imputed
cols_with_missing = (col for col in new_data.columns 
                                 if new_data[col].isnull().any())
for col in cols_with_missing:
    new_data[col + '_was_missing'] = new_data[col].isnull()

print(new_data)

print (pd.get_dummies(training_data_fromCSV))


# Imputation
#my_imputer = SimpleImputer()
#new_data = pd.DataFrame(my_imputer.fit_transform(new_data))
#new_data.columns = pd.get_dummies(training_data_fromCSV).columns

#print(new_data)

from xgboost import XGBRegressor
my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05)
my_model.fit(train_X, train_y, early_stopping_rounds=5, 
             eval_set=[(test_X, test_y)], verbose=False)
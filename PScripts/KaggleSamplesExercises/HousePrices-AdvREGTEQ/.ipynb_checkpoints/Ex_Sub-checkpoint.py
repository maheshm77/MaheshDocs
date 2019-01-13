import pandas as pd
import numpy as np
import csv
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
from sklearn.ensemble.partial_dependence import partial_dependence, plot_partial_dependence
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Imputer
import TestEx_Sub as t



#### STEP 1
#### Read training data & test data from their respective CSV files - BEGIN
training_data_fromCSV = pd.read_csv("./Input/train.csv")
training_data = training_data_fromCSV.fillna(0)
#print ("training_data_fromCSV size : ", training_data_fromCSV.size)
#print ("training_data size : ", training_data.size)

test_data_fromCSV = pd.read_csv("./Input/test.csv")
test_data = test_data_fromCSV.fillna(0)
#print ("test_data_fromCSV size : ", test_data_fromCSV.size)
#print ("test_data size : ", test_data.size)
#### Read training data & test data from their respective CSV files - END


#### Make y for the model from training data - BEGIN
training_data_price = training_data.SalePrice
#### Make y for the model from training data - END

#### STEP 2

#### Convert categorical variables into dummy/indicator variables - BEGIN
### get_dummies is used to get one-hot encoding
training_data_dummies = pd.get_dummies(training_data)            
test_data_dummies = pd.get_dummies(test_data)
#### Convert categorical variables into dummy/indicator variables - BEGIN


#### STEP 3

#### Get features common to both training data & test data. - BEGIN

## Get axes to check the common features - BEGIN
list_training_data_dummies_axes = training_data_dummies.axes
list_test_data_dummies_axes = test_data_dummies.axes
## Get axes to check the common features - END

#print("list_training_data_xSet_dummies_axes - 1 : ", len(list_training_data_dummies_axes[1]))
#print("list_test_data_xSet_dummies_axes - 1 : ", len(list_test_data_dummies_axes[1]))

features_list = [];

#comparing value of two lists
for item in list_training_data_dummies_axes[1]:
    #print("item : ", item)
    for item1 in list_test_data_dummies_axes[1]:
        if item == item1:
             features_list.append(item)

#print ("\n\n\n\nfeatures_list length : ", len(features_list))
#### Get features common to both training data & test data. - END


#### STEP 4

#### Make X for the model - BEGIN
training_data_dummies_xSet = training_data_dummies [features_list]
test_data_dummies_xSet = test_data_dummies [features_list]
#### Make X for the model - END


#impute the data // Imputer didn't made any difference.. MAE was same in both cases when tried to predict with training data only
imputer = SimpleImputer()
#imp_train_X = pd.DataFrame(imputer.fit_transform(training_data_dummies_xSet))
#imp_test_X = pd.DataFrame(imputer.fit_transform(test_data_dummies_xSet))
imp_train_X = training_data_dummies_xSet
imp_test_X = test_data_dummies_xSet

#### Create model, fit training data with the common features - BEGIN
my_model = RandomForestRegressor(random_state=1, n_estimators=100)

#from sklearn.model_selection import train_test_split #TEMP
#train_X, val_X, train_y, val_y = train_test_split(imp_train_X, training_data_price, random_state=1) #TEMP
#my_model.fit(train_X, train_y) #TEMP
#print("Mean Absolute Error using RandomForestRegressor: \n ", mean_absolute_error(val_X, val_y)) #TEMP

my_model.fit(imp_train_X, training_data_price)
#### Create model, fit training data with the common features - END


#### STEP 5

#### Predict SalePrice, using test data with the common features - BEGIN
predictedSalePrices = my_model.predict(imp_test_X)

#print("Mean Absolute Error from Imputation: \n ", mean_absolute_error(training_data_price, predictedSalePrices))

##############print("\n\n\n : predictedSalePrice : ", predictedSalePrices)


my_submission = pd.DataFrame({'Id': test_data_dummies.Id, 'SalePrice': predictedSalePrices})
my_submission.to_csv('./Output/submissionRFG.csv', index=False)

#### Predict SalePrice, using test data with the common features - END


#my_modelXGB = XGBRegressor()
my_modelXGB = XGBRegressor(n_estimators=1000, early_stopping_rounds = 5, learning_rate=0.05)

my_modelXGB.fit(imp_train_X, training_data_price, verbose=False)
predictions = my_modelXGB.predict(imp_test_X)

my_submission2 = pd.DataFrame({'Id': test_data_dummies.Id, 'SalePrice': predictions})
my_submission2.to_csv('./Output/submission.csv', index=False)

t.getMAE()

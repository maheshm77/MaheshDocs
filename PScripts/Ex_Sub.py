import pandas as pd
import numpy as np
import csv
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, LabelEncoder


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


#### Convert categorical variables into dummy/indicator variables - BEGIN
training_data_dummies = pd.get_dummies(training_data)            
test_data_dummies = pd.get_dummies(test_data)
#### Convert categorical variables into dummy/indicator variables - BEGIN


#### Make y for the model from training data - BEGIN
training_data_price = training_data.SalePrice
#### Make y for the model from training data - END


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


#### Make X for the model - BEGIN
training_data_dummies_xSet = training_data_dummies [features_list]
test_data_dummies_xSet = test_data_dummies [features_list]
#### Make X for the model - END

#### Create model, fit training data with the common features - BEGIN
my_model = RandomForestRegressor(random_state=1)
my_model.fit(training_data_dummies_xSet, training_data_price)
#### Create model, fit training data with the common features - END

#### Predict SalePrice, using test data with the common features - BEGIN
predictedSalePrices = my_model.predict(test_data_dummies_xSet)

#print("\n\n\n : predictedSalePrice : ", len(predictedSalePrices))

my_submission = pd.DataFrame({'Id': test_data_dummies.Id, 'SalePrice': predictedSalePrices})
my_submission.to_csv('./Output/submission.csv', index=False)

#### Predict SalePrice, using test data with the common features - END
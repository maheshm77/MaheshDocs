import pandas as pd
import numpy as np
import csv
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, LabelEncoder

#### Make X for the model
training_data_fromCSV = pd.read_csv("/Users/maheshmachapalli/MaheshDocs/PScripts/KaggleSamplesExercises/Input/train.csv")
training_data = training_data_fromCSV.fillna(0)
#training_data = training_data_fromCSV.dropna(how='any') #Need to find a way to remove only those rows.

print ("training_data_fromCSV size : ", training_data_fromCSV.size)
print ("training_data size : ", training_data.size)

test_data_fromCSV = pd.read_csv("/Users/maheshmachapalli/MaheshDocs/PScripts/KaggleSamplesExercises/Input/test.csv")
test_data = test_data_fromCSV.fillna(0)
print ("test_data_fromCSV size : ", test_data_fromCSV.size)
print ("test_data size : ", test_data.size)


#print ("\n\n\nIndex: ", test_data.index)
#print ("axes: ", test_data.axes)
#print ("ndim: ", test_data.ndim)
#print ("size: ", test_data.size)
#print ("shape: ", test_data.shape)
#print ("memory_usage: ", test_data.memory_usage)
#print ("memory_usage: ", test_data.describe())
#print ("\n\n\nIndex: ", training_data.index, "\n\n\n\n\n\n")
#print (training_data.describe())


training_data_price = training_data.SalePrice

training_data_dummies = pd.get_dummies(training_data)

#enc = OrdinalEncoder()
#enc.fit_transform(training_data_xSet.head())
#print ("Categories :- ", enc.categories_)
#enc.transform(training_data_xSet.head())
#enc.transform(training_data_xSet.head()) #.toarray()
#print ("training_data_xSet.axes :- ", training_data_xSet_dummies.axes)

list_training_data_dummies_axes = training_data_dummies.axes
            
#test_data_xSet = test_data [features]
test_data_dummies = pd.get_dummies(test_data)

list_test_data_dummies_axes = test_data_dummies.axes


#### Get features common to both training data & test data. - BEGIN
features_list = [];

print("list_training_data_xSet_dummies_axes - 1 : ", len(list_training_data_dummies_axes[1]))
print("list_test_data_xSet_dummies_axes - 1 : ", len(list_test_data_dummies_axes[1]))

with open('train.txt', 'w') as f:
    for item in list_training_data_dummies_axes[1]:
        f.write("%s\n" % item)
        
with open('test.txt', 'w') as f:
    for item in list_test_data_dummies_axes[1]:
        f.write("%s\n" % item)
        
        
#comparing value of two list
for item in list_training_data_dummies_axes[1]:
    #print("item : ", item)
    for item1 in list_test_data_dummies_axes[1]:
        if item == item1:
             features_list.append(item)

            
#print ("\n\n\n\nfeatures_list  : ", features_list)
print ("\n\n\n\nfeatures_list length : ", len(features_list))
#### Get features common to both training data & test data. - END

#### Make X for the model
training_data_dummies_xSet = training_data_dummies [features_list]
test_data_dummies_xSet = test_data_dummies [features_list]

my_model = RandomForestRegressor(random_state=1)
my_model.fit(training_data_dummies_xSet, training_data_price)

predictedSalePrice = my_model.predict(test_data_dummies_xSet) #This needs to be enabled?????? - TASK 2

print("\n\n\n : predictedSalePrice : ", predictedSalePrice)
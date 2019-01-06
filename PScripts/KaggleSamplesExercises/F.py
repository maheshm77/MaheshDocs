import pandas as pd

#print ("Hello")
melbourne_data = pd.read_csv("/Users/maheshmachapalli/MaheshDocs/PScripts/KaggleSamplesExercises/Input/train.csv")

print (melbourne_data.columns)

melbourne_data.dropna(axis=0)
y = melbourne_data.SalePrice

print (y.head())

df = melbourne_data.describe()
df.to_csv ("/Users/maheshmachapalli/MaheshDocs/PScripts/KaggleSamplesExercises/Output/trainO.csv", "\t")

#print ("Printing only SalePrice: ")
#print (y.describe())
print ("y.head...", y.head())

melbourne_features = ['TotalBsmtSF', 'GrLivArea', 'LotArea', 'YearBuilt', 'YearRemodAdd']

x = melbourne_data[melbourne_features]

#print ("Printing only selected features: ")
#print (x.describe())


#print ("Printing head of only the selected features: ")
#print (x.head())

from sklearn.tree import DecisionTreeRegressor

melbourne_model = DecisionTreeRegressor(random_state=1)

melbourne_model.fit(x, y)

print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(melbourne_model.predict(x.head()))



feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

x = melbourne_data [feature_names]
#print(x.describe())
#print(x.head())

#print("\n\n\nMaking predictions using iowa model:")

iowa_model = DecisionTreeRegressor(random_state=1)

iowa_model.fit(x,y)

#print (iowa_model.predict(x.head()))
#print ("Printing y..... : ", y.head())

from sklearn.metrics import mean_absolute_error

predicted_home_prices = iowa_model.predict(x)
myMAE = mean_absolute_error(y, predicted_home_prices)
#print ("MAE : ", myMAE)


#print("Working with trains... \n\n\n")
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(x, y, random_state = 0)
# Define model
new_melbourne_model = DecisionTreeRegressor()
# Fit model
new_melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = new_melbourne_model.predict(val_X)
#print (val_predictions.head())

#print (val_predictions.SalePrice)

#print(mean_absolute_error(val_y, val_predictions))


#print ("\n\n\nUnderfitting OR Overfitting : Right fitting\n\n\n")

def getMAE(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]

# Write loop to find the ideal tree size from candidate_max_leaf_nodes
scores = {leaf_size: getMAE(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
best_tree_size = min(scores, key=scores.get)

final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)

final_model.fit(x, y)

#print ( final_model.predict(x.head()) )


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
#forest_model.fit(train_X, train_y)
#melb_preds = forest_model.predict(val_X)
#print("\n\n\n\n\n\n\n", mean_absolute_error(val_y, melb_preds))


forest_model.fit(x, y)
melb_preds = forest_model.predict(x.head())
#print ("\n\n\n\n\n\n", melb_preds)
#print ("MAE: ", mean_absolute_error(y, melb_preds))
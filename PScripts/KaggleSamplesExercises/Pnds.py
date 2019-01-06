import pandas as pd

df = pd.DataFrame ([["Alex", 123], ["Jim", 456]], columns=["Name", "ID"])

df = pd.DataFrame ([[30, 21]], columns=["Apples", "Bananas"])

df = pd.DataFrame ([[35, 21], [41, 34]], columns=["Apples", "Bananas"], index=["2017 Sales", "2018 Sales"])

se = pd.Series (name="Dinner", data=["4 cups", "1 cup", "2 large", "1 can"], index=["Flour", "Milk", "Eggs", "Spam"])

print (df)
#print ("\n\n\n df.iloc[0] : ", df.iloc[0])
#print ("\n\n\n df.iloc[1] : ", df.iloc[1])
#print ("\n\n\n df.iloc[:, 1] : ", df.iloc[:, 1])

print ("\n\n\n df.loc[0] : ", df.loc['2017 Sales'])
print ("\n\n\n df.loc[:, 1] : ", df.loc[:, 'Apples'])


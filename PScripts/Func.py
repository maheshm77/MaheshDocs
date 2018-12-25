#import Timesample
#from Timesample import getCurrTime

import Timesample

print("Current time from Func is ", Timesample.getCurrTime())


#str = input("Enter your input: ")
#print ("Received input is : ", str)

myFile = open("/Users/maheshmachapalli/MaheshDocs/PScripts/AdvPyScrpts/GITCMNDS", "r+")

print ( myFile.read(10) )

myFile.write("pull, add, commit\npush")
import os
os.rename("/Users/maheshmachapalli/MaheshDocs/PScripts/AdvPyScrpts/GITCMNDS","/Users/maheshmachapalli/MaheshDocs/PScripts/AdvPyScrpts/GITCMNDS2")
myFile.close()
print (myFile.closed)
print (myFile.name)
print (myFile.newlines)
print (myFile.mode)





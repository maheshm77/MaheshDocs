
import re

line = "Cats are smarter than dogs and other animals"

searchObj = re.search( r'(.*) smarter (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
   print ("searchObj.group(2) : ", searchObj.groups())
else:
   print ("Nothing found!!")
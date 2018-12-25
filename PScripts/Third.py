import sys

try:
   # open file stream
   file_name="One.py"
   file = open(file_name, "w")
except IOError:
   print ("There was an error writing to", file_name)
   sys.exit()
file_two="FirstPY2.py"
print ("Enter '", file_two)
print ("' When finished")
while file_two != file_name:
   #file_text = raw_input("Enter text: ")
   if file_two == file_name:
      # close the file
      file.close
      break
   file.write(file_two)
   file.write("\n")
file.close()
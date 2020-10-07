# importing required modules 
from zipfile import ZipFile 
  
# specifying the zip file name 
file_name = "intershipfile.zip"
  
# opening the zip file in READ mode 
zip = ZipFile(file_name, 'r')
# printing all the contents of the zip file 
zip.printdir() 
# extracting all the files 
print('Extracting all the files now...') 
zip.extractall() 
print('extract done!') 

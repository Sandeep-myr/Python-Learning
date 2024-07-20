import os 

#  if i want to create new directory in my local system then i use this function
# y = "Allen"
# try:
#     os.mkdir(f"C:\\Users\\sandeepsahu\\Music\\{y}")
#     print("Directory created successfully")
# except :
#     print("Directory already exists")    


#  perform some reading and writing operations inside my directory then i am using this function]

# try:
#   file =  open("C:\\Users\\sandeepsahu\\Music\\Allen\\test.txt", "r") 
#   print(file.read())
# except :
#     print("Unable to open the file")
    
# write()
# read()
# open()
# read(numberOfCharacters)
# readLine() complete line i write 

 
# try:
#   file =  open("C:\\Users\\sandeepsahu\\Music\\Allen\\test.txt" , "r")
# #   file.write("") 
#   print(file.read())
#   file.close()
# except :
#     print("Unable to open the file")
    
#  delete the file from operating system
try:
    os.remove("C:\\Users\\sandeepsahu\\Music\\Allen\\test.txt")
except:
    print("Unable to delete the file because it is not exist")               
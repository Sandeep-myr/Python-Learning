import re 

fruits = "Mango is a seasonal fruit"

x = re.search("^Mango.*seasonal fruit$", fruits)

if x:
    print("Match found")
else:
    print("No match")    
    
print("------------------------------------------------------------------------------------------------")
x = re.findall("al", fruits)
print(x)    
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
else:
    print("The loop has ended")  
    
# using the range function for control statements it is printing all the less value from 0 to range number but range number is excluded

for i in range(6):
    print(i)
    
print("--------------------------------------------------------------------------------------------------------------------------------")    
for i in range(3,7):
    print(i)    
print("--------------------------------------------------------------------------------------------------------------------------------")    

for i in range(3,15,2):
    print(i)    
  
print("--------------------------------------------------------------------------------------------------------------------------------")    
month_name_list = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
month_number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Using zip to pair month names with month numbers
for number, name in zip(month_number_list, month_name_list):
    print(f"{number} : {name}")
print("--------------------------------------------------------------------------------------------------------------------------------")    

# Using nested loops to match month numbers with month names
for i in range(len(month_name_list)):
    for j in range(len(month_number_list)):
        if i == j:
            print(month_number_list[j], ":", month_name_list[i])
   
    

    
    



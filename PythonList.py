fruits_list = ["banana", "Apple", "Banana" ] 
print(fruits_list)

object_list = list(("apple", "*args", "mango"))
print(object_list)
print(type(object_list))

#  new in the python is here negetive indexing is also working

print(fruits_list[-1])  # Output: Banana
print(fruits_list[-2])  # Output: Apple

#  perticular range printing

print(fruits_list[0:4])  # Output: ['Apple', 'Banana']
print(fruits_list[:1])  # Output: ['Apple', 'Banana']
print(fruits_list[1:])  # Output: ['Apple', 'Banana']

#  we have alos check the perticular value is exist in the list or not 


print("Apple" in fruits_list)  # Output: True
print("orange" in fruits_list)  # Output: False

# replace the 0 to 3 element value by the single value 
thislist = ["apple", "banana", "cherry"]
thislist[0:4] = ["watermelon"]
print(thislist)

#  i have inserted one new value inside the list at the position 1 
fruits_list.insert(1,"kharbuja")
print(fruits_list)

# append new value inside the existing list

fruits_list.append("mango")
print(fruits_list)

#  extend method is used to merge two list into the single list 
fruits_list.extend(thislist)
print(fruits_list)

#  remove the data from list 

fruits_list.remove("banana")
print(fruits_list)

#  by using the pop method we have remove the any value from list 

fruits_list.pop(0)
print(fruits_list)

#  remove the last object from the map

fruits_list.pop()
print(fruits_list)

#  using del property we have to remove the value from specific position 

del fruits_list[1]
print(fruits_list)

# clear the complete list data 

fruits_list.clear()
print(fruits_list)

# ======================================================================================

#  use the loop inside the list 

crickter_list = ["Virat Kohli","Rohit sharma","Shivam Dubey","Ravindra Jadeja","Hardik Pandya","Jasprit Bumrah"]
for i in crickter_list:
    print(i)

i=0
while i < len(crickter_list):
    print(crickter_list[i])
    i+=1
    
[print(x) for x in crickter_list]   

print("------------------------------------------------------------------------------------------------")
india_crickter_list = []
for i in crickter_list:
    india_crickter_list.append(i)
        
print(india_crickter_list)        

#  r letter in name that store in this list 

k_letter_cricketers = [i for i in crickter_list if 'k' in i.lower()]
print(k_letter_cricketers)


# ------------------------------  Sort The List In Python------------------------------------------------------------------

india_crickter_list.sort()
print(india_crickter_list)

india_crickter_list.reverse()
print(india_crickter_list)

print("------------------------------------------------------------------------------------------------")
india_crickter_list.sort(reverse= False)
print(india_crickter_list)


# ============================Copying The List =================================

newList = india_crickter_list.copy()
print(newList)
prevList =list(india_crickter_list)
print(prevList)

list1 = [1,2,3,4,5,6,7,8,9,10,11]
list2 = ["pink", "orange", "red", "Blue"]
list1 = list1+list2
print(list1)




























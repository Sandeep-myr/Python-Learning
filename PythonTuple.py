tuple_data = ("pink","orange","Blue","green")
print(tuple_data[-1])
print(tuple_data[2:5])

print("----------------------------------------------------------------------------------------------")
x = tuple(tuple_data)

print(type(x))
y = list(x)
print(type(y))

fruits = ("apple","orange","Mango")
(apple, orange, Mango) = fruits

print(apple)
print(orange)
print(Mango)

#  ek tuples ko dusre tuple se join karne k liye + opertor ka use kar sakte hai 

newFruitTuple = ("grapes","kiwi","papaya") 
fruits = fruits+newFruitTuple
print(fruits)



import json

x = '{"name" : "John", "age" :23 , "salary" :1234}'


y = json.loads(x)

print(y["age"])

y = json.dumps(x)
print(y)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x))
print(json.dumps(x, indent=4))

print(json.dumps(x, indent=4,separators=(".","=")))
print("------------------------------------------------------------------------------------------------")
print(json.dumps(x, indent=4,sort_keys=True))
print("------------------------------------------------------------------------------------------------")
#  false karna bekaar hai 
print(json.dumps(x, indent=4,sort_keys=False))




a = 5
b = 10.0
c = "square"
d = False
e = 1 + 2j
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
coordinates = (1, 2)
r = range(a)
person = {"name": "John", "email": "sanderson@gmail.com"}

setData = {"p", "q", "r"}
frozendata = frozenset(["a", "b", "c", "d", "e"])

data = b"hello"   
 
mutable_data = bytearray(b"hello")  # bytearray
view = memoryview(b"hello")   # memoryview
nothing = None 
# Type checking
print(type(a))         # <class 'int'>
print(type(b))         # <class 'float'>
print(type(c))         # <class 'str'>
print(type(d))         # <class 'bool'>
print(type(e))         # <class 'complex'>
print(type(numbers))   # <class 'list'>
print(type(coordinates)) # <class 'tuple'>
print(type(r))         # <class 'range'>
print(type(person))    # <class 'dict'>
print(type(setData))   # <class 'set'>
print(type(frozendata))   # <class 'set'>
print(type(data))   # <class 'set'>
print(type(mutable_data))   # <class 'set'>
print(type(view))   # <class 'set'>
print(type(nothing))   # <class 'set'>

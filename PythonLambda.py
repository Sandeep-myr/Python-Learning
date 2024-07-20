#  A Python Lambda function is a small annonymous function
x = lambda a: a*10
print(x(5))  

print("------------------------------------------------------------------------------")
#  A Lambda Function Take any Number of argunmnets
y = lambda a, b: a*b
print(y(5, 10))

print("------------------------------------------------------------------------------")
z = lambda a,b,c : a*b*c
print(z(2,3,4))

print("------------------------------------------------------------------------------")

def test(n):
    return lambda a:a+n

trouble = test(5)
print(trouble(2))

print("------------------------------------------------------------------------------")

def test1(a,b):
     return a+b  







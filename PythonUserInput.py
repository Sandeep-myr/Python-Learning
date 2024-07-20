import random
# x = input("Ente the name: ")
# print("Your name is : ", x)

x = True
y = random.randrange(1, 12345)

  


# Generate a random number between 1 and 100
y = random.randint(1, 100)
x = True

while x:
    z = int(input("Enter The Number: "))
    if z < y:
        print("Too Low!")
    elif z > y:
        print("Too High!")
    else:
        print("Congratulations! You guessed the number.")
        x = False

        
        
        
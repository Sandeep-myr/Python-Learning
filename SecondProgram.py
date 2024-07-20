import random  # Import the random module

x = 4
y = "John"

# Corrected string and integer operation
print(y + str(x))  # Convert x to string before concatenation

def test():
    global z
    z = "sandeep"
    print(x)

test()
print(z)  # Ensure z is defined before printing

print(random.randrange(1, 12345678))  # Use random.randrange() correctly

def loop():
    name = "sandeep"
    print(len(name))
    for i in name:
        print(i)

loop()  # Correct indentation for loop() function

txt = "My School Name is Sarla Higher Secondary School Sarlanagar"
print("Sarla" in txt)  # Correct indentation for checking substring in txt

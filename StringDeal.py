name = "MS Dhoni"
#converting into upper case
print(name.upper()) 
# converting into lower case
print(name.lower())

#remove the white spaces
print(name.replace(' ', ''))

# remove the white spaces from begining of the text and ending of the text
print(name.strip())

#  split the string
print(name.split(' '))

#  using the formatted string into our string string me prefix f lagana padega

age = 33
print(f"My name is {name} and my age is {age}")

txt = f"ager mai 15 x 8  karuga to { 15*8 } milega"
print(txt)


#  escape characters for using " " word
print("My Village name is \"Bhadanpur pahad\" located\r\r in maihar district") 



# String methods examples (continued)

# center(): Returns a centered string
string = "Hello"
centered_string = string.center(10, "*")
print(f"center(): '{centered_string}'")  # Output: '**Hello***'

# encode(): Returns an encoded version of the string
string = "Hello"
encoded_string = string.encode(encoding='utf-8')
print(f"encode(): {encoded_string}")  # Output: b'Hello'

# expandtabs(): Sets the tab size of the string
string = "Hello\tworld"
expanded_string = string.expandtabs(4)
print(f"expandtabs(): '{expanded_string}'")  # Output: 'Hello   world'

# find(): Searches the string for a specified value and returns the position of where it was found
string = "Hello world"
position = string.find("world")
print(f"find(): {position}")  # Output: 6

# format(): Formats specified values in a string
name = "John"
age = 30
formatted_string = "My name is {} and I am {} years old".format(name, age)
print(f"format(): '{formatted_string}'")  # Output: 'My name is John and I am 30 years old'

# isalnum(): Returns True if all characters in the string are alphanumeric
string = "Hello123"
is_alnum = string.isalnum()
print(f"isalnum(): {is_alnum}")  # Output: True

# isalpha(): Returns True if all characters in the string are in the alphabet
string = "Hello"
is_alpha = string.isalpha()
print(f"isalpha(): {is_alpha}")  # Output: True

# isascii(): Returns True if all characters in the string are ascii characters
string = "Hello"
is_ascii = string.isascii()
print(f"isascii(): {is_ascii}")  # Output: True

# isdecimal(): Returns True if all characters in the string are decimals
string = "12345"
is_decimal = string.isdecimal()
print(f"isdecimal(): {is_decimal}")  # Output: True

# isdigit(): Returns True if all characters in the string are digits
string = "12345"
is_digit = string.isdigit()
print(f"isdigit(): {is_digit}")  # Output: True

# Additional methods can be added similarly



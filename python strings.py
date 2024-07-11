print("maneesh")
print("is good boy")

# ouotes inside quotes 
print("he is called 'maneesh'")
print('he is also called "adithya"')

# assign string to a variable
a="maneesh"
print(a)

# Multiline string
# You can assign a multiline string to a variable by using three quotes
# You can use three double quotes or three single quotes

x= """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(x)

'''
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
'''
a = "Hello, World!"
print(a[1])

# Looping Through a String

for x in "maneesh":
    print(x)

# string length 

x="maneesh"
print(len(x))

# check string 

txt= "maneesh is a very good boy"
print("good" in txt)

# checking using if statement 

txt= "maneesh is a very good boy"
if "good" in txt:
    print('yes there is good in "txt"')



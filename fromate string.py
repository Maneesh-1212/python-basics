# we cannot combine strings and numbers 
'''
F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
To specify a string as an f-string, simply put an f in front of the string literal, and 
add curly brackets {} as placeholders for variables and other operations.

'''

# Example 1

age= 21
txt= f"my name is maneesh , i am {age}"
print(txt)

# Placeholders and Modifiers
# A placeholder can contain variables, operations, functions, and modifiers to format the value.

price= 7
txt= f"The price of an egg is {price}"
print(txt)

'''
A placeholder can include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

'''
# example 2

price= 7
txt= f"The price of an egg is {price:.2f}"
print(txt)

# A placeholder can contain Python code, like math operations

# Example 1

txt= f'The price is {3 * 9} dollars'
print(txt)
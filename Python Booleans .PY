# BOOLEN VALUES 
# Booleans represent one of two values TRUE or FLASE

# example 1
print(10 > 9)
print(10 == 9)
print(10 < 9)

# When you run a condition in an if statement, Python returns True or False
# example 2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate Values and Variables
#The bool() function allows you to evaluate any value, and give you True or False in return,

#Example
#Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))
#Example
#Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

# Example
# The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

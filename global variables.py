# global variables

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


# creating a variable inside a function with the sam name as gloable variable 

x="easy"

def myfunc():
  x="simple to learn"
  print('python is '+ x)

myfunc() 

print('python is '+ x)

# The Global keyword 

def name():
  global y
  y= "maneesh"
name()
print("My name is " + y)

# Also, use the global keyword if you want to change a global variable inside a function.

# Example
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

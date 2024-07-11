# Many values to multiple variables 

x,y,z="maneesh", "adithya","satya"
print(x)
print(y)
print(z)

# one values to multiple variables

x=y=z= 'maneesh'
print(x)
print(y)
print(z)

# unpack a collectiom
NUM=['ONE','TWO','THREE']
x,Y,Z=NUM
print(x)
print(y)
print(z)

# output variables 

#example 1

x="python "
y="is "
z= "awesome"
print(x,y,z)

#example 2

x="python "
y="is "
z= "awesome"
print(x+y+z)


#In the print() function, when you try to combine a string and a number with the + operator, 
#Python will give you an error:
#The best way to output multiple variables in the print() function is to separate them with commas, 
#which even support different data types

x = 5
y = "John"
print(x, y)

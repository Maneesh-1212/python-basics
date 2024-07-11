# python data types 
#Python has the following data types built-in by default, in these categories:

'''
Text Type       :	str
Numeric Types   :	int, float, complex
Sequence Types  :	list, tuple, range
Mapping Type    :	dict
Set Types       :	set, frozenset
Boolean Type    :	bool
Binary Types    :	bytes, bytearray, memoryview
None Type       :	NoneType

'''
x= "hello world"
print(type(x))

A= 20
print(type(A))

b=4.4
print(type(b))

c=1j
print(type(c))

d=["apple","mango","bananna"]
print(type(d))

e=("apple","mango","bananna")
print(type(e))

f={"pen","book","prncile"}
print(type(f))

g={"name":"maneesh","age": 21}
print(type(g))

x = frozenset({"apple", "banana", "cherry"})
print(type(x))

x = True
print(type(x))

x=b"hello"
print(type(x))

x = bytearray(5)
print(type(x))

x=memoryview(bytes(5))
print(type(x))

x=None
print(type(x))

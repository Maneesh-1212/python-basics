
# The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# other escape characters 

#1. \'	    Single Quote	
#2. \\	    Backslash	
#3. \n	    New Line	
#4. \r	    Carriage Return	
#5. \t	    Tab	
#6. \b	    Backspace	
#7. \f	    Form Feed	
#8. \ooo	Octal value	
#9. \xhh	Hex value


# example 1
txt = 'It\'s alright.'
print(txt)

#Example2 
txt = "This will insert one \\ (backslash)."
print(txt) 

# example 3 
txt = "Maneesh\nadithya"
print(txt)

# example 4
txt = "Hello\rWorld!"
print(txt) 

# example 5
txt = "Maneesh\tAdithya"
print(txt)

# example 6
txt= "maneesh\badithya"
print(txt)

# example 7
txt = "HELLO\fWORLD"
print(txt)

# example 8
txt = "\110\145\154\154\157"
print(txt)

# example 9 
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

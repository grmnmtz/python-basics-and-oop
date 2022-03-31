# String methods.

hello = "hello"
print(type(hello))

# <class 'str'>

# .upper()

upper_string = "hello"
print(upper_string.upper()) # "HELLO"

# .lower()

lower_string = "WORLD"
print(lower_string.lower()) # "world"

# .capitalize()

capitalized_string = "dante"
print(capitalized_string.capitalize()) # "Dante"

# .count()

# Looks for substring occurences inside a string

greeting = "heLLO World"
print(greeting.count("ll")) # 0 since ll are capitalized
print(greeting.lower().count("ll")) # 1 
print(greeting.lower().count("o")) # 2 

# Repeating a string by multiplying it.

x = "hello"
y = 3
z = "yes"
print(x * 3) # hellohellohello

# concatenating strings
print(x + " " + z) 
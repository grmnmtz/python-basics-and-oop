# Conditional operators

# Evaluates two variables or data types and returns either
# either true or false based on the comparison.

# Is the left hand equals to the right hand
# ==

# Is left hand not equals to the right hand
# !=

# <=
# >=
# >
# <

x = "hello"
y = "hello"
print(x == y) # True
print(x != y) # False

# comparing by ASCII Code in Python by ordinal value of a char.

print ("a" > "Z") # True

print(ord("a")) # 97
print(ord("Z")) # 90

# We are comparing the ordinal values of a string.

# Storing the comparison in a variable

result = 6.0 == 6
print(result) # True

a = 7
b = 8
z = 0

result1 = a == b # False
result2 = a > b # False
result3 = z - 2 < b + 2 # True

print(result3)

# Chained conditionals

# and 
# or
# not

result4 = result1 or not result2 or result3

# if the left hand is true or if the right hand is true
# then the whole condition is true. 

print("not true", not True) # False
print("not false", not False) # True
print("both true", not (False and True)) # True

# order of operations in chained conditionals

# not is first
# and is second
# or is last





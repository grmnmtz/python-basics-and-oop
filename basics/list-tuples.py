# Lists and tuples
# It can store different values and it is unordered.

x = [4, True, "Hi"]
y = "hi"

# To check the length of any element use len(value) function.

print(len(x), len(y))

# list.append(value) (add an element to the end of the list)

x.append("Hello")

print(x) # now includes hello

x.extend([1,2,3,4,5])
print(x) 

# Extends a list by adding all the elements from another list.

# pop()

# removes an element from a list
# last if no arguments are given, and it can remove 
# another element
# by using it's index.

x.pop()
print(x) # Without 5 now.
x.pop(0) # removes 4
print(x)

# indexes starts at 0 on lists.
# If we want to look into the last element of a list we look into the lenght of the list and we substract 1. 

# To change a value from a list 

x[0] = "hello"

print(x)

# Lists are mutable, doesn't store a copy, stores a reference in
# memory.

print(x[len(x) - 1]) # access the last element of a list.
print(x[0]) # hello

y = x # not copied
y = x[:] # copied

print(x,y)

# Tuples

# tuples are similar to lists but they're immutable. They use
# round brackets instead of square brackets. They work the same
# except we can't append or remove or we can't change elems.

x = (0,0,2,2)

# TypeError: 'tuple' object does not support item assignment.
# x[0] = 5

print(x[0])
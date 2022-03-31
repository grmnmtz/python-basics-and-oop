x = "Dante"

def func(name):
    x = name # local variable
    print(x) # now you can access it

print(x)
func('changed') # Doesn't do anything, because it's out of scope.
print(x)

# Using the global keyword inside another scope in this case
# a function.

def global_changer_function(name):
    global x # access the global variable
    x = name

global_changer_function("I changed from inside of a function")

# it now prints "I changed from inside of a function", because
# we change the global variable from our function accesing it 
# with the global keyword.

print(x)

# Note: Never use the global keyword isn't a good practice. 
# Always stick to local variables when possible.
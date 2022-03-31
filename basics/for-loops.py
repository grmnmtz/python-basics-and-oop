# for variable or element in range, in this a collection based
# on the input we give it.

for i in range(1, 10, 1):
    print("going positively: ", i)
    
# going positively from 1 to 10

for i in range(10, -1, -1):
    print("going negatively: ", i)

# going negatively from 10 to 0

# range(start, stop, step) function args

# if only 1 arg, by default is going to use the stop arg.
# if 2 args are given, they're going to be start stop.
# if we add 3 is going to use the step arg which will tell us
# by how much we should increment after each iteration.

for i in ["hello", "world", "I'm", "Iterating", "wohoo"]:
    print(i)

x = [1,2,3,4,5]

# Iterate until the length of my x array

for i in range(len(x)):
    print(x[i])

# iterating with the enumerate function

for i, element in enumerate(x):
    print(i, element) 

#Prints index and element from index.


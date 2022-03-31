def func(x):
    def func2():
        print(x)

    return func2

func(3)() # 3

x = func(5)
x() # 5

# The unpack operator separates all the elements from a list, 
# tuple or other collection. And sends them as args to another 
# function.

def args_function(*args, **kwargs):
    pass

x = [1,23,45,69]

# prints all elements extracted from x, separated by spaces.

print(*x) # 1 23 45 69 

# Without the unpack operator it prints the list.

print(x) # [1, 23, 45, 69]

def another_unpack(x, y):
    print(x,y)

pairs = [(1,2), (3,4)] # tuples inside list with pairs.

for pair in pairs:
    another_unpack(*pair)

# returns
# 1 2
# 3 4

# for dictionaries we need ** asterisk

another_unpack(**{'x': 2, 'y': 5})

# args keys needs to be the same as defined in the unpack.

def function(*args, **kwargs):
    print(args, kwargs)
    # print(*args) still works

function(1,2,3,4,5, one = 0, two = 1)

# returns tuple with positional args, and the keyword args which
# are one and two as a dictionary.

# (1, 2, 3, 4, 5) {'one': 0, 'two': 1}

# if using kwargs without valid params it's going to throw an error

# def func(*arg, **kwargs):
    # print(**kwargs) Error
    # print(one = 0, two = 1) Valid
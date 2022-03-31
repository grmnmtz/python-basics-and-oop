# maps takes an iterable, list a list and returns all elements
# converted using the lambda function inside the map functions

nice_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

mapped_list = map(lambda element: element * 2, nice_list)

print(list(mapped_list))

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

# Filter returns an iterable with the elements that return 
# true from the lamba condition.

numbers_greater_than_10 = filter(lambda element: element > 10, nice_list)

even_numbers_only = filter(lambda element: element % 2 == 0, nice_list)

print(list(numbers_greater_than_10))

# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(list(even_numbers_only))

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def func(i):
    i = i * 3
    return i % 2 == 0

# You can use another function instead of a lambda as a callback.


# we can define a for loop inside the list

x = [x for x in range(5)]

print(x) # [0, 1, 2, 3, 4]

x = [x + 5 for x in range(5)]

print(x) # [5, 6, 7, 8, 9]

# More complex examples of comprehension

x = [i for i in range(20) if i % 5 == 0]

print(x) # [0, 5, 10, 15]

# A dictionary is a key value pair store

x = {'key': 'value'}

print(x['key'])

# adding a key value pair to a dictionary

x['key2'] = 5

print(x) # {'key': 'value', 'key2': 5}

# You can add another value other than string as key.

x[2] = 'number'

print(x) # {'key': 'value', 'key2': 5, 2: 'number'}

# Just as a set, this uses a hash so it is very fast to do
# operations on dictionaries. 
# O(1) constant time on average 
# O(n) linear time at worst case 

# check if a key exist in a dictionary.

print('key' in x) # True

# values() to get all the values from a dictionary

print(x.values()) # dict_values(['value', 5, 'number'])

# creating an array from dictionary values

print(list(x.values())) # ['value', 5, 'number']

# Getting all keys from a dictionary

print(list(x.keys())) # ['key', 'key2', 2]

# deleting a key from a dictionary

# del x['key']

print(x) # {'key2': 5, 2: 'number'}

# iterating over a dictionary

for key, value in x.items():
    print(key, value)

# another way to iterate over dictionaries.

for key in x:
    print(key, x[key])
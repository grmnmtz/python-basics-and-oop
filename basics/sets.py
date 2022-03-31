# A set is a unique unordered collection of elements.

x = set()

s = {4,32,2,2}

s.add(5)
s.remove(2)

print(s) # {32,4,5}

# check if an element exists in a set

print(4 in s) # True or False in this case True

# Sets operations run in constant time O(1) much faster than lists. So Sets are useful with large collection of non duplicate data.

s2 = {3,4,22,1}

print(s.union(s2)) # essentialy adding 2 sets together

print(s.intersection(s2)) # values that exists in both sets.
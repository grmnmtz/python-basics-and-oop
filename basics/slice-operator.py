x = [0,1,2,3,4,5,6,7,8,9]

y = ["hi", "hello", "goodbye", "cya", "sure"]

s = "hello"

# syntax

# sliced = x[start:stop:step]

# go to the index at start, stop as we hit the stop index, do
# not include the stop index. And for each iteration increment
# by the step definition.

sliced = x[0:4:2] #[0,2]

# Iterate and stop at index 4

sliced = x[:4] # [0,1,2,3]

# Start at 2 and leave at the end

sliced = x[4:] # [4,5,6,7,8,9]

# Start at 2 and end at index 4, step by 1 ( default )

sliced = x[2:4] # [2,3]

# start from index 4, end at index 2 do not include it, and 
# iterate by negative 1 (reverse)

sliced = x[4:2:-1] # [4,3]

# reversing a list with the slice operator

reversed = x[::-1]

# slice works on strings, tuples and any collection of elements.

print(sliced)

print(reversed)
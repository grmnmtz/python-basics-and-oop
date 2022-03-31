# Strings can be expressed with '' or "" and \ can be used
# to escape quotes:

text1 = 'spam eggs'
text2 = "doesn't"
greeting = '"Yes", they said.'
greeting2 = "\"Yes,\" they said."
greeting3 = '"Isn\'t," they said.'

# print() function is used to produce readable output.

print("nice day")

# You can use raw strings by adding an r before the first quote.

print(r'C:\some\name')

# String literals can span multiple lines by using """...""" or
# '''...'''. End of lines are automatically included. It's 
# possible to prevent this by adding a \ at the end of the line

print("""\
Usage: thingy [OPTIONS]
    -h
    -H hostname
""")

# Strings can be concatenated with the + operator and repeated
# with * operator

3 * 'un' + 'ium'

# 2 or more string literals next to each other are automatically
# concatenated, particularly useful when you want to break long strings.

'Py' 'thon'

text = ('Put several strings within parentheses '
        'to have them joined together.')

print(text)

# This only works with 2 literals. Not variables or expressions.
# To concatenate variables or a variable and a literal use +

prefix = "Hello, "

print(prefix + "world")

# Strings can be indexed with the first character having index 0
# There is no separate character type. A character is simply a 
# string of size one.

word = 'Python'

print(word[0]) # 'P'

# Indices may also be negative numbers to start counting from
# the right 

word[-1] # 'n'

word[-2] # second-last character

word[-6] # 'p'

# Note that since -0 is the same as 0, negative indices start from -1.

# In addition to indexing, slicing is also supported. While 
# indexing is used to obtain individual characters, slicing 
# allows you to obtain substring:

word[0:2] 

# Characters from position 0 (included) to 2 (excluded)
# 'Py'

word[2:5] 

#Characters from position 2 (included) to 5 (excluded)
# 'tho'



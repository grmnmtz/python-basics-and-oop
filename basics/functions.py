# Basic function syntax def means define 
# Functions are objects, so you can return them.

def func():
    print("Run")
func()

# You can define functions inside functions

def func2():
    print("I have another function")
    def func():
        print("I'm 'inside another function.")
    func()

func2()

# defining arguments for functions:

def multiply(a, b):
    print(a * b)
    return a * b

multiply(5,10)

# Destructuring results

def destructured(a,b):
    print("Destructure", a, b)
    return a * b, a / b

# Extract the values from the tuple and asign to variables.

result1, result2 = destructured(3,6)

print(result1, result2) # 18 0.5

# Default assignments

def default_function(z = True):
    print(z) # True

default_function()

# Multiplying without using * operator exercise

def multiply_with_sum(num1: int, num2: int) -> int:
    result = 0
    if num1 == 0 or num2 == 0:
        return 0
    else:
        for i in range(0, num2):
            result += num1
    return result

multiply_with_sum(5,5)
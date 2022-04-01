# Object Oriented Programming in Python.

# Whatever you create in Python is an instance of
# an specific class. For example Int, Str or Function and that class defines the way that our
# object can interact with other parts of our 
# program

# x = 1
# y = "hello"

# print(x + y) # Unsupported operation.

# string = "hello"

# upper is a method of the str class

# print(string.upper()) # HELLO

# Dog class
class Dog:

    # Instantiate the object right when it is created
    
    # Init method.

    # self denotes the object itself, similar to this.
    # self passes a reference to which object is 
    # what called on

    def __init__(self, name, age):

        # an attribute of the class Dog.
        self.name = name
        self.age = age

        # it immediatealy prints it on instantiation.
        print(name)

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def set_age(self, age): 
        self.age = age


# print(type(dog1)) # class __main__.Dog

# A new Instance of the Dog class called milthon.

dog1 = Dog(name = "Milthon", age = 5)

dog2 = Dog(name = "Bill", age = 10)

print(dog2.get_name()) # Bill
print(dog1.get_age()) # 5
dog1.set_age(33)
print(dog1.get_age()) # 33


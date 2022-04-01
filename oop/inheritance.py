# Basic Example of inheritance.

# General Class

class Pet:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')

    # Original method to inherit.

    def speak(self):
        print("I'm a nice method.")

# Specific Class

# Add the Class from which this class will inherit with parentheses.

# Child or derive classes

class Cat(Pet):
    def __init__(self, name, age, color):
        # Calling the super class to obtain attributes.
        super().__init__(name, age)
        self.color = color

    # Method overriding

    def speak(self):
        print("Meow")

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')

class Dog(Pet):

    # Method overriding

    def speak(self):
        print("Bark")

class Fish(Pet):
    # No methods overriding in Fish class
    pass


p = Pet("Tim", 19)
p.speak() # I'm a nice method.
c = Cat("Bill", 24, "White")
c.speak() # Meow
d = Dog("Jill", 25)
d.speak() # Bark

# If is there a method with the same name as the
# Upper Class, it will override the inherited method.

f = Fish("Joe", 16)
# No method overriding in the Fish class
f.speak() # I'm a nice method.

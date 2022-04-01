# Class Attributes and class method.

# Self was referring to the instances we were 
# talking about in that context.

# Class attributes are attributes that specific to the class, not to an instance of an object of that class.

class Person:
    # Class attribute
    # this is not specific to any instance.
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()


    #Decorator
    @classmethod
    
    # This method acts on the class itself, they don't have access to any instance.
    # No self since it's only acting on this class.

    def number_of_people_(cls):
        return cls.number_of_people

    #Decorator

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1



p1 = Person("Tim")
print(Person.number_of_people) # 1 
p2 = Person("Jill")
print(Person.number_of_people) # 2

print(p2.number_of_people) # 2

# Calling our class method.

print("Number", Person.number_of_people_()) # 2 


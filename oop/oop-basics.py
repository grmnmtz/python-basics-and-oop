'''

----------------- Object Oriented Basics ---------------------

What is an object? 

An object is a collection of DATA and associated BEHAVIORS.

What does object oriented means?

Object oriented means functionally directed toward modeling objects.

This is one of many techniques used for modeling complex systems. 
It is defined by describing a collection of interacting objects via their data and behavior.


------- Object Oriented Analysis (Exploration) --------------

Object Oriented Analysis (OOA) is the process of looking at a problem, system or task 
(that somebody wants to turn into an application) and identifying the objects and interactions between those objects.
The analysis stage is all about what needs to be done.

Output:

The output of the analysis stage is a set of requirements. If we were to complete the analysis stage in one step, 
we would have turned a task, such as I need a website, into a set of requirements. As an example here or some 
requirements as to what a website visitor might need to do.

Actions ----------------- Objects

Review our                history
Apply for                 jobs
Browse, compare, order    products

A better turn phrase might be object-oriented exploration.

In software development, the initial stages of analysis include
interviewing customers, studying their processes, and eliminating possibilities.


------------------ Object Oriented Design ---------------------

OOD is the process of converting such requirements into an implementation specification. 
The designer must name the objects, define the behaviors, and formally specify which objects can activate 
specific behaviors on other objects. The design stage is all about how things should be done.

Output:

The output of the design stage is an implementation specification. If we were to complete the design stage 
in a single step, we would have turned the requirements defined during object-oriented analysis into a set of 
classes and interfaces that could be implemented in (ideally) any object-oriented programming language.


----------------- Object Oriented Programming -----------------

Object-Oriented programming (OOP) is the process of converting
this perfectly-defined design into a working program that does exactly what the CEO originally requested.

In real world, this doesn't happen. We'll always find things that need further analysis while we're designing. 
When we're programming, we find features that need clarification in the design.

In iterative development, a small part of the task is modeled, designed and programmed, and then the program is 
reviewed and expaned to improve each feature and include new features in a series of short development cycles.
 
'''

'''

----------------- Objects and classes -------------------------


Let's pretend we are doing and inventory application for a fruit
farm. To facilitate the example, we can assume that apples go in
barrels and oranges go in baskets.

Now, we have four kinds of objects: apples, orange, baskets, and
barrels. 

In object-oriented modeling, the term used for a kind of object is class

So, in technical terms, we now have four classes of objects.

Class: A kind of object / A template for creating objects.

Classes describe objects. They're like blueprints for creating
objects. 

Objects are instances of classes that can be associated with each other.

An object instance is a specific object with its
own set of data and behaviors

Each orange is a distinct object, but all three have the attributes
and behaviors associated with one class: the general class of oranges.

The relationships between the four classes of objects in our
inventory system cna be described using UML (Unified modeling language)
class diagram.

Orange * --- go in --- 1 Basket

Apple  * --- go in --- 1 Barrel

This diagram showst that a basket is associated with an orange.
And apples are associated with a barrel.

Association is the most basic way for two classes to be related.

One basket can hold many (represented by *) Orange Objects.
Anh orange can go in exactly 1 basket.
This number is referred to as the multiplicity of the object.
You might also hear it described as cardinality. These are slightly
different terms.

Cardinality refers to the actual number of items in the set,
whereas multiplicity specifies how small or how large the set
could be.

Reading from left to right, many instances of the Apple class
can go in any one Barrel. 

Reading from right to left, exactly one Barrel can be associated
with any one Apple.

'''

''' 

-------------------- Data and behaviors -----------------------

Data describes objects

Data represents the individual characteristics of a certain object.

A class can define specific sets of characters that are shared by all objects from that class.

Any specific object can have different data values for the 
given characteristics. Attributes don't have to be unique.

Attributes are frequently referred to as members or properties.

Orange
    -Weigth
    -Orchard
    -Date_picked

Apple
    -Color
    -Weight

Basket
    -Location

Barrel
    -Size

Adding attributes and methods to individual objects allows us to create a system of interacting objects. 

Each object in the system is a member of a certain class. 

These classes specify what types of data the object can hold and what methods can be invoked on it. 

The data in each object can be in a different state from other instances of the same class; each object may react to method calls differently because of the differences in state.

Object-oriented analysis and design is all about figuring out what those objects are and how they should interact. 

'''


'''

-------------- Interfaces and hiding details -----------------



'''
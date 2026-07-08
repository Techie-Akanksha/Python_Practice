# OOPS CONCEPT

# Inheritance
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or subclass) to inherit properties and behaviors (methods) from another class (called a parent or superclass). This promotes code reusability and establishes a hierarchical relationship between classes.  

# Benefits of using inheritance is :
# 1. Code reusability
# 2. Organized structure
# 3. Easy to maintain and extend 

class Parent:
    def speak(self):
        print("I am the parent class.")

class child(Parent):
    pass

child_instance = child()
child_instance.speak()  # Output: I am the parent class.

# Constructor in Inheritance

# when you create a parent class with a constructor function inside it and then this class is inherited by another class then constuctor function of parent class will work for the child class as well.

class parent:
    def __init__(self, name):
        self.name = name

class child(parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# If you need a new parameter in your child class you have to create a constructor function for your child class but the parameters that can be initialized in the parent class will be initialized using the super() function. Super function will target the parent class.

child_instance = child("John",19)
child_instance.display()  # Output: My name is John.

#Types of Instance 

# 1. Single Level Inheritance

# Single Inheritance means one child class inherits the properties and methods of one parent class. This allows the child class to reuse the parent's code and also add its own features.

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


# Child Class
class Dog(Animal):

    def bark(self):
        print(f"{self.name} is barking.")


# Creating Object
dog1 = Dog("Tommy")

# Method inherited from Animal
dog1.eat()

# Method of Dog class
dog1.bark()

# 2. MultiLevel Inheritance

# Multilevel Inheritance means a class inherits from another class, and that class itself inherits from another class. This forms a chain of inheritance, allowing the last child class to access features from all its ancestor classes.

class LivingThing:

    def breathe(self):
        print("Living things breathe.")


class Animal(LivingThing):

    def eat(self):
        print("Animals eat food.")


class Dog(Animal):

    def bark(self):
        print("Dog barks.")


# Creating object of Dog
dog = Dog()

# Dog can access methods from all levels
dog.breathe()   # From LivingThing
dog.eat()       # From Animal
dog.bark()      # From Dog

# 3. Multiple Inheritance

# Multiple inheritance is a feature in OOP where a child class inherits from more than one parent class, allowing it to access attributes and methods of all parent classes.

# MRO (Method Resolution Order) : Left to Right priority
# Agar dono parent class me same method name ho:

class Father:
    def driving(self):
        print("Father: Knows driving")


class Mother:
    def cooking(self):
        print("Mother: Knows cooking")


class Child(Father, Mother):
    def gaming(self):
        print("Child: Knows gaming")


# Object
c = Child()

c.driving()   # from Father
c.cooking()   # from Mother
c.gaming()    # from Child


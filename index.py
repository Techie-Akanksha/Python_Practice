# OOPS CONCEPT

# OOPS (Object-Oriented Programming System) is a programming paradigm that organizes software around objects rather than functions. An object contains both data (attributes) and methods (functions) that operate on that data. OOPS helps make programs more modular, reusable, maintainable, and easier to scale.

# OOPS (Object-Oriented Programming System) is a programming approach that uses objects containing data and methods. Its four core principles are Encapsulation, Abstraction, Inheritance, and Polymorphism. OOPS helps build software that is reusable, modular, secure, and easier to maintain.


# 1)Class : Blueprint of object

    # Creating a class is simple, we use the keyword class followed by the name of the class. The name of the class should be in PascalCase.
    # Inside the class, we define attributes and methods that represent the behavior and characteristics of the objects created from the class.

    # Variables inside the class are called attributes, and functions inside the class are called methods. Attributes represent the state or properties of an object, while methods define the actions or behaviors that an object can perform.

    # Variables -> inside the class are called attributes
    # funtion -> inside class it becames method

class Car:
    color = "Red"  # Attribute

    def hello(): # Method
        print("Hello")  

#You can access the attributes and methods after accessing the class using the dot operator.

print(Car.color)  # Accessing attribute
Car.hello()  # Accessing method (This is not a good practice, as methods should be called on instances of the class, not the class itself.)

#Learn something different
# Instance method (most common):

class Car:
    def hello(self): #instance methods must take self as the firstparameter.
        print("Hello")

car = Car() #object of class
car.hello()

# Static method (called using the class):

class Car:
    @staticmethod
    def hello():
        print("Hello")

Car.hello()

# Object 

# Object is an instance of a class. It is created from a class and can have its own unique state and behavior. Objects are the building blocks of OOPS, and they allow us to create multiple instances of a class with different attributes and methods.

# It is very easy to create an object you just have to call the class inside a variable and that variable becomes an object.

class Techie:
    name = "TechieAkanksha"

    def details(self):
        print("This is a Company who creates a lot of content for learning purpose")

obj = Techie() # Creating an object of the class Techie
obj.details() # Calling the method on the object
print(obj.name) # Accessing the attribute on the object

obj.details() # Calling the method on the object


# Constructor

# A constructor is a special method in a class that is automatically called when an object is created. It is used to initialize the object's attributes.

class Techie:
    def __init__(self):
        print("This is a constructor method")

obj = Techie() # Creating an object of the class Techie, which automatically calls the constructor

# self keyword holds the reference of the current object. It is used to access the attributes and methods of the class within the class itself.
class Bag:
    def __init__(self,color,material):
        self.color = color  # Assigning the color parameter to the object's color attribute
        self.material = material  # Assigning the material parameter to the object's material attribute

leather_bag = Bag("Red","Leather") # Creating an object of the class Bag with specific attributes
print(leather_bag.color)  # Accessing the color attribute of the bag object
print(leather_bag.material)  # Accessing the material attribute of the bag object

neon_bag = Bag("Neon","Plastic") # Creating another object of the class Bag with different attributes
print(neon_bag.color)  # Accessing the color attribute of the neon bag object
print(neon_bag.material)  # Accessing the material attribute of the neon bag object

#self is used to refer to the current object of a class. It helps the object access its own variables (attributes) and functions (methods). When you create different objects from the same class, self makes sure each object uses its own data instead of someone else's.

#Types of Attributes in OOPS:

# 1) Instance Attributes: These are attributes that are specific to each instance (object) of a class. A created inside the constructor using instance like self.color, self.name,etc. Each object can have different values for its instance attributes.

#2) Class Attributes:A normal variable created inside the class but outside any method. They are defined directly within the class and are not tied to any specific object. All objects of the class will have access to the same value of a class attribute.

class car:
    wheels = 4  # Class attribute

    def __init__(self,color):
        self.color = color  # Instance attribute

# Types of methods in OOPS:

# 1) Instance Methods: These are the most common type of methods in OOPS. They are defined within a class and operate on the instance (object) of that class. They take self as the first parameter, which refers to the current object. Instance methods can access and modify instance attributes.

class myClass:
    def instance_method(self):
        print("This is an instance method.")

# Uses self as the first parameter.
# Can access and modify instance variables.

class Student:
    
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

    def display_info(self):  # Instance method
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Alice", 90)
s1.display_info()

# 2) Class Methods: These methods are defined using the @classmethod decorator. They take cls as the first parameter, which refers to the class itself rather than an instance. Class methods can access and modify class attributes but cannot access instance attributes directly.

class myClass:
    @classmethod
    def class_method(cls):
        print("This is a class method.")

# Uses cls as the first parameter.
# Decorated with @classmethod.
# Can access class variables.

class Student:
    school = "ABC School"  # Class attribute
    @classmethod
    def display_school(cls):  # Class method
        print(f"School: {cls.school}")

Student.display_school()  # Calling class method using the class name

# cls refers to the class (Student).
# No object is needed.
# Class Method Can Change Class Variables

class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

Student.change_school("XYZ School")
print(Student.school)

# 3) Static Methods: These methods are defined using the @staticmethod decorator. They do not take self or cls as the first parameter. Static methods are utility functions that do not depend on the instance or class state. They can be called using the class name or an instance of the class.

class myClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

# A static method does not use self or cls.

# Decorated with @staticmethod
# Cannot access instance variables directly.
# Cannot access class variables directly (unless using the class name).
# Used for utility/helper functions.

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))

# add() simply adds two numbers.
# It doesn't need any object or class information.

# Example Showing All Three Together

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    # Instance Method
    def display(self):
        print("Name:", self.name)
        print("School:", Student.school)

    # Class Method
    @classmethod
    def show_school(cls):
        print("School:", cls.school)

    # Static Method
    @staticmethod
    def greet():
        print("Welcome Students!")

s1 = Student("Alice")

s1.display()           # Instance Method
Student.show_school()  # Class Method
Student.greet()        # Static Method


# Think of a school:

# Instance Method (self) → Talks about one student.
# Example: Name, marks, age.
# Class Method (cls) → Talks about the whole school.
# Example: School name, total students.
# Static Method → Talks about general tasks.
# Example: Add numbers, check if a year is a leap year, calculate percentage.
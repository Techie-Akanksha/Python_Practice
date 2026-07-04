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


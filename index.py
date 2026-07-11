# OOPS CONCEPT

# Polymorphism
# Polymorphism is the ability of different objects to respond to the same method call in their own specific way.
# Polymorphism is a core concept in Object-Oriented Programming (OOP). The word means "many forms" — and in programming, it allows the same interface or method name to behave differently depending on the object or context.

class Greet:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Heyy {self.name}, Welome to the Coding World!")

class Guest(Greet):
    def __init__(self, name):
        super().__init__(name)

    def greet(self):
        super().greet() #super keyword used for call methods from parent class inside the child class 
        print(f"{self.name} happy to have you here!")

obj = Guest("Rahul")
obj.greet()

# Polymorphism is the ability of the same method to perform different actions in different classes. A child class can redefine (override) a method of the parent class to provide its own behavior.

# Polymorphism is an OOP concept where the same method name behaves differently in different classes by using method overriding.

# types of polymorphism

# 1. Method Overloading
# Method overloading means having the same method name but allowing it to work with different numbers or types of arguments.

# Unlike Java or C++, Python does not allow multiple methods with the same name in the same class. If you define the same method twice, the last definition replaces the previous one.

class Demo:
    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):
        print(a + b + c)

obj = Demo()
obj.add(10, 20, 30)

# The first add() method is ignored because the second one overwrites it.

# still you want to achieve overloading in python. Python uses default arguments or *args..
class Demo:
    def add(self, a, b, c=0):
        print(a + b + c)

obj = Demo()

obj.add(10, 20)      # 30
obj.add(10, 20, 30)  # 60

# Using *args
class Demo:
    def add(self, *numbers):
        print(sum(numbers))

obj = Demo()

obj.add(10, 20)
obj.add(10, 20, 30)
obj.add(10, 20, 30, 40)
# Here, *args accepts any number of arguments.

# Does Python support method overloading?
# Python does not support method overloading like Java or C++. We achieve similar behavior using default arguments or *args.

# 2. Method overriding

# Method overriding is an OOP concept where a child class provides its own implementation of a method that is already defined in the parent class. The child method overrides the parent method.

class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound()

# Method Overriding with super()

class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def sound(self):
        super().sound()      # Calls parent method
        print("Dog barks")

obj = Dog()
obj.sound()

# Here, super().sound() calls the parent class method first, and then the child class adds its own behavior.

# 3. Operator Overloading

# Python lets you redefine how operators like +, -, ==, >, etc., work for your own objects.
# This is done using magic (dunder) methods such as __add__(), __eq__(), __lt__(), etc.

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)

# Normally, + adds numbers. Here, you've changed how + works for Number objects.
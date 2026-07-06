# OOPS CONCEPT

# OBJECT and INsTANCE difference:
# An object is the actual entity created from a class. An instance means that the object belongs to a particular class. In Python, the terms object and instance are generally used interchangeably. For example, if dog = Animal(), then dog is an object and also an instance of the Animal class.

class Animal:
    kingdom = "Animalia"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is speaking")
        
    @classmethod
    def show_kingdom(cls):
        print(cls.kingdom)

    @staticmethod
    def add(a, b):
        return a + b
    
#Instance method
dog = Animal("Dog")
dog.speak()

# Instance method works with instance variables and requires an object to call it. It takes self as the first parameter.

#class method
Animal.show_kingdom()

# Class methods work with class variables. They take cls as the first parameter and are called using the class.

#Static method
Animal.add(5, 10)

# Static methods neither access instance variables nor class variables. They behave like normal utility functions inside the class.

class employee:
    company_name = "ABC Pvt Ltd"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def show_salary(self):
        print(f"{self.name}'s salary is: {self.salary}")
    
    @classmethod
    def show_company_name(cls):
        print(f"Company name is: {cls.company_name}")
    
    @staticmethod
    def calculate_gst(amount):
        gst = amount * 0.18
        print(f"GST on ₹{amount} is ₹{gst}")


rahul = employee("Rahul", 50000)
amit = employee("Amit", 60000)
priya = employee("Priya", 70000)

rahul.show_salary()
amit.show_salary()
priya.show_salary()

employee.show_company_name()
employee.calculate_gst(50000)
employee.calculate_gst(60000)
employee.calculate_gst(70000)
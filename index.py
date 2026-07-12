# OOPS CONCEPT

# Encapsulation 
# Setter() and Getter() methods

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary")

    def get_salary(self):
        return self.__salary

emp = Employee(50000)
emp.set_salary(-5000)
emp.set_salary(6000)
print(emp.get_salary())


class Employee:

    def __init__(self):
        self.__salary = 50000

    def set_salary(self, salary):

        if salary > 0:
            self.__salary = salary

emp = Employee()

emp.set_salary(-2000)

print(emp._Employee__salary)


class Employee:
    def __init__(self):
        self.salary = 500

    def set_salary(self, salary):
        self.salary = salary
        print(f"Salary changed to {salary}")

employee = Employee()
# employee.salary = 50000
# employee.set_salary(50000)
print(employee.salary)

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
emp = Employee(10000)
print(emp.get_salary() + 1000)
print(emp.get_salary())

class Student:

    def __init__(self):
        self.__marks = 80

    def get_marks(self):
        print("Getter Called")
        return self.__marks

s = Student()

print(s.get_marks())

#Q1. Kya Getter sirf variable return karne ke liye hota hai?
# Getter method mein future functional operation bhi perform kar sakte hai.
class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        print("Access Log Saved")
        return self.__salary
    
emp = Employee(10000)
emp.get_salary()

# Future me tum aur bhi kaam kar sakte ho.

# Access Log
# Permission Check
# Cache
# Database Fetch
# Encryption/Decryption
# Analytics

# Isi liye Getter sirf "return value" nahi hota.

# Ye controlled read access hota hai.

class Employee:

    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        print("Getter Called")
        return self.__salary

emp = Employee()

x = emp.get_salary()

print(x)


# Suppose project me 500 jagah likha hai.

# emp.get_salary()

# Ek din requirement aayi:

# Sirf HR hi salary dekh sakta hai.

# Ab kya karoge?

# Agar Getter hai...

def get_salary(self, user):

    if user.role != "HR":
        raise PermissionError

    return self.__salary

# Getter aur Setter sirf value lene-dene ke methods nahi hote. Ye object ke public interface (API) ka hissa hote hain.


# print()	                          
# Screen par output dikhata hai	    
# Function continue karta hai	   
# Kuch store nahi karta	Value      

# return
# Value caller ko wapas bhejta hai
# Function turant end ho jata hai
# variable me store ho sakti hai

print("-"*20)

def demo():
    x = print("Python")
    return x

a = demo()

print(a)
print(type(a))
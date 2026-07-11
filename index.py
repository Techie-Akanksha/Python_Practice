# OOPS CONCEPT

# Encapsulation 

# Encapsulation ka matlab data ko hide karna nahi hai.

# Encapsulation ka matlab hain :- Data aur us data par operate karne wale methods ko ek hi class ke andar rakhna aur direct access ko control karna.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    def get_marks(self):
        return self.__marks

s = Student("Ash", 80)

print(s.get_marks())

s.set_marks(95)

print(s.get_marks())

s.set_marks(-20)

# Double underscore (__)

# Ye Python ka convention hai jisse attribute ko name mangling ke through accidental direct access se bachaya jata hai.
# Double underscore = Private Variable

# Python me true private variables nahi hote.Python trust-based language hai. Double underscore sirf name change karta hai. Isko kehte hain Name Mangling

# Name Mangling 

# Internal Working

# Humne likha

# self.__marks = 80

# Python internally isse convert karta hai

# self._Student__marks

# Dhyan se dekho.

# Ye hide nahi hua.

# Sirf rename hua.

# Memory me actual attribute ban gaya:

# Student Object

# ----------------------

# name = "Ash"

# _Student__marks = 80

# ----------------------

# Isliye

# Ye chalega.

# print(s._Student__marks)



# To phir double underscore ka fayda?

# Ye intentionally direct access ko discourage karta hai aur subclasses me accidental name conflicts se bhi bachata hai.


#Q.1 Def:- Encapsulation is the process of bundling data and the methods that operate on that data into a single class while restricting uncontrolled direct access to the object's internal state. It helps protect data integrity by allowing validation through methods.

# Q2. Why do we use Encapsulation?

# Data Protection
# Validation
# Maintainability
# Controlled Access
# Loose Coupling

# Q3. Does Python support private variables?

# Best interview answer:

# Python does not have true private variables. It uses name mangling with double underscores (__) to reduce accidental access and avoid name conflicts, but the attributes can still be accessed using their mangled names if needed.

# Ye answer beginners aur experienced candidates ke beech difference create karta hai.

class Bank:

    def __init__(self):
        self.__balance = 1000 #self._Bank__balance = 1000 (Name Mangling)

b = Bank()

b.__balance = 5000 #yeh object mein ek naya variable banata hai.

print(b.__balance) 

# Name mangling sirf class definition ke andar __attribute references par apply hoti hai. Class ke bahar obj.__attribute likhne par Python us naam ko mangle nahi karta; wo ek alag attribute create kar sakta hai.

# Q. Is class ko Encapsulation use karke complete karo:

class Employee:

    def __init__(self, name, salary):
        # salary ko encapsulate karo
        self.name = name
        self.__salary = salary

    def set_salary(self, salary):
        # sirf salary > 0 allow ho
        if 0 < salary:
            self.__salary = salary
        else:
            print("Invalid Salary")

    def get_salary(self):
        return self.__salary
    
Employee1 = Employee("Rahul",20000)
print(Employee1.get_salary())

Employee1.set_salary(35000)
print(Employee1.get_salary())


# Q.1

class Employee:

    def __init__(self):
        self.__salary = 50000

emp = Employee()

print(emp.__dict__)

# Q. 2
class Employee:

    def __init__(self):
        self.__salary = 50000

emp = Employee()

emp.__salary = 1000

print(emp._Employee__salary)  #Python simply object ke andar exactly isi naam ka attribute dhundta hai.


# Syntax	            Meaning
# name	     Public attribute (sab access kar sakte hain)
# _name	     Protected by convention (internal use; "please don't touch" signal)
# __name	 Name mangling (accidental access aur subclass name conflicts se bachata hai)


#__ private variable hota hai?

#  Double underscore (__) triggers name mangling, where Python changes the attribute name internally to _ClassName__attribute. This helps prevent accidental access and name conflicts in inheritance, but it is not true privacy.



# Internal Working
# class className:
#     def __init__(self):
#         self.__attribute = "attribute"
#     def show(self):
#         return self.__attribute
# clsname = className()
# clsname.__attribute = "newattribute"

# Object ki memory:

# className

# ↓

# +--------------------------------------+

# _className__attribute = 50000

# __attribute = 1000

# +--------------------------------------+
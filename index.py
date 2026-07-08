# OOPS CONCEPT

#Inheritance Pratice Example 


class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def display_info(self):
        print(f"Person's name is {self.name}\nAge is {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, Student_id, grade):
        super().__init__(name, age)
        self.Student_id = Student_id
        self.grade = grade

    def display_info(self):
        super().display_info()
        print(f"Student ID is {self.Student_id}")
        print(f"Grade is {self.grade}")

class Teacher(Person):
    def __init__(self, name, age,subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
    def display_info(self):
        super().display_info()
        print(f"Subject is {self.subject}")
        print(f"Salary is {self.salary}")


one_student = Student("Alice", 20, "S101", "A")
one_teacher = Teacher("Mr. John", 40, "Mathematics", 65000)
print("----- Student Details -----")
one_student.display_info()

print()

print("----- Teacher Details -----")
one_teacher.display_info()
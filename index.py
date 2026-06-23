# #tuple quesition
# # 1) Create a tuple containing 5 different fruits and print it.
# fruits = ("apple", "Banana", "cherry", "date", "elderberry")
# print(fruits)

# # 2)Create a tuple with the values (10, 20, 30, 40, 50) and:
# # Print the first element.
# # Print the last element.
# # Print the third element.

# numbers = (10, 20, 30, 40, 50)
# print(numbers[0])   # Output: 10
# print(numbers[-1])  # Output: 50
# print(numbers[2])   # Output: 30

# # 3)Print all elements using a loop.
# numbers = (1, 2, 3, 4, 5) 
# for num in numbers:
#     print(num)

# # 4)Find the length of:
# colors = ("red", "green", "blue", "yellow")
# print(len(colors))

# # 5) Check whether "apple" exists in:
# fruits = ("banana", "apple", "mango", "grapes")
# for i in fruits:
#     if i == "apple":
#         print("Found it!")
#         break
# else:
#         print("Not found.")

# # 6)Find the sum of all elements.
# data = (5, 10, 15, 20, 25)
# for i in data:
#     sum = 0
#     sum +=i
# print(sum)

# # 7)Count how many times 3 appears in:
# nums = (1, 3, 5, 3, 7, 3, 9)
# print(nums.count(3))

# # 8)Find the index of "Python" in:
# lang = ("Java", "C++", "Python", "JavaScript")
# print(lang.index("Python"))

# # 9)Convert the following list into a tuple:
# my_list = [10, 20, 30, 40]
# print(tuple(my_list))  # Output: (10, 20, 30, 40)

# # 10)Convert the following tuple into a list:
# my_tuple = (100, 200, 300)
# print(list(my_tuple))  # Output: [100, 200, 300]

# # 11)Concatenate:
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# print(t1 + t2)  # Output: (1, 2, 3, 4, 5, 6)

# #12) Repeat the tuple:
# t = ("A", "B")
# print(t * 3)  # Output: ('A', 'B', 'A', 'B', 'A', 'B')
# count = 0
# # Repeat the tuple using loop
# while count < 3:
#     print(t)
#     count += 1
# # 13)into separate variables and print them.
# student = ("Rahul", 20, "Mumbai")
# name, age, city = student
# print(f"Name: {name}, Age: {age}, City: {city}")

# # 14)Use tuple unpacking to store:
# # First value in a
# # Last value in e
# # Remaining values in middle
# num = (1, 2, 3, 4, 5)
# a, *middle, e = num
# print(f"a: {a}, middle: {middle}, e: {e}")

# # 15)Swap two variables using tuple unpacking:
# x = 10
# y = 20
# x, y = y, x
# print(f"x: {x}, y: {y}")

# SETS
# A set automatically removes duplicates and has no guaranteed order

a = {1, 2, 3, 4, 5}
print(type(a))  # Output: <class 'set'>
# Remove duplicates from a list using a set
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print(unique_set)  # Output: {1, 2, 3, 4, 5}
print(sum(unique_set))
s = "hello"
print(hash(s))  # Output: -903732784889659485
# print(hash(s))  # Output: TypeError: unhashable type: 'set'

a = {1, 2, 3, 4, 5}
# for i in range(len(a)):
#     print(a.pop())  # Output: 1, 2, 3, 4, 5 (order may vary)
#     print(a)  # Output: {2, 3, 4, 5}, {3, 4, 5}, {4, 5}, {5}, set()

a = {10, 20, 30, 40, 50,60,50,50}
for i in a:
    print(i)  # Output: 1, 2, 3, 4, 5 (order may vary)
print(a)  

# Add value in set: add() method adds a single element to the set. If the element already exists, it does nothing.
a.add(160)
print(a)

# Clear complete set: clear() method removes all elements from the set, resulting in an empty set.
a.clear()
print(a)  # Output: set()

#making Copy of set: copy() method returns a shallow copy of the set. It creates a new set with the same elements as the original set.
a = {1, 2, 3, 4, 5}
b = a.copy()
print(b)

# Discard value from set : discard removes the specified element from the set if it exists. If the element does not exist, it does nothing and does not raise an error.
a.discard(3)
print(a)

# pop removes and returns an arbitrary element from the set. If the set is empty, it raises a KeyError. it randomly removes an element from the set, and the order of elements in a set is not guaranteed. Therefore, you cannot predict which element will be removed when using pop().
a.pop()
print(a)

s1 = {10,20,30,40,50}
s2 = {30,40,50,60,70}

# Union of two sets: union() method returns a new set that contains all unique elements from both sets. It combines the elements of both sets without duplicates.
s3 = s1.union(s2)
print(s3)
print(s1|s2)

# update()	
# |=	Update the set with the union of this set and others
s1 |= s2
print(s1)  # Output: {10, 20, 30, 40, 50, 60, 70}

# Difference of two sets: difference() method returns a new set that contains elements that are in the first set but not in the second set.
s4 = s1.difference(s2)
print(s4)
print(s1-s2)

# difference_update()	
# -=	Removes the items in this set that are also included in another, specified set
s1 -= s2
print(s1)  # Output: {10, 20, 30, 40, 50}

# Intersection of two sets: intersection() method returns a new set that contains elements that are common to both sets.
s5 = s1.intersection(s2)
print(s5)
print(s1&s2)

# intersection_update()	
# &=	Removes the items in this set that are not present in other, specified set(s)
s1 &= s2
print(s1)  # Output: {30, 40, 50}

# Symmetric difference of two sets: symmetric_difference() method returns a new set that contains elements that are in either of the sets but not in both. It effectively combines the unique elements from both sets while excluding the common elements.
s6 = s1.symmetric_difference(s2)
print(s6)
print(s1^s2)

# symmetric_difference_update()	
# ^=	
# Inserts the symmetric differences from this set and another
s1 ^= s2
print(s1)

# isdisjoint()
# Returns True if two sets have no elements in common, otherwise False
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))  # Output: True

s3 = {1, 2, 3}
s4 = {3, 4, 5}
print(s3.isdisjoint(s4))  # Output: False

# issubset()
# Returns True if all elements of the set are present in another set, otherwise False
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
print(s1.issubset(s2))  # Output: True
s1 <= s2  # Output: True

# issupset()
# Returns True if all elements of another set are present in the set, otherwise False
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
print(s1.issuperset(s2))  # Output: True
s1 >= s2  # Output: True

# Set questions: 
# 1) Create a set containing 5 different colors and print it.
colors = {"red", "blue", "green", "yellow", "purple"}
print(colors)

# 2) Add elements to a set:
numbers = {10, 20, 30, 40, 50}
numbers.add(60)
print(numbers)

# 3) Remove an element from a set:
numbers.remove(30)
print(numbers)

# 4)use the discard() create set discard 500 print sets
numbers.discard(500)
print(numbers)

# You're studying tutorials but not building projects.
# You're learning too many things and mastering none.

# Python
# SQL
# APIs
# Pandas basics
# Automation scripts


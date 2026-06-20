# Creating a function
# def Palindrome(a):
#     copy = a
#     rev = 0
#     while a > 0:
#         rev = rev * 10 + a % 10
#         a = a//10

#     if rev == copy:
#         print(f"{rev} is a palidrome no.")
#     else :
#         print(f"{rev} is not a Palidrome no.")

# Palindrome(121)
# Palindrome(1212)

# Palindrome Word
# def palidrome_word(a):
#     rev = ""
#     for i in range(len(a)-1, -1, -1):
#         rev += a[i]

#     if a==rev:
#         print("It's Palindrome Word")
#     else:
#         print("It's Not a Palindrome Word")

# palidrome_word("NAMAN")
# palidrome_word("NAMASTE")


# Types of Argument

# 1) Postional Argument

# def pos(a,b,c,d):
#     print(a+b+c+d)
# pos(1,2,3,4) # a=1 b=2 c=3 d=4

# 2) Default Argument
# def default_arg(name = "Nidhi"):
#     print(f"My Name is {name}")
# default_arg() # we does not need to provide any agrument while calling function also we can provide value to variable as well.

# 3) KeyWord Argument

# def keyword_arg(a,b,c):
#     print(a-b-c)
# keyword_arg(c=4,a=10,b=1) 


# LIST
# ordered, mutable, Indexing start from 0

l = [10,12,12,32,43,12]
# l[1] = 13
# print(l) you can change the value as well

# for i in range(0,len(l)):
#     print(f"{i} = {l[i]}")

# user_list = [10,20,30,40,50]
# user_list.append(60) #append : add value at last 

# user_list.insert(0,0) #insert : add value at specified position 

# user_list.pop() #pop : Removes and returns an element from the list.removes an element by index, not by value.It returns the removed element, so you can store it in a variable. If no index is provided, pop() removes and returns the last element.

# user_list.remove(0) #remove : Removes the first occurrence of the specified value from the list. removes an element by value, not by index. does not return the removed value. If the value appears multiple times, only the first occurrence is deleted.

# user_list.sort() #sort : Sorts the original list directly.Does not return a new sorted list. By default, sorts in ascending order. Use reverse=True for descending order. works for string and numbers.

# user_list.reverse() #reverse : Reverses the current order of elements

# print(len(user_list))
# print(user_list)


# Q1
# Print all positive and negative elements separately.
# input= [3, -1, 4, -5, 9]
# positive = []
# negative = []
# for i in input:
#     if i > 0:
#         positive.append(i)
#     else:
#         negative.append(i)

# print("Positive elements:", positive)
# print("Negative elements:", negative)

# Q2
# Find the mean (average) of all list elements.
# elements = [10, 20, 30, 40, 50]
# sum = 0
# for i in elements:
#     sum += i
# mean = sum // len(elements)
# print("Mean of the list elements:", mean)
# mean = sum(elements) / len(elements)

# Q3
# Find the greatest element and print its index.
# Input: [4, 8, 2, 9, 1]
# elements = [4, 8, 2, 9, 100]
# lar = elements[0]
# index = 0
# for i in range(len(elements)):
#     if lar < elements[i]:
#         lar = elements[i]
#         index = i
# print(f"The greatest element is {lar} and its index is {index}")

# Q4
# Find the second greatest element.
# Input: [4, 8, 2, 9, 1]
a = [4, 8, 2, 9, 100]
largest = a[0]
second_largest = a[0]
for i in a:
    if largest < i :
        second_largest = largest
        largest = i
    elif second_largest < i and i != largest:
        second_largest = i
print(f"The second greatest element is {second_largest}, and the greatest element is {largest}")
# ind= 0
# for i in range(len(a)):
#     if largest < a[i]:
#         largest = a[i]
#         ind = i
# print(f"The greatest element is {largest} at index {ind}")

# Q5
# Check if the list is already sorted.
# Input: [1, 3, 5, 7]
a = [1, 3, 5, 7, 9]
is_sorted = True
for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        is_sorted = False
        print("The list is not sorted.")
        break

else:
    print("The list is already sorted.")

#WRITING FUNCTION FOR Q5
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            print("The list is not sorted.")
            return False
    print("The list is already sorted.")
    return True

is_sorted(a)



#TUPLE 
# ordered, immutable, Indexing start from 0
a = (1, 2, 3, 4, 5)
# a[0] = 10 # you cannot change the value of tuple as it is immutable
a = (10, 20, 30, 40, 50) # you can reassign the value of tuple but you cannot change the value of tuple
print(a)

print(a.count(10)) # count : returns the number of occurrences of a specified value in the tuple.

print(a.index(30)) # index : returns the index of the first occurrence of a specified value in the tuple. If the value is not found, it raises a ValueError.

def tuple_fun():
    return "Hello, I am a tuple function!", 2026, "Python is fun!"

result = tuple_fun()
msg, year, comment = result
print(msg)      # Output: Hello, I am a tuple function!
print(year)     # Output: 2026
print(comment)  # Output: Python is fun!


# You're studying tutorials but not building projects.
# You're learning too many things and mastering none.

# Python
# SQL
# APIs
# Pandas basics
# Automation scripts


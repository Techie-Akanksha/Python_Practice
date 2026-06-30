#Practice Problems:

#1. Create a tuple of 10 numbers and print only the even numbers. 
num = (1,2,3,4,5,6,7,8,9,10)
for i in num:
    if i % 2 == 0:
        print(i)

# 2. Given:
# employees = (
#     ("John", 50000),
#     ("Emma", 65000),
#     ("Mike", 55000)
# )
# Print the employee name with the highest salary.

employees = (
    ("John", 50000),
    ("Emma", 65000),
    ("Mike", 55000)
)

highest_name = employees[0][0]
highest_salary = employees[0][1]

for employee in employees:
    if employee[1] > highest_salary:
        highest_salary = employee[1]
        highest_name = employee[0]
print(f"{highest_name} is person who has highest salary")

# 3.Given:
# marks = (85, 92, 78, 96, 88)
# Find:
# o	Maximum mark 
# o	Minimum mark 
# o	Average mark

marks = (85, 92, 78, 96, 88)
max_marks = marks[0]
min_marks = marks[0]
total = 0
tuple_len = len(marks)
for mark in marks:
    if mark < min_marks:
        min_marks = mark

    elif mark > max_marks:
        min_marks = mark

    total+=mark

average_mark = total/tuple_len
print(f"Maximum Marks : {max_marks}")
print(f"Average Marks : {average_mark}")
print(f"Minimum Marks : {min_marks}")

# 4.Remove duplicates from:
nums = (1, 2, 2, 3, 4, 4, 5, 5)
nums = tuple(set(nums))
print(f"Tuple without duplicate values {nums}")

# 5.Sort the tuple:
t = (9, 2, 7, 1, 5)
sort = tuple(sorted(t))
print(f"Sorted tuple : {sort}")

# 6.Find the second largest element in:
nums = (10, 5, 20, 8, 15)
lg_value = nums[0]
second_lg = nums[0]
for i in nums:
    if lg_value < i:
        second_lg = lg_value
        lg_value = i
    elif i > second_lg and i != lg_value:
        second_lg = i

print(f"Second largest value : {second_lg}")
 
# 7.Check whether a tuple is a palindrome:
t = (1, 2, 3, 2, 1)
is_palindrome = True
for i in range(len(t)//2): #if (len = 5)//2 = 2 so iteration happens 2 times
    #Why 2: Because after reaching the middle, the comparisons would repeat.

    if t[i] != t[len(t)-1-i]:
        is_palindrome = False
        break

if is_palindrome:
    print("It's palindrome")
else:
    print("It's not palindrome")


# For Word Palindrome 

# 1) Using a loop
# word = "madam"

# is_palindrome = True

# for i in range(len(word) // 2):
#     if word[i] != word[len(word) - 1 - i]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not a palindrome")
    
# 2)Using string slicing

# word = "madam"

# if word == word[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# 8.Merge two tuples and remove duplicates

t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

# merge = tuple(set(t1+t2))
merged = t1 + t2
result = ()
for i in merged:
    if i not in result:
        result+=( i,)

print(f"Merge two tuples : {result}")

# 9. Given a tuple of strings:Find the longest word.
words = ("apple", "banana", "kiwi", "grapes", "mango")
long_word = words[0]
for i in words:
    if len(long_word) < len(i):
        long_word = i
print(long_word)

# 10.	Create a nested tuple containing student details:
# Find the student with the highest average score.
details = (
    ("Alice", (85, 90, 88)),
    ("Bob", (78, 80, 82)),
    ("Charlie", (92, 95, 91))
)
student = details[0][0]
high_avg_score = (details[0][1][0]+details[0][1][1]+details[0][1][2])/len(details[0][1])
for detail in details:
    name = detail[0]
    score = detail[1]
    avg = (score[0]+score[1]+score[2])/len(score)
    if high_avg_score < avg:
        high_avg_score = avg
        student = name
print(f"Student name is {student} who has highest average score")

#Set Questions:
#1) Create a set containing: 10, 20, 30, 40, 50 Print the set.
num = {10,20,30,40,50}
print(num)
# 2)Create a set:{1, 2, 3}Add 4 and 5 to it.
numbers = {1, 2, 3}

numbers.add(4)
numbers.add(5)

print(numbers)

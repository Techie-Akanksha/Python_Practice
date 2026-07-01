#Practice Problems:

#Set Questions:
#1. Create a set containing: 10, 20, 30, 40, 50 Print the set.
num = {10,20,30,40,50}
print(num)
# 2. Create a set:{1, 2, 3} Add 4 and 5 to it.
numbers = {1, 2, 3}
numbers.add(4)
numbers.add(5)
print(numbers)

# 3. Remove an element
new = {10, 20, 30, 40}
new.remove(20)
print(new)

# 4. Use discard() Try to discard 500. Print the set.
new.discard(500)
print(new)

# 5. Pop an element
fruits = {"apple", "banana", "mango"}
popped_element = fruits.pop()
print("Popped element:", popped_element)
print("Remaining set:", fruits)

# 6. Count unique elements
ele = [1, 2, 2, 3, 4, 4, 5]
print("Unique elements:", set(ele))

# 7. Remove duplicates
ele = [10, 20, 20, 30, 40, 40]
print("List without duplicates:", list(set(ele)))

# 8. Find common elements
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Common elements:", A & B) 

# 9. Find unique elements. Find elements present in A but not in B.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Unique elements in A :", A - B)

# 10. Merge two sets
A = {1, 2, 3}
B = {4, 5, 6}
print("Merged set:", A | B)

# Loop-Based Questions
# 11. Print all elements
s = {10, 20, 30, 40}
for i in s:
    print(i)

# 12. Find maximum element
s = {25, 10, 45, 5, 60}
max_value = None
for num in s:
    if max_value is None or num > max_value:
        max_value = num
print("Maximum element:", max_value)

# 13. Find minimum element
s = {25, 10, 45, 5, 60}
min_value = None
for num in s:   
    if min_value is None or num < min_value:
        min_value = num
print("Minimum element:", min_value)

# 14. Sum of all elements
s = {10, 20, 30, 40}
total_sum = 0
for num in s:
    total_sum += num
print("Sum of all elements:", total_sum)    
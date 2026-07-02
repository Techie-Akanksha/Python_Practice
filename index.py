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

# 15. Ask the user for a number and check whether it exists in the set.
s = {10, 20, 30, 40, 50}
num = int(input("Enter a number: "))
if num in s:
    print(f"{num} is present in the set.")
else:
    print(f"{num} is not present in the set.")

# 16. Find duplicate values from a list
lst = [1, 2, 3, 4, 5, 2, 3, 4]
duplicates = set()
for num in lst:
    if lst.count(num) > 1:
        duplicates.add(num)
print("Duplicate values:", duplicates)

# Count the number of unique elements in a list
lst = [1, 2, 3, 4, 5, 2, 3, 4]
unique_elements = set(lst)  
print("Number of unique elements:", len(unique_elements))

# 17. Character frequency using sets
input ="programming"
input = set(input)
print("Character frequency:" , input)

# 18. Find vowels in a string using sets
input = "hello"
vowels = set("aeiou")
found_vowels = set()
for char in input:
    if char in vowels:
        found_vowels.add(char)
print("Vowels found:", found_vowels)

# Alternative approach
vowels = set(input) & set("aeiou")
print("Vowels found:", vowels)

# 19. Check if two sets are equal
A = {1, 2, 3}
B = {3, 2, 1}
print("Sets are equal:", A == B)

# 20. Remove all elements from a set. Remove all elements one by one using pop().
s = {1, 2, 3, 4, 5}
while s:
    popped_element = s.pop()
    print("Popped element:", popped_element)
print("Remaining set:", s)

# 21.Create two sets:•	Even numbers •	Odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = set()
odd_numbers = set()
for num in numbers:
    if num % 2 == 0:
        even_numbers.add(num)
    else:
        odd_numbers.add(num)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
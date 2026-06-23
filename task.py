# import random
# com = random.randint(1,100)
# chance = 0
# while True:
#     user = int(input("Guess the number between :- "))
#     chance += 1
#     if com == user:
#         print("Congratulations Buddy you guessed it right !")
#         print(f"You took {chance} Chances to correct guess !")
#         break
    
#     elif com > user:
#         print("Wrong! Go little Upwards..")
    
#     elif com < user:
#         print("Wrong! go little lower")


# import random

# choices = ["stone", "paper", "scissor"]

# computer_choice = random.choice(choices)

# print("Computer chose:", computer_choice)



# Challenge Question ⭐
# Input: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Create two sets: Even numbers, Odd numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = {x for x in numbers if x % 2 == 0}
odd_numbers = {x for x in numbers if x % 2 != 0}
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# using function, loop, conditional statements
even_set = set()
odd_set = set()
def even_odd_sets(num):
    for i in num:
        if i % 2 == 0:
            even_set.add(i)
        else:
            odd_set.add(i)
    return even_set, odd_set

# print(f"Even numbers: {even_odd_sets(numbers)[0]}")
# print(f"Odd numbers: {even_odd_sets(numbers)[1]}")

even_odd_sets(numbers)
print("even numbers:", even_set)
print("odd numbers:", odd_set)

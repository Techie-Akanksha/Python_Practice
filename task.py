import random
com = random.randint(1,100)
chance = 0
while True:
    user = int(input("Guess the number between :- "))
    chance += 1
    if com == user:
        print("Congratulations Buddy you guessed it right !")
        print(f"You took {chance} Chances to correct guess !")
        break
    
    elif com > user:
        print("Wrong! Go little Upwards..")
    
    elif com < user:
        print("Wrong! go little lower")


# import random

# choices = ["stone", "paper", "scissor"]

# computer_choice = random.choice(choices)

# print("Computer chose:", computer_choice)
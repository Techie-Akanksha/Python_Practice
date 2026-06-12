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

for i in range(0,len(l)):
    print(f"{i} = {l[i]}")





# Q1
# Print all positive and negative elements separately.
input= [3, -1, 4, -5, 9]
positive = []
negative = []
for i in input:
    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
print(positive)
print(negative)

# Q2
# Find the mean (average) of all list elements.
    
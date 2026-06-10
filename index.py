# 1) Create Table
# n = int(input("Which table you want to :-"))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")

# 2) Odd Even Count
# oddsum = 0
# evensum = 0
# n = int(input("Which table you want to :-"))
# for i in range(1,n+1):
#     if i % 2 == 0:
#         evensum+=i
#     else:
#         oddsum+=i

# print(evensum)
# print(oddsum)

# 3) Reverse String
# a = "Akanksha"
# str =""
# for i in range(len(a)-1,-1,-1):
#     str+=a[i]
# print(str)

# 4) Check palindrome
# a = "NAMAN"
# str =""
# for i in range(len(a)-1,-1,-1):
#     str+=a[i]

# if str == a:
#     print("Yes it's palindrome word")
# else:
#     print("No it's not palindrome word")

# 5) Check if a no. is perfect(sum of factors = the number itself)
# n = int(input("Enter a number: "))

# sum_factors = 0

# for i in range(1, n // 2 + 1):
#     if n % i == 0:
#         sum_factors += i

# if sum_factors == n:
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")

# 6) count symbols from string
# str = "!@#$%^&*()1231123213adhjkdkjfsjksdfhsf"
# char = 0
# spchar = 0
# digits = 0
# for i in str:
#     if i.isalpha():
#         char+=1
#     elif i.isdigit():
#         digits +=1
#     else:
#         spchar+=1
# print(f"char {char}, special character {spchar}, digits {digits}")

# str = "!@#$%^&*()1231123213adhjkdkjfsjksdfhsf"
# char = 0
# spchar = 0
# digits = 0
# for i in str:
#     if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
#         char+=1
#     elif ord(i)>=48 and ord(i)<=57:
#         digits +=1
#     else:
#         spchar+=1
# print(f"char {char}, special character {spchar}, digits {digits}")

# a = 123
# while a > 0:
#     print(a%10)
#     a //= 10 

# a = 1212
# b = 0
# c = a
# while a > 0:
#        b = b * 10 + a % 10
#        a //= 10  
# if c == b:
#        print(f"this {c} is palindrome")
# else :
#        print(f"{c} not palindrome")
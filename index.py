#Exception Handling

# ❌ Errors (unfixable)
# SyntaxError — wrong syntax
# IndentationError — bad spacing
# TabError — mixing tabs/spaces

# ✅ Exceptions (handleable!)
# ZeroDivisionError
# ZeroDivisionError : A ZeroDivisionError occurs when you try to divide a number by zero.

# TypeError: 
# Ex: a= "10" b = 12 print(a+b) this will fail to give ans due to different datatype. when an operation or function is applied to an object of the wrong data type.

# ValueError: Ex: int("Hello") Error occurs when a function receives an argument of the correct type but with an invalid value.

# ValueError → The type is correct, but the value is invalid.
# TypeError → The type itself is incorrect. 

#FileNotFoundError
# A FileNotFoundError is a Python exception that occurs when you try to open or access a file that does not exist at the specified path.

# num = int(input("Provide no which you want to divide 10 : "))
# try:
#     result = 10 // num
# except ZeroDivisionError: 
#     print("Can't divide by zero!")
# else: 
#     print("Success:", result)
# finally: 
#     print("This always runs.")

try: 
    num = int(input("Enter Positive number : "))
    if 0 > num :
        raise ValueError("Negative value are not allowed.")
    
    result = 100 // num 

except ValueError as e:
    print("ValueError :",e)

except ZeroDivisionError:
    print("You cannot divide by zero")

else:
    print("Division Result: ", result)

finally:
    print("Program Execution Completed")

# try values : 10, 0, -5, abc

# Keyword	Code	Purpose
# try	try:	Wraps code that might cause an exception.
# raise	raise ValueError("Negative numbers are not allowed.")	Manually throws an exception if the number is negative.
# except	except ValueError..., except ZeroDivisionError...	Catches and handles specific exceptions.
# else	print("Division Result:", result)	Runs only if no exception occurs.
# finally	print("Program execution completed.")	Always runs, whether an exception occurs or not.
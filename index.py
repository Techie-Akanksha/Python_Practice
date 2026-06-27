# File Modes

# Mode	Meaning	Creates file?
# 'r'	Read only	❌ (must exist)
# 'w'	Write (overwrites!)	✅
# 'a'	Append to end	✅
# 'x'	Create (fails if exists)	✅

# "x" creates the file if it's not exist
# open("hello.txt","x")

#write file 
new_file = open("hello.txt","w")
data = input("Enter the data which you want in your file : ")
new_file.write(data)

#read the file
read = open("hello.txt","r")
print(read.read())

#Append the content in the file 
file = open("hello.txt","a")
file.write("\n This are newly added content in this file.")

# with open("te.py", "w") as f:
#     f.write("hello python")

# with open("te.txt", "r") as f:
#     content = f.read()
#     print(content)

# with open("te.txt","a") as f:
#     f.write("\nAdded a new line")
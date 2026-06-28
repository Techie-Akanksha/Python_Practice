import os
from pathlib import Path

def createfile():
    try: 
        filename = input("Enter your file name : ")
        path = Path(filename)
        if not path.exists():
            with open(path, "w") as f:
                data = input("Enter your content inside your file : ")
                f.write(data)
            print("File created successfully")
        else:
            print("Error your file is already exists")
    
    except Exception as err:
        print(f"an error occured due as {err}")


def updatefile():
    pass
def readfile():
    pass
def deletefile():
    pass

print("press 1 for creating a new file")
print("press 2 for updating an existing file")
print("press 3 for reading an existing file")
print("press 4 for deleting a file")

response = int(input("Enter your response here :- "))

if response == 1:
    createfile()
elif response == 2:
    updatefile()
elif response == 3:
    readfile()
elif response == 4:
    deletefile()
else:
    print("Error: Your are not selecting proper action")


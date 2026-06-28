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
        print(f"an error occured as {err}")


def updatefile():
    try : 
        filename = input("Enter file name you want to update : ")
        path = Path(filename)
        if path.exists():
            print("Operations")
            print("1. Renaming the file")
            print("2. Append the content")
            print("3. Overwriting the file")

            choice = int(input("Enter your operation :- "))

            if choice == 1:
                new_filename = input("Enter new file name :- ")
                new_path = Path(new_filename)
                if not new_path.exists():
                    path.rename(new_path)
                    print("Renamed Successfully")
                else:
                    print("Error this file name already exists")
        
            elif choice == 2:
                with open(path,"a") as fs:
                    content = input("What do you want to append : ")
                    fs.write("\n" + content)
                print("Content append successfully")

            elif choice == 3:
                with open(path,"w") as fs:
                    content = input("Enter content to overwrite in file : ")    
                    fs.write(content)
                print("Successfully overwritten")

            else : 
                print("Error: Select proper action")

        else:                        
            print("Error file not exists")

    except Exception as err:
        print(f"an error occured as {err}")  


def readfile():
    try : 
        filename = input("Enter your file name : ")
        path = Path(filename)
        if path.exists():
            with open(path, "r") as fs:
                content = fs.read()
                print(f"Your file content is \n {content}")
        else:
            print("Error no such file exists")

    except Exception as err:
        print(f"an error occured as {err}")

def deletefile():
    try:
        filename = input("Enter your file name : ")
        path = Path(filename)
        if path.exists():
            path.unlink()
            print("File deleted successfully")
        else:
            print("Error there is no such file exists")

    except Exception as err:
        print(f"an error occured as {err} ")

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
    print("Error: Select proper action")


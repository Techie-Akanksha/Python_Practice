from pathlib import Path

# Function to create file
def create_file():
    try: 
        filename = input("Enter your file name : ")
        path = Path(filename)
        if not path.exists():
            # encoding="utf-8"avoids issues with non-English text.
            with open(path, "w", encoding="utf-8") as f:
                data = input("Enter your content inside your file : ")
                f.write(data)
            print("File created successfully")
        elif not filename.strip():
            print("Filename cannot be empty. Try again.")
        else:
            print("Error your file is already exists")
    
    except Exception as err:
        print(f"an error occured as {err}")

# Function to update file
def update_file():
    try : 
        filename = input("Enter file name you want to update : ")
        path = Path(filename)

        if not filename.strip():
            print("Please enter filename again.")
            

        elif path.exists():
            print("Operations")
            print("1. Renaming the file")
            print("2. Append the content")
            print("3. Overwriting the file")

            try:
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
                    # encoding="utf-8"avoids issues with non-English text.
                    with open(path,"w",encoding="utf-8") as fs:
                        content = input("Enter content to overwrite in file : ")    
                        fs.write(content)
                    print("Successfully overwritten")
                else:
                    print("Please Select proper action")

            except ValueError as err:
                print("ValueError:",err)

        else:                        
            print("Error: File doesn't exist.")
            tocreate = input("Create it? (y/n) : ")
            if tocreate.lower() == "y":
                create_file()
            else:
                print("Get your response : File doesn't exist")


    except Exception as err:
        print(f"an error occured as {err}")  

# Function to read the file
def read_file():
    try : 
        filename = input("Enter your file name : ")
        path = Path(filename)
        if not filename.strip():
            print("Please enter filename again.")

        elif path.exists():
            with open(path, "r") as fs:
                content = fs.read()
                print(f"Your file content is \n{content}")

        else:
            print("Error: No such file exists")

    except Exception as err:
        print(f"an error occured as {err}")

# Function to delete file
def delete_file():
    try:
        filename = input("Enter your file name : ")
        path = Path(filename)
        if not filename.strip():
            print("Invalid Action. Enter your file name.")

        elif path.exists():
            confirm = input("Deleting this file? (y/n): ")

            # Taking confirmation from user before deleting file. 
            if confirm.lower() == "y":
                path.unlink()
                print("File deleted successfully")
            else :
                print("Thanks for confirming! Your file is not deleted.")

        else:
            print("Error: There is no such file exists")

    except Exception as err:
        print(f"an error occured as {err} ")



print("""1. Create
2. Update
3. Read
4. Delete""")
    
try : 
    response = int(input("Enter your response here :- "))
except ValueError:
    print("Please enter numbers only.")

    
if response == 1:
        create_file()
elif response == 2:
        update_file()
elif response == 3:
        read_file()
elif response == 4:
        delete_file()
else:
        print("Error: Select proper action")


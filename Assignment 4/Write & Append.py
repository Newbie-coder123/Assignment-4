import os
file_name="txt"
if os.path.exists(file_name):
    print("The file exists\n")
else:
    print("The file does not exist creating a new file\n")
    file = open("txt", "xt")
    file.close()
    print("New file created")

print(" 1: Enter 1 to write the text in the file. All previous data will be erased")
print(" 2: Enter 2 to append the text in the file")
print(" 3: Enter 3 to print and read the contents of the file ")
print(" 4: Enter 4 to exit the program")

while True:
    choice = input("Enter your choice: ")
    if choice=="1":
        print("You have chosen to write text in the file. Previous data will be erased")
        stuff=input("Enter text you want to write in this file: ")
        file=open("txt", "wt")
        file.write(stuff)
        file.close()
        print("Data written successfully")
        print("===============================\n")
    elif choice=="2":
        print("You have chosen to append the text in the file.")
        stuff1=input("Enter text you want to append in this file: ")
        file=open("txt", "at")
        file.write(f"\n{stuff1}")
        file.close()
        print("Data appended successfully")
        print("==============================\n")
    elif choice=="3":
        print("You have chosen to read the contents of the file. Contents are: \n")
        file=open("txt", "rt")
        lines = file.readlines()
        i = 1
        for line in lines:
            print(line.rstrip('\n'))
            i = i + 1
        file.close()
        print("===============================\n")
    elif choice=="4":
        print("You have chosen to exit the program")
        print("===============================\n")
        break
        break
    else:
        print("Please enter a valid choice")
        print("===============================\n")

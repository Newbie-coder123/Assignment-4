import os
file_name="Sample.txt"
if os.path.exists(file_name):
    print("The file exists\n")
    file = open("Sample.txt", "rt")
    lines = file.readlines()
    i=1
    for line in lines:
        print(f"Line {i}:",line.rstrip('\n'))
        i=i+1
    file.close()
else:
    print("The file does not exist")
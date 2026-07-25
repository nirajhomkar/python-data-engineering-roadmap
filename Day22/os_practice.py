import os
print("Current Working Directory:")
print(os.getcwd())

print()

print("Files and Folders:")
print(os.listdir())

print()

if(os.path.exists("Data")):
    print("Folder 'Data' already exists!")
else:
    os.mkdir("Data")
    print("Folder 'Data' created successfully!")

print("Files and Folders:")
print(os.listdir())
print("Folder 'Data' created successfully!")

print(os.path.isfile("os_practice.py"))

print(os.path.isdir("Data"))

print(os.rename("Data","Raw_Data"))

print("Files and Folders:")
print(os.listdir())
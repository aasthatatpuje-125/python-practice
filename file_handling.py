# Writing to file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a file handling example.\n")
    file.write("Python is powerful.")

# Reading from file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)
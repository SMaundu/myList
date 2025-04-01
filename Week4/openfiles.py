#open files

with open("Week4/example.txt", "r") as file:
    content = file.readline()
    print(content)

with open("Week4/output.txt", "w") as file:
    file.write("Hello Python, this is a text file")
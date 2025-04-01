try:
    with open("sample.txt", "r") as file:
        data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
   print("Execution completed.")
# In this example, the finally block will always execute, regardless of whether an exception occurred or not.
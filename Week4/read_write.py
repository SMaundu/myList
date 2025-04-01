def read_and_write_file():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, "r") as file:
            content = file.read()
        
        modified_content = content.upper()  # Example modification: Convert to uppercase
        new_filename = "modified_" + filename

        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_write_file()

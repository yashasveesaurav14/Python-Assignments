filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        print("\nFile opened successfully!\n")
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found. Please enter a correct file name.")

except PermissionError:
    print("Permission denied. Cannot access this file.")

except Exception as e:
    print("Something went wrong:", e)
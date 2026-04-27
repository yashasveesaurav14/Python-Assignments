file = open("StudentInfo.txt", "w")
file.write("Name: Yashasvee Saurav\n")
file.write("Course: Computer Engineering\n")
file.close()

print("File created successfully")

with open("StudentInfo.txt", "r") as file:
    print("\n--- File Contents ---")
    data = file.read()
    print(data)

with open("StudentInfo.txt", "a") as file:
    file.write("Division: SOC15\n")
    file.write("Subject: Python Programming\n")
    print("\nNew details added")

with open("StudentInfo.txt", "r") as file:
    print("\n--- Updated File Contents ---")
    updated_data = file.read()
    print(updated_data)
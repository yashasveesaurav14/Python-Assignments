import csv

row_count = 0

file_path = "student_data.csv"

with open(file_path, "r") as file:
    reader = csv.reader(file)
    
    print("CSV File Contents:\n")
    for row in reader:
        print(row)
        row_count += 1

print("\nTotal number of rows:", row_count)
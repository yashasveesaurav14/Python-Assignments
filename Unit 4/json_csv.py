import json
import csv

json_data = '''
[
    {"Name": "Yashasvee Saurav", "Age": 19, "City": "Pune"},
    {"Name": "Riya Sharma", "Age": 20, "City": "Nagpur"},
    {"Name": "Aman Verma", "Age": 21, "City": "Mumbai"}
]
'''

data = json.loads(json_data)

with open("student_data.csv", "w", newline="") as csv_file:
    headers = data[0].keys()
    
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

print("Student data converted from JSON to CSV successfully!")
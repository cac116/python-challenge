#Import the os module to create file parths accros operating systems
import os

#Import module to read CSVs
import csv

# Specify the file to read from
filepath = os.path.join("raw_data", "employee_data1.csv")
#We are storing date data on 'date' and revenue data on 'revenue'
emp_id = []
full_name = []
dob = []
formated_dob = []
ssn = []
state = []

first_name = []
last_name = []

dob_year = []
dob_month = []
dob_day = []

new_employee_data = []

with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        emp_id.append(row["Emp ID"])
        name = row["Name"]
        dob = row["DOB"]
        ssn = row["SSN"]
        state = row["State"]


        # email = f"{first_name}.{last_name}@example.com"
        # new_employee_data.append(
        #     {
        #         "first_name": row["first_name"],
        #         "last_name": row["last_name"],
        #         "ssn": row["ssn"],
        #         "email": email
        #     }
        # )

    print(emp_id)
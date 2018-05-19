## Import the os module to create file parths accros operating systems
import os

## Import module to read CSVs
import csv

## State abreviations dictionary
abbrev_dict = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

## Specify the file to read from and to write to
input_file = os.path.join('raw_data','employee_data1.csv')
output_file = os.path.join('formated_employee_data1.csv')

### Empy lists used to store the raw data

## Raw Emp ID data
emp_id = []

## Raw Name data
full_name = []

## Raw DOB data
dob = []

## Raw SSN data
ssn = []

## Raw State data
state = []

## Separe First Name and Last Name lists after splitting raw Name data
first_name = []
last_name = []

## Separe DOB Year, DOB Month and DOB Day lists after splitting raw DOB data
dob_year = []
dob_month = []
dob_day = []

## Final variable where we'll store the formatted DOB
formated_dob = []

## Final variable where we'll store the formatted SSN
formated_ssn = []

name_to_abbr = []
abbrev = []

with open(input_file, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Loop through csv reader and store raw data on our datastore lists
    for row in csvreader:
        emp_id.append(row[0])
        full_name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])   

# Removing headers Emp ID,Name,DOB,SSN,State. We could have saved this step if we would have used DictReader
# (I did not know how to use it though)
full_name.pop(0)
dob.pop(0)
ssn.pop(0)
state.pop(0)
emp_id.pop(0)

## Sice all columns have the same lenght, we loop till the lenght of full_name (any other variable would've worked too)
for row in range(len(full_name)):
    ## The split method breaks a string and adds the data to a string array using a the difined separator " "
    ## Splitting full_name will result in the array ['First Name', 'Last Name']
    first_name.append(full_name[row].split(" ")[0]) ## Index 0 gives us the First Name that we append to our datastore
    last_name.append(full_name[row].split(" ")[1])  ## Index 1 gives us the First Name that we append to our datastore

    ## Similarly to splitting full_name, we split the raw DOB data using "-" as a separator
    ## This will generate the array ['Year','Month','Day']
    dob_year.append(dob[row].split("-")[0])
    dob_month.append(dob[row].split("-")[1])
    dob_day.append(dob[row].split("-")[2])

    ## Reformated date
    formated_dob.append(f"{dob_month[row]}/{dob_day[row]}/{dob_year[row]}")

    ## Replace first six characters of SSN with "***-**" 
    ssn[row]= ssn[row].replace(ssn[row][0:6],"***-**")

    ## By default, iterating over a dict iterates over its keys
    for key in abbrev_dict:
        ## If current row's state matches current key, the current row's state will be replaced with current dict value
        if state[row] == key:
            state[row] = abbrev_dict[key]

with open(output_file, 'w', newline='') as csvfile:

    ### Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    ## Write the first row (column headers)
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])

    ## Loop to write all formated rows on our txt
    for i in range(len(emp_id)):
        csvwriter.writerow([emp_id[i],first_name[i],last_name[i],formated_dob[i],ssn[i],state[i]])

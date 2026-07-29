import csv

with open("students.csv") as file:
    reader = csv.reader(file)
    #use either one
    #reader1 = csv.DictReader(file)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)
        print(row[0])

    #for row in reader1:
        #print(f"{row["Name"]} is {row["Age"]} year ols and lives in {row["City"]} ")

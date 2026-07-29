import csv
with open("sales.csv") as file:
    reader = csv.DictReader(file)
    total = 0
    for row in reader:
        print(f"{row['Product']} -> {int(row['Quantity']) * int(row['Price'])}")


        total += int(row['Quantity']) * int(row['Price'])

    print(f"Total Revenue = {total}")
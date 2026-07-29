import csv
with open("employees.csv","w",newline="") as file:
    writer =csv.writer(file)
    writer.writerow(["Name","Salary","Department"])
    writer.writerow(["Rahul",50000,"IT"])
    writer.writerow(["Priya",60000,"HR"])
    writer.writerow(["Amit",45000,"Finance"])
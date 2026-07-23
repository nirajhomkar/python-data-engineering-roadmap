from datetime import date, datetime, timedelta

# Current Date and Time
today = date.today()
now = datetime.now()

# Employee Joining Date
joining_date = date(2025, 1, 15)

# Date Calculations
next_salary_date = today + timedelta(days=30)
days_worked = (today - joining_date).days

# Report
print("-" * 35)
print("EMPLOYEE ATTENDANCE REPORT")
print("-" * 35)

print()
print(f"Login Timestamp : {now}")

print()
print(f"Today           : {now.strftime('%A')}")

print()
print(f"Date            : {now.strftime('%d/%m/%Y')}")

print()
print(f"ISO Date        : {now.strftime('%Y-%m-%d')}")

print()
print(f"Current Time    : {now.strftime('%I:%M:%S %p')}")

print()
print(f"Year            : {today.year}")
print(f"Month           : {today.month}")
print(f"Day             : {today.day}")

print()
print(f"After 7 Days    : {today + timedelta(days=7)}")
print(f"After 30 Days   : {today + timedelta(days=30)}")
print(f"15 Days Ago     : {today - timedelta(days=15)}")

print()
print(f"Days Worked     : {days_worked}")

print()
print(f"Next Salary     : {next_salary_date}")

print()
print("-" * 35)
print("Report Generated Successfully!")
print("-" * 35)
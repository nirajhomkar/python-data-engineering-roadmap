import re

log_data = """
INFO: User Niraj logged in.
ERROR: Invalid password for user Rahul.
INFO: Email sent to niraj@gmail.com.
WARNING: Disk usage 85%.
ERROR: Database connection failed.
INFO: Contact: 9876543210
"""

# Find all ERROR messages
error = re.findall("ERROR", log_data)

# Find all INFO messages
info = re.findall("INFO", log_data)

# Extract email addresses
email = re.findall(r"\w+@\w+\.\w+", log_data)

# Extract phone numbers
number = re.findall(r"\d{10}", log_data)

# Print Report
print("-" * 35)
print("LOG ANALYZER REPORT")
print("-" * 35)

print(f"Errors Found  : {len(error)}")
print(f"Info Messages : {len(info)}")

print()

print("Emails:")
print(email)

print()

print("Phone Numbers:")
print(number)
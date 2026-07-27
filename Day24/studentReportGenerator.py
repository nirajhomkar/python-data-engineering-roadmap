from pathlib import Path

# Read marks from file
marks_file = Path("marks.txt")

content = marks_file.read_text()

print("Student Marks:\n")
print(content)

# Create report
report_file = Path("report.txt")

report = "Student Marks Report\n\n" + content

report_file.write_text(report)

print("\nReport Created Successfully!\n")

print(report_file.read_text())
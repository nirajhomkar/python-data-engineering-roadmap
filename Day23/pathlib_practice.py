from pathlib import Path

print("Current Working Directory:")
print(Path.cwd())

print()

file = Path("employees.csv")

print("Does employees.csv exist?")
print(file.exists())
print("Does employees.csv exist and is a file?")
print(file.is_file())

print()

folder = Path("Reports")
folder.mkdir(exist_ok=True)

print("Reports folder created (or  already exits.)")

folder.rename("Logs")

print("Folder renamed to Logs")


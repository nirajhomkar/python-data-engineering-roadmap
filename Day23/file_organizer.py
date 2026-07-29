from pathlib import Path

folder = Path("Raw_Data")
file = folder / "sales.csv"

print("Does sales.csv exist?")
print(file.exists())

print("Is sales.csv a file?")
print(file.is_file())

if file.exists():
    new_file = file.rename(folder / "sales_2026.csv")
    print("File renamed successfully.")

print("\nContents of Raw_Data:")

for item in folder.iterdir():
    print(item.name)
from pathlib import Path
folder = Path("PracticeFolder")

for item in folder.iterdir():
    if item.is_file():
        print(f"{item.name} -> File")
    else:
        print(f"{item.name} -> Directory")

for item in folder.glob("*.txt"):
    print(item)

for item in folder.rglob("*.txt"):
    print(item)
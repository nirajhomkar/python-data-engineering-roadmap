from pathlib import Path

folder = Path("Downloads")

for item in folder.iterdir():
    if item.is_file():
        print(f"{item.name} -> {item.suffix}")

    if item.suffix == ".pdf":
        pdf_folder = folder / "PDFs"
        pdf_folder.mkdir(exist_ok=True)

        item.rename(pdf_folder / item.name)

    if item.suffix == ".png":
        png_folder = folder / "Images"
        png_folder.mkdir(exist_ok=True)

        item.rename(png_folder / item.name)

    if item.suffix == ".csv":
        csv_folder = folder / "CSVs"
        csv_folder.mkdir(exist_ok=True)

        item.rename(csv_folder / item.name)

    if item.suffix == ".txt":
        txt_folder = folder / "TextFiles"
        txt_folder.mkdir(exist_ok=True)

        item.rename(txt_folder / item.name)

    if item.suffix ==".py":
        py_folder = folder / "Python"
        py_folder.mkdir(exist_ok=True)

        item.rename(py_folder / item.name)
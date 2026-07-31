# Day 28 - shutil Module (Python for Data Engineering)

## Topics Covered
- shutil.copy()
- shutil.copy2()
- shutil.move()
- shutil.rmtree()
- shutil.make_archive()

## Concepts Learned
- Copying files
- Preserving metadata during copy
- Moving files after processing
- Deleting directories recursively
- Creating ZIP archives
- Designing a safe backup workflow

## Mini Project
Backup Manager

### Features
- Copies incoming files to a backup folder.
- Preserves metadata using copy2().
- Creates a ZIP archive of the backup folder.
- Moves processed files to the processed folder.

## Key Learning
Learned why ETL pipelines should copy and back up data before moving the original file, ensuring data safety if later steps fail.
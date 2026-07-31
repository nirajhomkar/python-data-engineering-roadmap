import shutil

#Step 1 : Copying the file sales.csv from incoming folder to backup folder with metadata
shutil.copy2("incoming/sales.csv", "backup/sales.csv")

#Step 2 : Creating a zip archive of the backup folder
shutil.make_archive("backup_archive", "zip", "backup")

#Step 3 : Moving the file sales.csv from incoming folder to processed folder
shutil.move("incoming/sales.csv", "processed/sales.csv")

print("Backup completed successfully!")
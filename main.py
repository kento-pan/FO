from pathlib import Path
from datetime import datetime
import os
import shutil

print("### FO - File Organizer ###")
print("Press CTRL + C to stop File Organizer.")

# Creating folders in user/pictures/
path_to_fo = Path.home() / "Pictures" / "FO - File Organizer"
path_to_src_files = path_to_fo / "Move your files in here"
path_to_files_output = path_to_fo / "Organized files"

if not os.path.isdir(path_to_fo):
    os.mkdir(path_to_fo)
if not os.path.isdir(path_to_src_files):
    os.mkdir(path_to_src_files)
if not os.path.isdir(path_to_files_output):
    os.mkdir(path_to_files_output)

print(f"Place your files into the folder {path_to_src_files}.")
print(f"They will be moved to {path_to_files_output}.")

# La magie
while True:
    try:
        # Checking for file in source folder
        for file in os.listdir(path_to_src_files):
            # File paths
            pathjoin_src = os.path.join(path_to_src_files, file)
            pathjoin_copy = os.path.join(path_to_src_files, "duplicate-" + file)
            # Getting and converting the Last Modified time of file
            time_lm = os.path.getmtime(pathjoin_src)
            time_lm_conv = datetime.fromtimestamp(time_lm).strftime("%Y-%m")
            path_to_date_folder = path_to_files_output / time_lm_conv
            # Creating folder by month
            if not os.path.isdir(path_to_files_output / time_lm_conv):
                os.mkdir(path_to_date_folder)
            # Check if file exists already
            if os.path.isfile(path_to_date_folder / file):
                # Check for duplicates and rename file if necessary
                try:
                    # Rename file
                    os.rename(pathjoin_src, pathjoin_copy)
                    print(f"{file} exists already. Renamed to duplicate-{file} and moved.")
                except PermissionError:
                    print("Permission error.")
                    break
            else:
                try:
                    # Move file
                    shutil.move(pathjoin_src, path_to_date_folder)
                    print(f"File {file} moved to {path_to_date_folder}")
                except PermissionError:
                    print("Permission error.")
                    break
    # Exit while loop with CTRL + C
    except KeyboardInterrupt:
        print("File Organizer stopped.")
        break
